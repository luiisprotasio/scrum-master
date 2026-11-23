#!/usr/bin/env python3
"""Render a Markdown scope into a DOCX template without overwriting inputs."""

from __future__ import annotations

import argparse
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


class RenderError(Exception):
    """An actionable input, template, or dependency error."""


WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REQUIRED_FIELDS = ("project_name",)
FIELD_PATTERNS = {
    "project_name": re.compile(r"\{\{\s*project_name\s*\}\}"),
    "body": re.compile(r"\{\{\s*p\s+body\s*\}\}"),
}


def read_markdown(source: Path) -> tuple[dict[str, object], str]:
    """Read simple YAML front matter and return its mapping and Markdown body."""
    try:
        text = source.read_text(encoding="utf-8-sig")
    except OSError as exc:
        raise RenderError(f"Cannot read Markdown file: {source}: {exc}") from exc

    match = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", text, re.S)
    if not match:
        raise RenderError(
            "Markdown needs a YAML front matter block with project_name."
        )

    try:
        import yaml
    except ImportError as exc:
        raise RenderError("Missing dependency: PyYAML. Install it before rendering.") from exc

    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise RenderError(f"Invalid YAML metadata: {exc}") from exc

    if not isinstance(metadata, dict):
        raise RenderError("YAML metadata must be a mapping of field names to values.")

    missing = [
        name
        for name in REQUIRED_FIELDS
        if not isinstance(metadata.get(name), str) or not metadata[name].strip()
    ]
    if missing:
        raise RenderError("Missing required metadata: " + ", ".join(missing))

    date = metadata.get("date")
    if date is not None and not isinstance(date, str):
        if hasattr(date, "isoformat"):
            metadata["date"] = date.isoformat()
        else:
            raise RenderError("Metadata field 'date' must be a string or YAML date.")

    body = text[match.end() :]
    if not body.strip():
        raise RenderError("Markdown body is empty.")
    return metadata, body


def validate_template(template: Path) -> None:
    """Ensure the DOCX contains all fields required by the renderer."""
    if not template.is_file():
        raise RenderError(f"Template does not exist: {template}")

    try:
        with zipfile.ZipFile(template) as archive:
            document_xml = archive.read("word/document.xml")
    except (OSError, zipfile.BadZipFile, KeyError) as exc:
        raise RenderError(f"Not a readable Word DOCX template: {template}") from exc

    try:
        root = ET.fromstring(document_xml)
    except ET.ParseError as exc:
        raise RenderError(f"Template has invalid Word document XML: {template}") from exc

    text_runs = [
        node.text or ""
        for node in root.iter(f"{{{WORD_NS}}}t")
    ]
    missing = [
        field
        for field, pattern in FIELD_PATTERNS.items()
        if not any(pattern.search(text) for text in text_runs)
    ]
    if missing:
        labels = {
            "project_name": "{{project_name}}",
            "body": "{{p body}}",
        }
        formatted = ", ".join(labels[field] for field in missing)
        raise RenderError(
            f"Template is missing required fields or body anchor: {formatted}. "
            "Place each marker in one Word text run."
        )


def validate_output_path(source: Path, template: Path, output: Path) -> None:
    """Reject overwrites of existing files and any input document."""
    output_resolved = output.resolve()
    protected = (source.resolve(), template.resolve())
    if output_resolved in protected:
        raise RenderError("Output path must differ from the Markdown and DOCX template paths.")
    if output.exists():
        raise RenderError(f"Output already exists; choose another path: {output}")
    if not output.parent.is_dir():
        raise RenderError(f"Output directory does not exist: {output.parent}")


def missing_dependencies() -> list[str]:
    missing: list[str] = []
    if shutil.which("pandoc") is None:
        missing.append("Pandoc")
    for module, label in (
        ("yaml", "PyYAML"),
        ("docxtpl", "docxtpl[subdoc]"),
        ("docxcompose", "docxtpl[subdoc]"),
        ("docx", "python-docx"),
    ):
        if importlib.util.find_spec(module) is None and label not in missing:
            missing.append(label)
    return missing


def render(source: Path, output: Path, template: Path | None = None) -> None:
    source = source.resolve()
    output = output.resolve()
    selected_template = (template or Path(__file__).resolve().parents[1] / "assets" / "blue.docx").resolve()

    metadata, body = read_markdown(source)
    validate_output_path(source, selected_template, output)
    validate_template(selected_template)

    missing = missing_dependencies()
    if missing:
        raise RenderError("Missing dependencies: " + ", ".join(missing) + ".")

    try:
        from docxtpl import DocxTemplate
    except ImportError as exc:
        raise RenderError("Could not load docxtpl and its subdoc extra.") from exc

    with tempfile.TemporaryDirectory(prefix="to-word-") as temp_dir:
        temp = Path(temp_dir)
        body_markdown = temp / "body.md"
        body_docx = temp / "body.docx"
        body_markdown.write_text(body, encoding="utf-8")

        command = [
            "pandoc",
            "--from=markdown",
            "--to=docx",
            f"--reference-doc={selected_template}",
            f"--resource-path={source.parent}",
            f"--output={body_docx}",
            str(body_markdown),
        ]
        try:
            subprocess.run(
                command,
                cwd=source.parent,
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as exc:
            detail = (exc.stderr or exc.stdout or "Pandoc conversion failed.").strip()
            raise RenderError(f"Pandoc could not convert the Markdown: {detail}") from exc
        except OSError as exc:
            raise RenderError(f"Could not start Pandoc: {exc}") from exc

        try:
            document = DocxTemplate(str(selected_template))
            body_subdocument = document.new_subdoc(str(body_docx))
            context = {
                "project_name": metadata["project_name"],
                "date": metadata.get("date", "") or "",
                "body": body_subdocument,
            }
            document.render(context, autoescape=True)
            with tempfile.NamedTemporaryFile(
                prefix=".to-word-", suffix=".docx", dir=output.parent, delete=False
            ) as staged_file:
                staged_path = Path(staged_file.name)
            try:
                document.save(str(staged_path))
                staged_path.replace(output)
            finally:
                staged_path.unlink(missing_ok=True)
        except Exception as exc:
            if isinstance(exc, RenderError):
                raise
            raise RenderError(f"Could not populate the DOCX template: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Markdown source with YAML metadata")
    parser.add_argument("output", type=Path, help="New DOCX output path")
    parser.add_argument("--template", type=Path, help="Optional custom DOCX template")
    args = parser.parse_args(argv)

    try:
        render(args.input, args.output, args.template)
    except RenderError as exc:
        print(f"to-word: {exc}", file=sys.stderr)
        return 2
    print(f"Created {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

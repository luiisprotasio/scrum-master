import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_docx.py"


def write_template(path: Path, text: str) -> None:
    document = f'''<?xml version="1.0" encoding="UTF-8"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body>
</w:document>'''
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("word/document.xml", document)


class RenderDocxCliTests(unittest.TestCase):
    def run_cli(self, source: Path, output: Path, template: Path | None = None):
        command = [sys.executable, str(SCRIPT), str(source), str(output)]
        if template is not None:
            command.extend(["--template", str(template)])
        return subprocess.run(command, capture_output=True, text=True, check=False)

    def test_missing_project_metadata_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "scope.md"
            source.write_text("# Scope\n\nBody text.\n", encoding="utf-8")
            result = self.run_cli(source, root / "scope.docx")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("project_name", result.stderr)

    def test_template_without_body_anchor_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "scope.md"
            source.write_text(
                "---\nproject_name: Demo\n---\n\n# Scope\n",
                encoding="utf-8",
            )
            template = root / "custom.docx"
            write_template(template, "{{project_name}}")
            result = self.run_cli(source, root / "scope.docx", template)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("body", result.stderr.lower())
        self.assertIn("anchor", result.stderr.lower())

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "scope.md"
            source.write_text(
                "---\nproject_name: Demo\n---\n\n# Scope\n",
                encoding="utf-8",
            )
            template = root / "custom.docx"
            write_template(
                template,
                "{{project_name}} {{p body}}",
            )
            output = root / "scope.docx"
            output.write_bytes(b"existing document")
            result = self.run_cli(source, output, template)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("exist", result.stderr.lower())
            self.assertEqual(output.read_bytes(), b"existing document")

    def test_valid_inputs_do_not_change_sources_when_dependency_is_missing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "scope.md"
            source.write_text(
                "---\nproject_name: Demo\n---\n\n# Scope\n",
                encoding="utf-8",
            )
            template = root / "custom.docx"
            write_template(
                template,
                "{{project_name}} {{p body}}",
            )
            source_before = source.read_bytes()
            template_before = template.read_bytes()
            output = root / "scope.docx"
            result = self.run_cli(source, output, template)

            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(
                "pandoc" in result.stderr.lower()
                or "docxtpl" in result.stderr.lower()
            )
            self.assertFalse(output.exists())
            self.assertEqual(source.read_bytes(), source_before)
            self.assertEqual(template.read_bytes(), template_before)


if __name__ == "__main__":
    unittest.main()

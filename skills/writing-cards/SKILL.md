---
name: writing-cards
description: Use when a Scrum Master needs to create or review sprint or backlog cards/issues from scope documents, briefs, meeting notes, decisions, or other project sources, or publish them to GitHub Projects.
---

# Writing Cards

Turn project sources into one card or a coherent collection. Ask questions in conversation; do not create a local form.

## Workflow

1. **Read sources.** Inspect supplied sources and project conventions. Treat a designated scope as authoritative for its scope; use other sources as context. Surface conflicts and ask which decision governs. Do not turn assumptions into requirements.
2. **Clarify material gaps.** Ask about unknowns that change outcome, scope, acceptance, dependencies, sprint/backlog destination, or publication. Establish single card versus collection and sprint number or backlog; ask when unclear.
3. **Propose architecture first.** Before full cards, show each proposed title, outcome/scope boundary, dependencies, preliminary Fibonacci points, and brief rationale/uncertainty. Use only `1, 2, 3, 5, 8, 13` as relative proposals, never time or team commitments. Split work above 13. Wait for approval/adjustment before detailing. Approval does not authorize sync.
4. **Name and draft.** Use `S{N}-{SIGLA}-{NN} [{TIPO}] [{ÁREAS}] {Resumo}` for sprints and `BKL-{SIGLA}-{NN} [{TIPO}] [{ÁREAS}] {Resumo}` for backlog. Preserve existing IDs and taxonomy; otherwise infer a scope acronym and start two-digit numbering at `01`. Every title needs a type: use team taxonomy or `[FEATURE]` (user-visible capability), `[BUG]` (defect), `[TASK]` (discovery/internal work), `[CHORE]` (maintenance). No free-form types. Optional area tags: `BE`, `FE`, `ARCH`, only when supported. Read [references/card-model.md](references/card-model.md); adapt sections and state unknowns explicitly.
5. **Review all cards.** Give count by status and one row per card with attention points, publication impact, and next action. Use exactly one status: `Pronto para publicação`, `Falta informação`, `Falta detalhamento`, `Conflito entre fontes`, `Dependência bloqueante`, `Revisar escopo`. Only ready cards may sync. Re-review the full collection after changes.
6. **Always create the local index.** Every run creates or updates `.scrum-master/cards/{collection}/` and its index, whether or not individual cards are saved locally. Ensure the project-root `.gitignore` contains `.scrum-master/`, adding it once and preserving other rules. For a sprint, use [references/sprint-index-model.md](references/sprint-index-model.md) and save as `Sprint N/sprint-n-index.md`; for backlog, use a matching collection index. Keep estimates and architecture only in the index, never in individual cards. Mark pre-approval indexes as proposals and update them as plans change. Ask separately whether to save one Markdown file per card in the same folder; save/update those files if requested, including when asked mid-flow.
7. **Sync is separate and opt-in.** Follow [references/github-project-sync.md](references/github-project-sync.md) only when the SM opts in for this run.

## Review output

```markdown
## Revisão dos cards

| Card | Status | Pontos de atenção | Impacto na publicação | Próxima ação |
|---|---|---|---|---|
| [ID e título] | [status definido] | [problema ou “Nenhum”] | [Pronto / Bloqueado] | [ação ou “Nenhuma”] |
```

Readiness requires checking scope, outcome, acceptance, conflicts, dependencies, and duplication—not merely filled template fields.

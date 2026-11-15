---
name: writing-cards
description: Use when a Scrum Master needs to create or review sprint or backlog cards/issues from scope documents, briefs, meeting notes, decisions, or other project sources, or publish them to GitHub Projects.
---

# Writing Cards

Turn project sources into one card or a coherent collection. Ask questions conversationally; do not create a separate form.

## Workflow

1. **Read sources.** Inspect supplied sources and project conventions. Treat a designated scope as authoritative for its scope; use other sources as context. Surface conflicts and ask which decision governs. Do not turn assumptions into requirements.
2. **Ask about sync early.** After reading sources, record any sync decision already given; otherwise ask yes/no in the first clarification turn, before discussing the card breakdown. A yes authorizes only an attempt, subject to capability checks and review. Follow [references/github-project-sync.md](references/github-project-sync.md).
3. **Clarify gaps.** Ask about unknowns that change outcome, scope, acceptance, dependencies, destination, or publication. Establish single card versus collection and sprint number or backlog; ask when unclear.
4. **Propose first.** Before detailing cards, show each proposed title, outcome/scope boundary, dependencies, preliminary Fibonacci points, and brief rationale/uncertainty. Use only `1, 2, 3, 5, 8, 13` as relative estimates, never time or team commitments. Split work above 13. Wait for approval or adjustment.
5. **Draft and save every card.** Follow title rules and [references/card-model.md](references/card-model.md). Always save one Markdown file per card plus the index under `.scrum-master/cards/{collection}/`, including drafts. Ensure the project-root `.gitignore` contains `.scrum-master/`. Use [references/sprint-index-model.md](references/sprint-index-model.md) for paths and format. Estimates and rationale belong only in the index, never individual cards or GitHub data. Update files as the proposal changes.
6. **Review and update files.** Review the whole collection and record each card's attention points and exactly one status in its file and the index: `Pronto para publicação`, `Falta informação`, `Falta detalhamento`, `Conflito entre fontes`, `Dependência bloqueante`, or `Revisar escopo`. Re-review all cards after changes. Only ready cards may sync.
7. **Sync after review.** If the SM opted in, sync eligible cards using the registered integration and rules in [references/github-project-sync.md](references/github-project-sync.md). If not, do not make remote writes.
8. **Report briefly.** Do not print card bodies or the full index in chat. Report status counts, the collection directory, index path, card filenames, and sync outcome. If the SM asks for every card's contents, direct them to the collection directory; show only one specifically requested card at a time.

Readiness requires checking scope, outcome, acceptance, conflicts, dependencies, and duplication—not merely filled template fields.

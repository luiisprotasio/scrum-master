# Índice local de coleção de cards

Create or update this local index on every card-authoring run, even when the Scrum Master declines local copies of the individual cards. It preserves the proposed or approved architecture and preliminary estimates; it is not a GitHub Issue or Project payload.

For a numbered sprint, save as `.scrum-master/cards/Sprint N/sprint-n-index.md`. For general backlog, use a matching collection path and index such as `.scrum-master/cards/Backlog/backlog-index.md`.

```markdown
# Sprint N — Índice de cards

**Estado da proposta:** [Aguardando aprovação / Aprovada / Revisada]
**Fonte(s):** [documento, solicitação ou decisão]

## Arquitetura proposta

| Ordem | ID | Título | Resultado | Dependências | Pontos Fibonacci | Justificativa/risco | Status de revisão |
|---:|---|---|---|---|---:|---|---|
| 1 | [ID] | [Título completo] | [Resultado resumido] | [IDs ou Nenhuma identificada] | [1, 2, 3, 5, 8 ou 13] | [Base e incerteza] | [Status] |

**Total preliminar:** [soma dos pontos; não é prazo nem compromisso da equipe]

## Decisões e dependências da coleção

- [Decisão, fonte conflitante ou dependência] — [impacto e responsável, se conhecido].

## Issues vinculadas (quando houver sincronização)

- [ID do card] — [URL da Issue] — [estado do vínculo ao Project].
```

Keep Fibonacci estimates and rationale in this index only. Do not copy them into individual card files, Issue titles, Issue bodies, labels, comments, Project fields, or other remote metadata. Create the index when the proposal is first presented and update it after approval, revisions, review, and sync outcomes. Mark pre-approval indexes as awaiting approval and preserve unresolved questions. Saving the index is mandatory; saving individual card files remains a separate SM choice.

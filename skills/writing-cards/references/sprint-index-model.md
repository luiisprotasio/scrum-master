# Índice local de coleção de cards

Crie ou atualize este índice em toda execução junto com um arquivo Markdown por card. Ele guarda a arquitetura da coleção e as propostas preliminares de estimativa; nunca é payload de Issue ou Project.

Para uma sprint numerada, use `.scrum-master/cards/Sprint N/sprint-n-index.md`. Para backlog ou outra coleção, use uma pasta e nome de índice correspondentes, por exemplo `.scrum-master/cards/Backlog/backlog-index.md`.

Use blocos curtos por card, em vez de tabelas. Mantenha cada rótulo em uma linha própria para o arquivo continuar legível no terminal e em visualizadores de texto simples:

```markdown
SPRINT 6 — ÍNDICE DE CARDS
Estado da proposta: Aprovada
Fontes: Escopo da Sprint 6; decisão registrada em reunião

RESUMO
Cards: 2
Pontos preliminares: 8 (esforço relativo; não é prazo ou compromisso)

CARD 01
ID: S6-AUTH-01
Título: S6-AUTH-01 [FEATURE] [BE] Recuperar acesso administrativo
Resultado: Permitir que administradores recuperem o acesso à conta.
Dependências: Serviço de envio de e-mail
Estimativa Fibonacci: 5
Base e incerteza: Fluxo conhecido; integração de e-mail precisa ser confirmada.
Revisão: Pronto para publicação
Pontos de atenção: Nenhum
Próxima ação: Nenhuma

----------------------------------------

CARD 02
ID: S6-AUTH-02
Título: S6-AUTH-02 [TASK] [ARCH] Definir política de expiração
Resultado: Registrar a decisão sobre validade dos links de recuperação.
Dependências: Aprovação de Segurança
Estimativa Fibonacci: 3
Base e incerteza: A regra está pendente; esforço pode mudar após a decisão.
Revisão: Falta informação
Pontos de atenção: Prazo de expiração não definido.
Próxima ação: Confirmar a política com Segurança.

----------------------------------------

DECISÕES E DEPENDÊNCIAS DA COLEÇÃO
- [Decisão ou dependência] — [impacto e responsável, se conhecido]

ISSUES VINCULADAS
- S6-AUTH-01 — [URL ou “Não sincronizada”] — [estado do vínculo]
```

Crie o índice ao apresentar a proposta, inicialmente com o estado `Aguardando aprovação`, e atualize após aprovação, mudanças, revisão e sincronização. Guarde estimativas e justificativas somente neste índice — nunca nos arquivos individuais dos cards, títulos, corpos, labels, comentários ou campos do GitHub. Atualize o índice para refletir os arquivos individuais salvos e o resultado da revisão.

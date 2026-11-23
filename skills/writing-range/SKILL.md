---
name: writing-range
description: Use when a product manager needs to clarify a project's boundaries through a conversation and produce a structured Markdown scope document.
---

# Delimitar o escopo de um projeto

Conduza uma conversa com a pessoa responsável pelo produto para entender o problema, os usuários, os resultados esperados e os limites do projeto. Entregue um arquivo Markdown com a estrutura de [`references/example.md`](references/example.md), preenchido conforme [`references/fields.md`](references/fields.md).

## Conversa

1. Leia `references/fields.md` e `references/example.md` antes de iniciar. Leia também os materiais do projeto que a pessoa fornecer ou indicar.
2. Use [`references/questions.md`](references/questions.md) como banco de perguntas. Faça perguntas em rodadas curtas, selecionadas pelas lacunas no entendimento atual. Não despeje o questionário inteiro nem repita algo que já foi respondido.
3. Explore o problema e seu impacto, os usuários e seus objetivos, as capacidades desejadas, as regras de negócio, as restrições e o que ficará fora do escopo. Pergunte sobre sprints somente quando houver ou se esperar um planejamento de entrega.
4. Diferencie fatos confirmados de decisões em aberto. Não invente datas, prazos, papéis, regras, capacidades, prioridades ou plano de sprints. Se uma resposta mudar o escopo, faça uma pergunta de acompanhamento antes de consolidá-la.
5. Antes de salvar, apresente uma síntese curta do escopo e das incertezas relevantes. Peça confirmação ou correções. Continue a conversa até a pessoa confirmar o conteúdo ou indicar que deseja um rascunho com pontos em aberto identificados.

## Arquivo de saída

Depois da confirmação, produza um arquivo Markdown seguindo a ordem, os campos e a sintaxe de `example.md`. Use `fields.md` para preencher metadados, seções e user stories. Mantenha a estrutura do exemplo; não acrescente seções ou formatos sem necessidade ou pedido da pessoa.

Inclua `project_name`. Inclua `date` somente quando a pessoa informar a data e seu significado; escreva-a como `AAAA-MM-DD`. O YAML deve ficar no início do arquivo, sem cercas de código.

Salve no caminho informado pela pessoa. Se ela não indicar um caminho, use `.scrum-master/scopes/{slug-do-projeto}.md` na raiz do projeto e crie a pasta se necessário. Nunca sobrescreva um arquivo existente; escolha um sufixo numérico livre.

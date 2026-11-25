# Descrição dos campos do escopo

Este guia descreve os campos usados em [`example.md`](example.md) e o formato validado para preenchê-los. Os nomes, papéis, quantidade de sprints e funcionalidades do exemplo são ilustrativos; use os dados definidos para cada projeto.

## Metadados

Os metadados ficam em um bloco YAML no início do arquivo. Abra e feche o bloco com `---`. Não cerque esse bloco com marcas de código Markdown.

```yaml
---
project_name: Projeto de exemplo
date: 2025-12-25
---
```

### `project_name`

Nome do projeto descrito no escopo. Escreva como texto simples em uma única linha. Use o nome acordado com as pessoas responsáveis pelo projeto.

### `date`

Data associada ao escopo, no formato `AAAA-MM-DD` (por exemplo, `2025-12-25`). Opcional.

## Seções do escopo

Use títulos Markdown de nível 1 (`#`) para as seções principais, numerados na ordem em que aparecem. Use nível 2 (`##`) para subdivisões, como cada sprint do planejamento.

### 1. Visão geral

Apresente o contexto do projeto, o problema atual e o que a proposta pretende permitir. Escreva em parágrafos curtos. Quando a equipe tiver acordado exclusões, registre os limites do escopo em uma frase clara nesta seção, sem criar uma seção nova. Use uma lista com marcadores para destacar comportamentos ou capacidades importantes. Aplique quebras de linha no início dos parágrafos. O objetivo disso é detalhar, então, detalhe o máximo possível, não se preocupe tanto com pragmatismo.
### 2. Planejamento do projeto

Informe a duração e a quantidade de sprints planejadas. Esses valores precisam refletir o plano acordado; os 15 dias e as duas sprints de `example.md` são apenas dados de demonstração.

Para cada sprint, crie um título de nível 2 (`##`) com o número e um objetivo , por exemplo `## Sprint 1: Agenda e disponibilidade`. Em seguida, descreva o trabalho detalhadamente. não tenha dó de gastar linhas e o resultado esperado naquela sprint. Mantenha o escopo compatível com a capacidade e a duração acordadas. Lembre de seguir a capitalização das letras

### 3. Usuários previstos

Liste os papéis que usarão ou administrarão o produto. Escreva cada papel em negrito, seguido de dois-pontos e das responsabilidades ou ações permitidas. Descreva comportamentos observáveis e inclua somente papéis previstos para o projeto.
Não tenha dó na hora de detalhar.

Formato usado no exemplo: `**Administrador:** cadastra os espaços...`.

### 4. User stories

Converta as necessidades dos papéis em histórias curtas. Cada item começa com um identificador em negrito, seguido de dois-pontos e da estrutura:

`Como [perfil], quero [ação ou capacidade] para [benefício esperado].`

Use ID's numéricos (`US01`, `US02`). Mantenha os IDs únicos e consistentes no documento. Cada história deve expressar uma necessidade e um benefício; não misture várias capacidades independentes em um único item. Não insira bullet ( - ) no início da user storie.

Exemplo:

```markdown
 **US01:** Como administrador, quero cadastrar os espaços disponíveis para que os moradores possam consultá-los ao fazer uma reserva.
```

### 5. Fora de escopo

Liste features que não estão no escopo de forma alguma e não serão implementadas no escopo atual. Descreva o que o campo gaz e liste as uma por uma, explicando elas de maneira simples, exemplo:

```markdown
Durante o desenvolvimento do projeto, podem surgir novas ideias, necessidades, ajustes de fluxo, alterações de regra de negócio, mudanças visuais, integrações adicionais ou funcionalidades que não foram identificadas no momento de diagnóstico e elaboração deste escopo.
&nbsp Essas solicitações serão consideradas funcionalidades não previstas quando não estiverem descritas neste documento ou quando alterarem de forma relevante o funcionamento, a estrutura, os módulos, os fluxos, as permissões, as integrações ou a complexidade da solução inicialmente planejada.
De forma geral, serão tratadas como funcionalidades não previstas:
- Aplicativo nativo para celular.
- Integração com WhatsApp, incluindo envio de mensagens ou lembretes.
- Integração com e-mail para envio de notificações ou lembretes.
- Importação de dados de planilhas existentes.
```

## Validação antes de entregar

- Confirme que `project_name` identifica o projeto e que o YAML está no início do arquivo, sem cercas de código.
- Verifique se cada papel descrito na seção 3 aparece nas histórias relevantes.
- Verifique se as histórias cobrem capacidades descritas na visão geral e no planejamento, sem criar funções ou decisões que o escopo não definiu.
- Confira a sequência dos títulos e dos IDs. Os números de sprint e a quantidade de sprints devem coincidir com o plano acordado.

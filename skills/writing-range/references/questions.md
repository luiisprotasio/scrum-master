# Perguntas sobre o escopo.
Este arquivo documenta as perguntas que você deve fazer ao usuário antes de começar a redigir o escopo.

## 1. Nome do projeto

Definir o nome do projeto é essencial e corresponde a tag {{project_name}} amplamente usada. Diga:

"Qual o nome do projeto que vamos definir o escopo? Responda considerando espaços e maíusculas!"

## 2. Entendendo o projeto

Peça ao usuário para explicar a funcionalidade do projeto e sua história, a fim de popular a visão geral:

"Me conta a história completa de como o negócio funciona hoje, desde o momento em que o cliente chega até a entrega final, e como você imagina isso rodando no sistema: quais são as principais dores e gargalos do processo manual atual, quem são os perfis que vão usar a solução (e o que cada um pode ver ou fazer), onde será acessado (web, app, landing page), como você ganha dinheiro nisso e o que não precisa entrar nesta primeira versão?"

## 3. Entendendo a operação

É hora de definir prazos e a operação em si. Aqui, você vai entender como gerar o planejamento. Faça dois questionamentos:

"Quanto ao prazo do projeto, quanto tempo temos? Como serão divididas as sprints?"

"Para eu dimensionar o cronograma de desenvolvimento e dividir as entregas em etapas: quais funcionalidades precisam existir desde o primeiro dia para a operação começar a rodar, o que pode ser entregue numa segunda etapa, e existe algum gargalo operacional ou dependência externa (como aprovação de cadastro, integração de pagamento, revisão de loja de aplicativo ou entrega de conteúdo por vocês) que trava o avanço de outras partes?"

## 4. Usuários

Aqui você deve definir quais usuários serão usuários da plataforma. Tente inferir pelo que você sabe, e logo peça uma revisão para receber os usuários do projeto corretos.

"Pelo que entendi, o projeto será usado por x, y e z. Certo? Me corrija e vamos entender melhor o que cada um fará dentro do projeto." 

## 5. User stories

Infira da seção anterior o papel de cada usuário para criar User Stories. Você deve seguir a documentação em ../fields.md para criar US o suficiente para cobrir todas as funcionalidades, sempre pedindo revisão de tudo.

## 6. Fora de escopo

Pergunte ao usuário funcionalidades que não serão incluídas de forma alguma no escopo:

"Para finalizarmos, tem algumas funcionalidades que não podem entrar no escopo de forma alguma? Precisamos registrar isso, caso não pense em nada, vou inferir algumas e você revisa."

## Perguntas opcionais de aprofundamento

As seções 1 a 6 acima são o roteiro principal. Use as perguntas abaixo somente quando as respostas deixarem uma lacuna que possa alterar o escopo, as entregas ou as user stories. Não faça todas por padrão.

### Resultado e prioridade

- Como a equipe vai perceber que o projeto resolveu o problema descrito?
- Se não for possível entregar tudo na primeira versão, quais capacidades precisam permanecer e quais podem ser adiadas?

### Regras e exceções

- O que deve acontecer quando uma ação não puder ser concluída, como uma solicitação fora do horário disponível ou um cadastro incompleto?
- Existem limites, permissões ou condições que mudam o fluxo para algum perfil de usuário?

### Dependências e restrições

- Há sistemas, aprovações, dados ou pessoas externas que precisam estar disponíveis para uma entrega funcionar?
- Existe alguma restrição já decidida de prazo, orçamento, plataforma, privacidade ou acessibilidade que limite as opções?

### Validação das histórias

- Qual resultado observável permite confirmar que esta user story foi atendida?
- Há algum caso importante que a história ainda não cobre e que mudaria o comportamento esperado?


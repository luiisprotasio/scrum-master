# Sincronização com GitHub Projects via GitHub CLI

Depois de ler as fontes e antes de propor os cards, registre se o SM quer sincronizar nesta execução. Se ele ainda não respondeu, pergunte nesse primeiro turno. Se responder “sim”, pergunte imediatamente qual é o repositório de destino e se quer vincular as Issues a um GitHub Project; o repositório é obrigatório, o Project é opcional. Se o usuário informar somente o repositório, prossiga criando as Issues nele e não exija nem tente inferir um Project. Um workflow do repositório pode adicioná-las automaticamente. Só prossiga com a sincronização após confirmar o repositório. Toda operação remota deve usar o GitHub CLI `gh`; não use GitHub MCP, outra integração, `gh api` ou chamadas REST diretas.

## Pré-checagem

Confirme o repositório e, somente se o usuário pediu vínculo, o dono e número/título do Project. Antes de criar qualquer Issue, rode verificações somente de leitura:

```bash
gh --version
gh auth status
gh repo view <owner/repo>
```

Rode também `gh project view <project-number> --owner <project-owner>` somente quando houver Project de destino confirmado. Sem Project, não rode comandos `gh project` e não passe `--project` à criação da Issue.

Use comandos compatíveis com a versão instalada. Não use `gh auth status --active --no-refresh`: versões como `gh 2.45.0` não reconhecem essas opções.

Interprete falhas pelo tipo de erro, sem concluir que a conta está desconectada a partir de um erro de rede:

- Se aparecer `error connecting to api.github.com` ou outra falha de conexão, trate como possível bloqueio de rede do sandbox/ambiente. Não peça novo login nem declare o token inválido com base nisso.
- Se o ambiente oferecer uma execução autorizada fora do sandbox, tente novamente a mesma checagem somente de leitura nesse contexto. A autorização do SM para sincronizar já cobre a tentativa de sincronização; siga o mecanismo de aprovação de execução exigido pelo ambiente. Não mude conta nem credenciais.
- Se não houver execução externa disponível, ou ela também falhar, mantenha os arquivos locais e explique que a sincronização está bloqueada por conectividade. Dê ao SM os comandos `gh` necessários para executar em um terminal com acesso ao GitHub.
- Se `gh auth status` realmente indicar autenticação ausente/inválida no contexto com conectividade, explique a evidência e instrua o SM a corrigir a autenticação por conta própria. Nunca execute login, instalação do CLI, refresh de escopos ou troca de conta em nome dele.
- Se a autenticação estiver válida mas faltar o escopo `project`, informe que o CLI não está autorizado a vincular Issues ao Project. Ofereça continuar criando as Issues somente no repositório, sem vínculo manual; o workflow do repositório ainda pode adicioná-las. Se o SM preferir o vínculo direto, instrua-o a executar `gh auth refresh -s project` por conta própria e tente novamente depois. Não trate a falta desse escopo como impedimento para criar Issues no repo.

Uma falha de leitura não prova que uma Issue foi criada; uma falha de escrita pode ser ambígua. Antes de repetir uma criação após erro de conexão, procure a Issue pelo título no repositório e confirme se já existe, para evitar duplicatas. Se não for possível verificar, pare e relate a incerteza em vez de repetir a criação às cegas.

## Criar Issues e adicioná-las ao Project

Sincronize apenas cards com status `Pronto para publicação`. Para cada um, use o arquivo individual — que contém somente o conteúdo voltado ao desenvolvedor — como body:

```bash
gh issue create \
  --repo <owner/repo> \
  --title "<título do card>" \
  --body-file "<caminho-do-card>"
```

Use o comando acima quando o usuário informou somente o repositório. Se também confirmou um Project, inclua `--project "<título-do-project>"` para tentar adicioná-la durante a criação. Se a Issue foi criada sem vínculo e o Project foi confirmado, use o número e owner já confirmados para completar o vínculo:

```bash
gh project item-add <project-number> \
  --owner <project-owner> \
  --url <issue-url>
```

Confira o resultado de cada criação. Quando houver Project confirmado, confirme também que cada Issue foi vinculada antes de relatar sincronização completa. Se a criação der certo mas o vínculo falhar, relate a URL como criada e não vinculada; não crie outra Issue para tentar corrigir o vínculo. Quando não houver Project informado, relate as Issues como criadas no repositório; não afirme que foram adicionadas a um Project, pois um workflow do repositório pode cuidar disso separadamente.

O corpo remoto vem somente do card individual. Nunca envie Fibonacci, justificativas de estimativa, status ou notas da revisão, pontos de atenção, estado de publicação, caminhos/nomes dos arquivos fonte, ou o índice local em título, body, labels, comentários ou campos do Project. Não acrescente links ou citações dos materiais usados para preparar o card, exceto referências técnicas que já estejam no card porque o desenvolvedor precisa delas para implementar o trabalho.

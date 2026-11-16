# Scrum Master Skill

Scrum Master é um pacote de skills para auxiliar o Scrum Master em diversas etapas do scrum.
- Este é um projeto em desenvolvimento, as funcionalidade estarão disponíveis aos poucos.
- Quer contribuir? Sinta-se livre para abrir uma branch e abrir um PR com suas adições! (Alternativamente, sugira algo [aqui](https://github.com/luiisprotasio/scrum-master/issues/new/choose))

## Skills
### `writing-cards`
Skill que auxilia na criação de cards a partir de conteúdo de qualquer tipo.
Tem um documento de escopo, notas de reunião, ou até mesmo um documento de texto informal, contedo qualquer tipo de especificação do projeto? Esta skill transforma conteúdo solto em cards organizados e padronizados, além de automatizar o upload para o GitHub no formato de issues.

Inputs necessários: 
- É preciso um documento/texto explicando algum tipo de escopo/ideia/projeto.
- É preciso identificar a qual repositório remoto (github) as tarefas serão linkadas caso queria a sincronizaçãoa, alternativamente, serão criados todos localmente, em markdown.
- Ainda sobre sincronização: garanta que seu GitHub CLI esteja logado corretamente! A sincronização ocorre por meio do mesmo.

---

## Instalação
Comando para adicionar todas as skills deste repositório:

```bash
npx skills add luiisprotasio/scrum-master --skill '*'
```

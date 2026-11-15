# Guia do projeto para agentes

## O que é este repositório

Este projeto reúne skills para apoiar o trabalho de Scrum Masters. Cada skill ensina um agente a conduzir uma tarefa específica usando instruções reutilizáveis e, quando necessário, referências próprias. O pacote é organizado para instalação com o CLI `npx skills` e uso em agentes compatíveis com o formato Agent Skills.

O projeto está em desenvolvimento. No momento, a skill disponível é `writing-cards`, voltada à criação e revisão de cards de sprint ou backlog e à publicação opcional em GitHub Projects.

## Estrutura

```text
skills/
  writing-cards/
    SKILL.md
    references/
      card-model.md
      github-project-sync.md
      sprint-index-model.md
```

- `skills/<nome>/SKILL.md`: instruções principais da skill. Mantenha o arquivo focado no fluxo e encaminhe detalhes para referências quando isso melhorar a leitura.
- `skills/<nome>/references/`: modelos e orientações especializadas, vinculados a partir do `SKILL.md` correspondente.
- `README.md`: apresentação breve do pacote e informações para quem contribui.

## Regras para alterações

- Preserve a estrutura `skills/<nome>/SKILL.md` para que o CLI encontre cada skill.
- Use nomes de pasta e o campo `name` em minúsculas, com hífens quando necessário; mantenha ambos iguais.
- Escreva `description` como uma indicação clara de quando ativar a skill.
- Mantenha cada skill independente. Compartilhe referências somente quando forem realmente comuns a mais de uma skill.
- Não inclua tokens, credenciais ou configuração de autenticação. Instruções de integração devem usar capacidades já disponíveis no ambiente do agente.
- Registre no `SKILL.md` as decisões específicas da tarefa. Evite transformar convenções de uma skill em regra global deste repositório sem necessidade.
- Para `writing-cards`, pergunte sobre sincronização com GitHub Projects no início do fluxo, depois de ler as fontes. Salve sempre o índice e um arquivo local por card em `.scrum-master/cards/{coleção}/`; mantenha as estimativas Fibonacci somente no índice. Na resposta do agente, informe resumo, status e caminhos sem despejar todos os cards no chat. Use blocos curtos no índice, sem tabelas largas, para facilitar a leitura em terminal e texto simples.

## Teste local

Na raiz do repositório, instale uma skill para o agente desejado:

```bash
npx skills add . --skill writing-cards -a codex
```

Para testar outra skill, substitua `writing-cards` pelo nome da pasta. O CLI pode perguntar o escopo e o método de instalação. Durante desenvolvimento, o symlink mantém a instalação ligada aos arquivos locais; `--copy` instala uma cópia independente.

Valide também o `SKILL.md` com o validador do skill-creator, quando disponível, e confira os links relativos para referências. Teste o fluxo da skill com cenários representativos antes de publicar alterações. Não faça escritas reais em serviços externos durante simulações.

## Publicação e contribuição

Depois que uma alteração for revisada e enviada ao repositório remoto, a skill pode ser instalada pelo identificador GitHub do projeto:

```bash
npx skills add luiisprotasio/scrum-master --skill writing-cards -a codex
```

Contribuições devem ser feitas em uma branch e enviadas por pull request, conforme o `README.md`. Confirme que só os arquivos pretendidos foram incluídos e que a skill instalada corresponde à versão revisada.

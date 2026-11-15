# Modelo genérico de card

Use este modelo como estrutura para criar ou revisar um card de produto ou trabalho. Adapte os títulos à ferramenta e às convenções da equipe. Mantenha somente as seções que ajudam a esclarecer o trabalho.

## Orientações para preencher

- Baseie o card nas informações fornecidas e nas fontes consultadas. Não invente IDs, decisões, prioridades acordadas, estimativas da equipe, responsáveis, contratos ou detalhes técnicos. O agente pode propor pontos Fibonacci preliminares na conversa; registre-os e sua justificativa exclusivamente no índice local obrigatório da coleção, nunca neste card.
- Preserve nomes, termos e convenções que já existam no projeto. Se uma informação necessária estiver ausente, registre-a como pendência ou faça uma pergunta quando ela impedir a definição do escopo.
- Diferencie fatos confirmados, propostas e decisões pendentes. Cite a fonte de decisões ou requisitos importantes quando disponível.
- Escreva resultados e comportamentos observáveis. Evite prescrever implementação sem necessidade ou acordo explícito.
- Para cards de sprint, siga o padrão `S{N}-{SIGLA}-{NN} [{TIPO}] [{ÁREAS}] {Resumo}`: `N` é o número da sprint; `SIGLA` identifica o escopo; `NN` é a sequência de dois dígitos; todo título deve incluir um tipo. Use a taxonomia do time ou, sem taxonomia, `[FEATURE]` para capacidade visível ao usuário, `[BUG]` para correção de defeito, `[TASK]` para descoberta/trabalho interno e `[CHORE]` para manutenção. `ÁREAS` é opcional (`BE`, `FE`, `ARCH`, separadas por `/`). Preserve IDs existentes. Não invente número da sprint.
- Mantenha estimativas Fibonacci fora dos cards individuais; registre a proposta e sua justificativa somente no índice local obrigatório da coleção.
- Inclua critérios de aceite verificáveis. Use cenários quando eles esclarecerem condições e resultados que os critérios não deixam óbvios; evite duplicar conteúdo.
- Remova instruções entre colchetes e seções opcionais que não se aplicam. Não preencha uma seção apenas para manter o formato.
- Registre alterações realizadas durante a execução somente depois que forem conhecidas.

---

**Título de sprint:** `S{N}-{SIGLA}-{NN} [TIPO] [BE/FE/ARCH] {Resumo da tarefa}`
**Título de backlog:** `BKL-{SIGLA}-{NN} [TIPO] [BE/FE/ARCH] {Resumo da tarefa}`
**Status de revisão:** [Pronto para publicação / Falta informação / Falta detalhamento / Conflito entre fontes / Dependência bloqueante / Revisar escopo]  
**Pontos de atenção:** [problemas específicos ou Nenhum]  
**Impacto na publicação:** [Pronto / Bloqueado]  
**Próxima ação:** [pergunta, decisão, ação ou Nenhuma]  
**Tipo/categoria:** [valor conforme a taxonomia da equipe, se usada]
**Prioridade:** [valor ou critério acordado, se definido]
**Responsável:** [pessoa ou papel, se definido]
**Origem/rastreabilidade:** [pedido, objetivo, decisão ou artefato de origem, se conhecido]

**Depende de:**
- [ID ou condição] — [como e em que etapa afeta este card].

**Desbloqueia:**
- [resultado ou trabalho que este card viabiliza, se aplicável].

**Cards relacionados:**
- [ID] — [relação com este card].

## 1. Contexto e resultado esperado

**Situação ou necessidade:**
[Problema, oportunidade ou necessidade observável e o contexto necessário para entendê-la.]

**Resultado esperado:**
[Mudança ou valor que deverá existir quando o trabalho estiver concluído.]

**Escopo incluído:**
- [Capacidade, comportamento ou resultado coberto por este card.]

**Fora de escopo:**
- [Trabalho próximo que poderia ser confundido com este card, mas não faz parte dele.]

## 2. Requisitos e regras

Organize por fluxo, usuário, regra ou aspecto do produto. Inclua apenas detalhes relevantes para definir o resultado.

### [Fluxo ou aspecto]

- [Quem pode ou deve fazer o quê, em qual condição.]
- [Resposta ou comportamento esperado do produto.]
- [Validação, regra de negócio ou restrição aplicável.]

**Exceções e estados relevantes:**
- [Condição de erro, ausência de dados, indisponibilidade ou limite] — [comportamento esperado].

## 3. Dependências, decisões e referências

**Dependências conhecidas:**
- [ID, recurso ou condição] — [relação com o trabalho e impacto no desenvolvimento ou aceite].

**Decisões pendentes:**
- [Questão] — **responsável pela decisão:** [se conhecido] — **impacto:** [o que depende dessa decisão].

**Referências:**
- [Link, documento, card, tela, API ou artefato] — [informação que a referência sustenta].

## 4. Critérios de aceite

- [ ] [Condição verificável para o resultado principal.]
- [ ] [Condição verificável para uma regra ou fluxo relevante.]
- [ ] [Condição verificável para uma exceção importante, se aplicável.]

## 5. Cenários (opcional)

Inclua cenários quando ajudarem a esclarecer comportamentos condicionais ou resultados distintos. Use termos observáveis e não replique critérios de aceite sem acrescentar contexto.

**Cenário — [nome curto]**

- **Dado** [contexto e condições iniciais],
- **Quando** [ação ou evento],
- **Então** [resultado observável].

## 6. Notas de execução (preencher durante ou após o trabalho)

**Desvios em relação ao escopo aprovado:**
- [Alteração] — **motivo:** [razão] — **impacto:** [efeito em requisitos, critérios ou dependências].

**Entrega:**
- [Resultado concluído, limitação conhecida ou referência à implementação, se aplicável].

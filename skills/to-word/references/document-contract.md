# Contrato de entrada e saída

## Entrada Markdown

Use um bloco YAML no início do arquivo para fornecer os campos do documento:

```yaml
---
project_name: Nome do projeto
date: 2026-11-23
---
```

`project_name` é obrigatório. `date` é opcional. O corpo Markdown começa após o bloco YAML e controla o texto, a ordem das seções e a hierarquia dos títulos.

Recursos cobertos: títulos, parágrafos, ênfase, listas, tabelas, links e imagens locais. Imagens locais são resolvidas em relação ao arquivo Markdown. Se a fonte depender de um recurso não coberto ou externo, confirme a alternativa com o usuário antes de simplificar ou remover o conteúdo.

## Modelo DOCX

O modelo padrão é `assets/blue.docx`. Um modelo alternativo pode ser informado pelo usuário. Ele precisa conter o campo `{{project_name}}` e o ponto de inserção de parágrafo `{{p body}}`; pode conter `{{date}}`.

Preserve estilos, cabeçalho, rodapé, imagens e outros elementos fixos do modelo. Se um modelo alternativo não tiver os campos ou o ponto de inserção esperados, não remova nem substitua conteúdo por suposição; mostre o que falta e peça o mapeamento necessário.

No modelo `blue`, títulos Markdown de nível 1 ficam centralizados, em teal e negrito, com 24 pt. Títulos dos níveis 2 a 9 usam 13 pt, negrito, cinza do texto (`#666666`) e alinhamento à esquerda. O nível 2 tem recuo de uma parada de tabulação (0,5″); os níveis 3 a 9 não têm recuo adicional.

## Saída

Salve o DOCX em `.scrum-master/` na raiz do projeto, usando o mesmo nome-base do Markdown. Se esse caminho já existir, não o sobrescreva: use um nome livre com sufixo numérico. Um destino explícito que já exista deve ser recusado até o usuário escolher outro caminho.

Nunca sobrescreva o Markdown, o modelo, o documento fornecido pelo usuário ou qualquer arquivo de origem. Quebras de página podem mudar com o tamanho do conteúdo, mesmo quando o modelo mantém sua apresentação.

## Dependências

O renderizador requer Python 3.10 ou superior, Pandoc, PyYAML, `python-docx` e `docxtpl[subdoc]`. Se algum estiver ausente, informe qual e pare; não instale dependências sem pedido do usuário. LibreOffice pode ser usado para visualizar o resultado, mas não é necessário para a conversão.

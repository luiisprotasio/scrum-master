---
name: to-word
description: Converta documentos Markdown em DOCX usando o modelo padrão blue ou um modelo Word fornecido pelo usuário, preservando a apresentação do modelo.
---

# Markdown para Word

Transforme o conteúdo de um arquivo Markdown em um novo DOCX. O Markdown define o texto e a hierarquia das seções; o DOCX escolhido define a apresentação.

## Fluxo

1. Leia o Markdown e confira o bloco YAML, os recursos usados e o destino de saída.
2. Use `assets/blue.docx` como modelo padrão ou o DOCX alternativo indicado pelo usuário.
3. Peça o nome do projeto somente se estiver ausente. Não invente esse valor nem a data.
4. Verifique Python 3.10 ou superior, Pandoc, PyYAML, `python-docx` e `docxtpl[subdoc]`. Se faltar uma dependência, informe qual e pare sem instalá-la.
5. Salve o DOCX em `.scrum-master/` na raiz do projeto. Crie a pasta se ela não existir. Use o mesmo nome-base do Markdown; se já houver um arquivo com esse nome, escolha o próximo sufixo numérico livre. Gere o arquivo com `python3 scripts/render_docx.py INPUT.md OUTPUT.docx [--template TEMPLATE.docx]`, seguindo [o contrato de documento](references/document-contract.md).
6. Preserve as fontes e o modelo. Nunca sobrescreva o Markdown, o DOCX-modelo nem um arquivo de saída existente. Se o usuário escolher um destino existente, peça outro caminho.
7. Quando houver um visualizador DOCX disponível, confira a capa, os títulos, tabelas, imagens, cabeçalho e rodapé. Avise que a paginação pode mudar com a extensão do conteúdo.

## Modelo alternativo

O modelo padrão `assets/blue.docx` está incluído nesta skill. O modelo alternativo deve seguir os campos e o ponto de inserção descritos no contrato. Se o modelo escolhido não seguir esse formato, não o altere silenciosamente: explique a incompatibilidade e peça orientação.

# Guia de Documentacao Tecnica

## README

O README e o primeiro arquivo que qualquer pessoa le ao acessar um repositorio. Deve conter:

- Nome e descricao do projeto.
- Tecnologias utilizadas.
- Pre-requisitos e como instalar.
- Como executar localmente.
- Como executar os testes.
- Estrutura de pastas.
- Fluxo de desenvolvimento.

Use o template em `materiais/templates/template-readme-projeto.md`.

## PRD (Product Requirements Document)

O PRD documenta o que o produto deve fazer e por que. Deve conter:

- Visao geral do produto.
- Problema que resolve.
- Objetivo.
- Publico-alvo.
- Funcionalidades principais.
- Requisitos funcionais e nao funcionais.
- Regras de negocio.
- Criterios de sucesso.
- O que esta fora do escopo.

Use o template em `materiais/templates/template-prd.md`.

## CONTRIBUTING

O CONTRIBUTING.md orienta colaboradores sobre como contribuir com o projeto. Deve conter:

- Como configurar o ambiente de desenvolvimento.
- Convencoes de branch e commit.
- Como abrir Issues e Pull Requests.
- Criterios para aprovacao de PRs.

## Documentacao de API

Documente cada endpoint com:

- Metodo HTTP e URL.
- Descricao do que faz.
- Parametros de entrada (query, body, headers).
- Estrutura da resposta.
- Codigos de status possiveis.
- Exemplos de requisicao e resposta.

## Registro de decisoes

Documente decisoes tecnicas importantes em um arquivo `docs/decisoes.md` ou em comentarios no PRD. Para cada decisao, registre:

- O que foi decidido.
- Por que foi decidido assim.
- Alternativas consideradas.
- Consequencias da decisao.

## Registro de prompts

Documente os prompts utilizados em `docs/prompts.md`. Para cada prompt, registre:

- O objetivo do prompt.
- O prompt enviado.
- O resultado obtido.
- O que foi aceito, ajustado ou descartado.

## Evidencias de entrega

Inclua evidencias de execucao nas entregas:

- Prints do terminal com testes passando.
- Prints da interface funcionando.
- Links para Issues e Pull Requests.
- Logs de execucao relevantes.

Salve evidencias em uma pasta `evidencias/` ou `docs/evidencias/` no repositorio.

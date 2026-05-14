# Mini-Projeto

O mini-projeto e o trabalho avaliativo do modulo. Os alunos devem desenvolver um projeto de software aplicando as praticas aprendidas ao longo das semanas.

## Objetivo

Demonstrar a capacidade de usar IA como ferramenta de apoio ao desenvolvimento de software, produzindo artefatos de qualidade: documentacao, codigo, testes e rastreabilidade do processo.

## O que os alunos devem desenvolver

- Um produto de software com pelo menos tres funcionalidades implementadas.
- Documentacao tecnica completa (PRD, README, User Stories).
- Testes automatizados.
- Repositorio organizado com GitHub Flow (Issues, branches, Pull Requests).
- Registro dos prompts utilizados.
- Apresentacao tecnica final.

## Relacao com as semanas do curso

| Semana | Contribuicao para o mini-projeto |
|--------|----------------------------------|
| Semana 02 | Engenharia de contexto e prompts para gerar artefatos |
| Semana 05 | User Stories, backlog, GitHub Issues, branches e PRs |
| Semana 06 | Testes automatizados |
| Semana 07 | Documentacao tecnica e automacao |

## Estrutura esperada do repositorio

```
seu-projeto/
├── docs/
│   ├── PRD.md
│   ├── prompts.md
│   ├── user-stories/
│   └── diagramas/
├── src/                # codigo fonte
├── tests/              # testes automatizados
├── CONTRIBUTING.md
└── README.md
```

## Artefatos esperados

- `README.md` completo.
- `docs/PRD.md` com visao geral, requisitos e User Stories.
- User Stories com criterios de aceitacao em BDD.
- Diagramas (UML ou C4).
- GitHub Issues derivadas das User Stories.
- Branches e Pull Requests seguindo convencao.
- Testes automatizados com evidencias de execucao.
- `docs/prompts.md` com registro dos prompts utilizados.

## Como registrar prompts

Crie o arquivo `docs/prompts.md` no repositorio do projeto. Para cada prompt, registre:

- Objetivo do prompt.
- Prompt enviado.
- Resultado obtido.
- O que foi aceito, ajustado ou descartado.

## Como usar GitHub Issues

- Crie uma Issue para cada User Story ou tarefa relevante.
- Use o template de Issue disponivel em `materiais/templates/template-issue.md`.
- Adicione labels para organizar por tipo e semana.

## Como usar branches

- Crie uma branch para cada Issue: `feat/issue-{numero}-{descricao}`.
- Nunca commite diretamente na `main`.
- Delete branches apos o merge.

## Como abrir Pull Requests

- Use o template em `materiais/templates/template-pull-request.md`.
- Referencie a Issue com `Closes #numero`.
- Inclua instrucoes de como testar.

## Como registrar evidencias

- Salve prints do terminal com testes passando.
- Salve prints da interface funcionando.
- Inclua links para Issues e Pull Requests no relatorio de entrega.

## Como preparar a apresentacao final

A apresentacao deve cobrir:

1. Problema que o produto resolve.
2. Solucao desenvolvida.
3. Arquitetura e tecnologias.
4. Funcionalidades implementadas.
5. Como a IA foi utilizada.
6. Testes e evidencias.
7. Decisoes tecnicas tomadas.
8. Aprendizados.

## Niveis de entrega

Os criterios de avaliacao estao organizados em tres niveis em `criterios-avaliacao.md`. Consulte tambem o arquivo `Avaliacao MINI PROJETO.pdf` para a rubrica completa.

# Atividade - Semana 05

## Objetivo

Aplicar o fluxo de engenharia de software assistida por IA: criar User Stories, organizar o backlog, configurar o repositorio e usar GitHub Issues, branches e Pull Requests.

## O que o aluno deve produzir

- Pelo menos 3 User Stories no formato Como / Quero / Para.
- Criterios de aceitacao em BDD para cada User Story.
- Checklist tecnico para cada User Story.
- Issues criadas no GitHub correspondendo as User Stories.
- Branches criadas a partir das Issues.
- Pelo menos 1 Pull Request aberto com descricao adequada.
- Registro dos prompts utilizados.

## Como organizar a entrega

```
atividades/semana-05/
└── seu-nome/
    ├── user-stories.md     # User Stories com criterios de aceitacao
    ├── prompts-usados.md   # Prompts utilizados para gerar os artefatos
    └── README.md           # Descricao do que foi feito e links para Issues/PRs
```

## Como registrar os prompts usados

Crie um arquivo `prompts-usados.md` com:

- O prompt enviado para gerar cada artefato.
- O resultado obtido.
- O que foi aceito, ajustado ou descartado.

## Como versionar no Git

```bash
git checkout -b feat/atividade-semana-05-seu-nome
git add atividades/semana-05/seu-nome/
git commit -m "feat: adiciona atividade semana 05 - seu-nome"
git push origin feat/atividade-semana-05-seu-nome
```

Abra um Pull Request apos o push.

## Criterios minimos de qualidade

- User Stories no formato correto (Como / Quero / Para).
- Criterios de aceitacao em BDD (Given / When / Then).
- Issues criadas no GitHub com descricao adequada.
- Pelo menos uma branch criada a partir de uma Issue.
- Pelo menos um Pull Request aberto.
- Prompts documentados.
- Commits com mensagens descritivas.

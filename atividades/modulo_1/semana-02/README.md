# Atividade - Semana 02

## Objetivo

Praticar engenharia de contexto e prompts aplicados ao desenvolvimento de software.

## O que o aluno deve produzir

- Um conjunto de prompts estruturados para um caso de uso de sua escolha.
- Comparacao entre um prompt simples e um prompt com contexto adequado.
- Registro das respostas obtidas e analise critica dos resultados.

## Como organizar a entrega

```
atividades/semana-02/
└── seu-nome/
    ├── prompts.md          # Prompts criados e resultados obtidos
    ├── analise.md          # Analise critica das respostas da IA
    └── README.md           # Descricao do que foi feito
```

## Como registrar os prompts usados

Crie um arquivo `prompts.md` com a seguinte estrutura para cada prompt:

```
## Prompt 1

**Contexto:** [descreva o contexto fornecido]
**Objetivo:** [o que voce queria obter]
**Prompt enviado:**
[cole o prompt aqui]

**Resultado obtido:**
[cole ou resuma a resposta]

**Avaliacao:** [o que funcionou, o que nao funcionou, o que ajustou]
```

## Como versionar no Git

```bash
git checkout -b feat/atividade-semana-02-seu-nome
git add atividades/semana-02/seu-nome/
git commit -m "feat: adiciona atividade semana 02 - seu-nome"
git push origin feat/atividade-semana-02-seu-nome
```

Abra um Pull Request apos o push.

## Criterios minimos de qualidade

- Pelo menos dois prompts documentados com contexto, objetivo e resultado.
- Analise critica presente: o que a IA acertou, errou ou precisou de ajuste.
- Estrutura de pastas organizada.
- Commits com mensagens descritivas.

# Prompt: Gerar Issues para GitHub

## Quando usar

Para gerar o conteudo de Issues no formato padrao do projeto a partir de User Stories ou de uma lista de funcionalidades.

## Prompt

```
Contexto:
Estou criando Issues no GitHub para o projeto Shop4u.
Cada Issue deve corresponder a uma User Story do backlog.

Objetivo:
Gere o conteudo de Issues no formato abaixo para cada User Story listada.

Entrada esperada:
User Stories:
1. Como usuario, quero fazer login com email e senha, para acessar minha conta.
2. Como usuario, quero buscar produtos por nome, para encontrar o que preciso.
3. Como usuario, quero adicionar produtos ao carrinho, para organizar minha compra.

Restricoes:
- Para cada User Story, gere: titulo da Issue, descricao com a User Story, criterios de aceitacao em BDD e checklist tecnico.
- Use o formato de titulo: [US-0X] Descricao curta.
- Criterios de aceitacao no formato: Dado que / Quando / Entao.
- Checklist tecnico com tarefas de implementacao e testes.
- Nao invente criterios que nao derivem da User Story.
- Nao use emojis.

Formato de saida:
Para cada Issue, gere um bloco Markdown separado pronto para ser usado com --body-file no GitHub CLI.
```

## Como criar a Issue com o conteudo gerado

Salve o conteudo de cada Issue em um arquivo separado e use:

```bash
gh issue create \
  --title "[US-01] Login com email e senha" \
  --body-file issue-us-01.md \
  --label "user-story"
```

## Revisao humana necessaria

- Revise os criterios de aceitacao antes de criar as Issues.
- Confirme o checklist tecnico com a stack real do projeto.
- Ajuste os titulos para seguir a convencao do repositorio.
- Nao crie Issues em repositorios de producao sem autorizacao.

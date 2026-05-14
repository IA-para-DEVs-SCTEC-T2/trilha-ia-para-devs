# Gerar Issues com GitHub CLI

## Objetivo

Criar Issues no GitHub a partir de User Stories usando o GitHub CLI (`gh`), automatizando a criacao do backlog no repositorio.

## Pre-requisitos

- GitHub CLI instalado: https://cli.github.com
- Autenticado: `gh auth login`
- Repositorio configurado como remoto

## Quando usar

- Para criar multiplas Issues de uma vez a partir de um backlog.
- Para padronizar o formato das Issues do projeto.
- Para automatizar a criacao de Issues em scripts de setup do projeto.

## Quando evitar

- Quando as Issues precisam de revisao antes de serem publicadas.
- Quando o repositorio e de producao e Issues nao devem ser criadas automaticamente.

## Fluxo passo a passo

1. Crie um arquivo Markdown com o conteudo da Issue.
2. Use `gh issue create` com `--body-file` para criar a Issue.
3. Verifique a Issue criada no GitHub.
4. Ajuste o conteudo se necessario.

## Exemplo: criar Issue com arquivo

Crie o arquivo `issue-body.md`:

```markdown
## User Story

Como usuario do Shop4u,
quero fazer login com email e senha,
para acessar minha conta e historico de pedidos.

## Criterios de aceitacao

- Dado que o usuario esta na tela de login
  Quando ele informa email e senha validos e clica em Entrar
  Entao ele e redirecionado para a tela inicial autenticado

- Dado que o usuario informa senha incorreta
  Quando ele clica em Entrar
  Entao uma mensagem de erro e exibida

## Checklist tecnico

- [ ] Endpoint POST /auth/login implementado
- [ ] Validacao de campos no frontend
- [ ] Tratamento de erro 401
- [ ] Teste unitario para a funcao de autenticacao
```

Crie a Issue:

```bash
gh issue create \
  --title "[US-01] Login com email e senha" \
  --body-file issue-body.md \
  --label "user-story"
```

## Exemplo: criar Issue com heredoc

```bash
gh issue create \
  --title "[US-02] Busca de produtos por nome" \
  --body "$(cat <<'EOF'
## User Story

Como usuario do Shop4u,
quero buscar produtos por nome,
para encontrar rapidamente o que preciso.

## Criterios de aceitacao

- Dado que o usuario esta na tela de busca
  Quando ele digita um termo e pressiona buscar
  Entao os produtos correspondentes sao exibidos

## Checklist tecnico

- [ ] Endpoint GET /products?q={termo} implementado
- [ ] Campo de busca no frontend
- [ ] Tratamento de resultado vazio
EOF
)"
```

## Cuidados

- Revise o conteudo antes de criar a Issue.
- Nao crie Issues em repositorios de producao sem autorizacao.
- Use labels para organizar as Issues por tipo.
- Verifique se o repositorio correto esta configurado como remoto.

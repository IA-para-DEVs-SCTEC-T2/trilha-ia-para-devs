# Guia de Git e GitHub

## O que e Git

Git e um sistema de controle de versao distribuido. Ele registra o historico de alteracoes de um projeto, permitindo voltar a versoes anteriores, trabalhar em paralelo com outras pessoas e rastrear quem fez o que e quando.

## O que e GitHub

GitHub e uma plataforma de hospedagem de repositorios Git. Alem de armazenar o codigo, oferece ferramentas para colaboracao: Issues, Pull Requests, Projects, Actions e revisao de codigo.

## Comandos basicos

```bash
# Clonar um repositorio
git clone https://github.com/usuario/repositorio.git

# Ver o estado atual do repositorio
git status

# Adicionar arquivos ao stage
git add nome-do-arquivo
git add .                    # adiciona tudo

# Fazer commit
git commit -m "feat: descricao do que foi feito"

# Enviar para o remoto
git push origin nome-da-branch

# Atualizar o repositorio local
git pull origin main

# Buscar atualizacoes sem aplicar
git fetch origin

# Criar e mudar para nova branch
git checkout -b feat/issue-1-descricao

# Mudar de branch
git checkout nome-da-branch

# Listar branches
git branch -a

# Remover branch local apos merge
git branch -d nome-da-branch

# Remover branch remota
git push origin --delete nome-da-branch
```

## Convencoes de branch

| Prefixo | Quando usar | Exemplo |
|---------|-------------|---------|
| `feat/` | Nova funcionalidade | `feat/issue-1-tela-login` |
| `fix/` | Correcao de bug | `fix/issue-3-validacao-senha` |
| `docs/` | Documentacao | `docs/issue-5-readme` |
| `test/` | Testes | `test/issue-7-testes-frete` |
| `refactor/` | Refatoracao | `refactor/issue-9-servico-auth` |
| `chore/` | Manutencao | `chore/atualizar-dependencias` |

## Convencoes de commit

| Tipo | Quando usar |
|------|-------------|
| `feat:` | Nova funcionalidade |
| `fix:` | Correcao de bug |
| `docs:` | Documentacao |
| `test:` | Testes |
| `refactor:` | Refatoracao sem mudanca de comportamento |
| `chore:` | Manutencao, dependencias, configs |

Formato: `tipo: descricao curta no imperativo`

Exemplos:
```
feat: adiciona tela de login
fix: corrige calculo de frete com peso zero
docs: atualiza README com instrucoes de instalacao
test: adiciona testes unitarios para desconto
```

## Abrir Pull Request via GitHub CLI

```bash
gh pr create \
  --title "feat: adiciona tela de login (#1)" \
  --body-file pr-body.md \
  --base main
```

## Fluxo resumido

```
git checkout main
git pull origin main
git checkout -b feat/issue-1-descricao
# ... desenvolve e faz commits ...
git push origin feat/issue-1-descricao
gh pr create ...
# apos merge:
git checkout main
git pull origin main
git branch -d feat/issue-1-descricao
```

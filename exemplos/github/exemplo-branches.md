# Convencoes de Branches

Referencia para nomear branches de forma padronizada e consistente.

## Formato

```
tipo/descricao-curta
tipo/issue-{numero}-descricao-curta
```

## Prefixos

| Prefixo | Quando usar |
|---------|-------------|
| `feat/` | Nova funcionalidade |
| `fix/` | Correcao de bug |
| `docs/` | Documentacao |
| `test/` | Testes |
| `refactor/` | Refatoracao |
| `chore/` | Manutencao, dependencias, configs |

## Regras

- Use letras minusculas.
- Separe palavras com hifen (`-`), nao underscore ou espaco.
- Seja descritivo mas conciso.
- Inclua o numero da Issue quando houver.
- Evite nomes genericos como `fix/bug` ou `feat/nova-feature`.

## Exemplos corretos

```
feat/issue-1-tela-login
feat/issue-2-busca-produtos
fix/issue-5-validacao-senha-vazia
docs/issue-8-readme-modulo-busca
test/issue-10-testes-calculo-frete
refactor/issue-12-extrair-servico-auth
chore/atualizar-dependencias
```

## Exemplos incorretos

```
# Sem prefixo
login
nova-feature

# Com espacos ou maiusculas
feat/Tela Login
feat/tela_login

# Muito generico
fix/bug
feat/feature
```

## Criar e publicar uma branch

```bash
# Criar e mudar para a branch
git checkout -b feat/issue-1-tela-login

# Publicar no remoto
git push origin feat/issue-1-tela-login
```

## Remover branch apos merge

```bash
# Remover local
git branch -d feat/issue-1-tela-login

# Remover remota
git push origin --delete feat/issue-1-tela-login
```

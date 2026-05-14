# GitHub Flow

Fluxo basico de desenvolvimento com GitHub usado no modulo.

## Visao geral

```
main (sempre estavel)
  |
  +-- feat/issue-1-login
  |       |
  |       +-- commits
  |       |
  |       +-- Pull Request
  |               |
  |               +-- Revisao
  |               |
  |               +-- Merge na main
  |
  +-- feat/issue-2-busca
          |
          ...
```

## Passo a passo

### 1. Escolher uma Issue

Acesse as Issues abertas no repositorio e escolha uma para trabalhar.

```bash
gh issue list
```

### 2. Criar a branch

Crie uma branch a partir da `main` com o nome seguindo a convencao.

```bash
git checkout main
git pull origin main
git checkout -b feat/issue-1-login
```

### 3. Desenvolver e fazer commits

Faca commits pequenos e frequentes com mensagens descritivas.

```bash
git add src/screens/LoginScreen.js
git commit -m "feat: adiciona estrutura da tela de login"

git add src/services/auth.js
git commit -m "feat: adiciona servico de autenticacao"

git add tests/auth.test.js
git commit -m "test: adiciona testes para o servico de autenticacao"
```

### 4. Enviar a branch para o remoto

```bash
git push origin feat/issue-1-login
```

### 5. Abrir o Pull Request

```bash
gh pr create \
  --title "feat: adiciona tela de login (#1)" \
  --body-file pr-body.md \
  --base main
```

### 6. Revisao e aprovacao

- O revisor lê o PR, executa os testes e deixa comentarios.
- O autor responde aos comentarios e faz ajustes se necessario.
- Apos aprovacao, o merge e realizado.

### 7. Merge e limpeza

```bash
git checkout main
git pull origin main
git branch -d feat/issue-1-login
git push origin --delete feat/issue-1-login
```

## Regras do fluxo

- Nunca commite diretamente na `main`.
- Sempre crie uma branch para cada Issue ou funcionalidade.
- Abra um PR antes de fazer merge.
- A `main` deve estar sempre em estado funcional.
- Delete branches apos o merge.

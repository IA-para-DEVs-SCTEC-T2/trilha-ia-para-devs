# Exemplo de Casos de Teste

Estrutura de casos de teste para documentar cenarios de validacao.

## Estrutura de um caso de teste

| Campo | Descricao |
|-------|-----------|
| ID | Identificador unico (ex: CT-01) |
| Funcionalidade | Nome da funcionalidade testada |
| Cenario | Descricao do cenario |
| Pre-condicao | Estado necessario antes de executar |
| Passos | Sequencia de acoes |
| Resultado esperado | O que deve acontecer |
| Resultado obtido | O que aconteceu (preencher apos execucao) |
| Status | Passou / Falhou / Nao executado |

## Exemplo: Login

### CT-01: Login com credenciais validas

| Campo | Valor |
|-------|-------|
| Funcionalidade | Login |
| Cenario | Positivo |
| Pre-condicao | Usuario cadastrado com email `usuario@shop4u.com` e senha `senha123` |

**Passos:**
1. Acessar a tela de login
2. Informar email `usuario@shop4u.com`
3. Informar senha `senha123`
4. Clicar em Entrar

**Resultado esperado:** Usuario redirecionado para a tela inicial autenticado.

**Status:** [ ] Passou / [ ] Falhou

---

### CT-02: Login com senha incorreta

| Campo | Valor |
|-------|-------|
| Funcionalidade | Login |
| Cenario | Negativo |
| Pre-condicao | Usuario cadastrado |

**Passos:**
1. Acessar a tela de login
2. Informar email valido
3. Informar senha incorreta
4. Clicar em Entrar

**Resultado esperado:** Mensagem de erro exibida. Usuario permanece na tela de login.

**Status:** [ ] Passou / [ ] Falhou

---

### CT-03: Login com email vazio (valor limite)

| Campo | Valor |
|-------|-------|
| Funcionalidade | Login |
| Cenario | Valor limite |
| Pre-condicao | Nenhuma |

**Passos:**
1. Acessar a tela de login
2. Deixar o campo de email vazio
3. Clicar em Entrar

**Resultado esperado:** Mensagem de validacao exibida abaixo do campo de email.

**Status:** [ ] Passou / [ ] Falhou

---

### CT-04: Login com email sem formato valido (edge case)

| Campo | Valor |
|-------|-------|
| Funcionalidade | Login |
| Cenario | Edge case |
| Pre-condicao | Nenhuma |

**Passos:**
1. Acessar a tela de login
2. Informar `nao-e-um-email` no campo de email
3. Clicar em Entrar

**Resultado esperado:** Mensagem de validacao de formato de email exibida.

**Status:** [ ] Passou / [ ] Falhou

# Exemplo de Issue

Modelo de Issue com User Story, criterios de aceitacao em BDD e checklist tecnico.

## Estrutura

```markdown
## User Story

Como [perfil do usuario],
quero [acao que deseja realizar],
para [beneficio ou objetivo].

## Criterios de aceitacao

- Dado que [contexto inicial]
  Quando [acao do usuario]
  Entao [resultado esperado]

- Dado que [outro contexto]
  Quando [outra acao]
  Entao [outro resultado]

## Checklist tecnico

- [ ] [Tarefa tecnica 1]
- [ ] [Tarefa tecnica 2]
- [ ] Testes adicionados
- [ ] Documentacao atualizada
```

## Exemplo preenchido: Login

**Titulo:** [US-01] Login com email e senha

```markdown
## User Story

Como usuario do Shop4u,
quero fazer login com meu email e senha,
para acessar minha conta e historico de pedidos.

## Criterios de aceitacao

- Dado que o usuario esta na tela de login
  Quando ele informa email e senha validos e clica em Entrar
  Entao ele e redirecionado para a tela inicial autenticado

- Dado que o usuario informa senha incorreta
  Quando ele clica em Entrar
  Entao uma mensagem de erro "Credenciais invalidas" e exibida

- Dado que o usuario deixa o campo de email vazio
  Quando ele clica em Entrar
  Entao uma mensagem de validacao e exibida abaixo do campo

## Checklist tecnico

- [ ] Endpoint POST /auth/login implementado
- [ ] Validacao de campos no frontend (email e senha obrigatorios)
- [ ] Tratamento de erro 401 com mensagem adequada
- [ ] Token JWT armazenado de forma segura
- [ ] Teste unitario para a funcao de autenticacao
- [ ] Teste E2E para o fluxo de login
```

## Exemplo preenchido: Busca de produtos

**Titulo:** [US-02] Busca de produtos por nome

```markdown
## User Story

Como usuario do Shop4u,
quero buscar produtos por nome,
para encontrar rapidamente o que preciso comprar.

## Criterios de aceitacao

- Dado que o usuario esta na tela principal
  Quando ele digita um termo no campo de busca e pressiona buscar
  Entao os produtos com nome correspondente sao exibidos

- Dado que nenhum produto corresponde ao termo buscado
  Quando a busca e realizada
  Entao uma mensagem "Nenhum produto encontrado" e exibida

- Dado que o campo de busca esta vazio
  Quando o usuario pressiona buscar
  Entao todos os produtos sao exibidos

## Checklist tecnico

- [ ] Endpoint GET /products?q={termo} implementado
- [ ] Busca case-insensitive
- [ ] Campo de busca no frontend com debounce
- [ ] Tratamento de resultado vazio
- [ ] Teste unitario para a funcao de busca
```

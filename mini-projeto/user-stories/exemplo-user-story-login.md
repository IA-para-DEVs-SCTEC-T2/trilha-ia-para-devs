# [US-01] Login com email e senha

## User Story

Como usuario do Shop4u,
quero fazer login com meu email e senha,
para acessar minha conta e historico de pedidos.

## Criterios de aceitacao

Cenario 1: Login com credenciais validas
Dado que o usuario esta na tela de login
Quando ele informa email e senha validos e clica em Entrar
Entao ele e redirecionado para a tela inicial autenticado

Cenario 2: Login com senha incorreta
Dado que o usuario esta na tela de login
Quando ele informa uma senha incorreta e clica em Entrar
Entao uma mensagem de erro "Credenciais invalidas" e exibida

Cenario 3: Campo de email vazio
Dado que o usuario esta na tela de login
Quando ele deixa o campo de email vazio e clica em Entrar
Entao uma mensagem de validacao e exibida abaixo do campo

## Checklist tecnico

- [ ] Endpoint POST /auth/login implementado
- [ ] Validacao de campos obrigatorios no frontend
- [ ] Tratamento de erro 401 com mensagem adequada
- [ ] Token armazenado de forma segura
- [ ] Teste unitario para a funcao de autenticacao
- [ ] Teste E2E para o fluxo de login

## Evidencias esperadas

- Print da tela de login funcionando
- Print do terminal com testes passando
- Link para o Pull Request

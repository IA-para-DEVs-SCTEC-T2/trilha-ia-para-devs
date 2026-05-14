# [US-04] Finalizar compra

## User Story

Como usuario autenticado do Shop4u,
quero finalizar minha compra informando endereco e pagamento,
para receber os produtos que adicionei ao carrinho.

## Criterios de aceitacao

Cenario 1: Checkout com dados validos
Dado que o usuario tem itens no carrinho e esta autenticado
Quando ele informa endereco e dados de pagamento validos e confirma o pedido
Entao o pedido e criado e uma confirmacao e exibida com o numero do pedido

Cenario 2: Pagamento recusado
Dado que o usuario esta na tela de checkout
Quando ele informa dados de pagamento invalidos e confirma
Entao uma mensagem de erro e exibida e o pedido nao e criado

Cenario 3: Carrinho vazio
Dado que o usuario nao tem itens no carrinho
Quando ele tenta acessar o checkout
Entao ele e redirecionado para a tela de produtos com uma mensagem informativa

## Checklist tecnico

- [ ] Endpoint POST /orders implementado
- [ ] Integracao com servico de pagamento
- [ ] Validacao de campos de endereco e pagamento
- [ ] Tratamento de erro de pagamento recusado
- [ ] Email de confirmacao enviado apos pedido criado
- [ ] Teste unitario para a regra de carrinho vazio

## Evidencias esperadas

- Print da tela de confirmacao do pedido
- Print do terminal com testes passando
- Link para o Pull Request

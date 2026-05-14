# [US-03] Adicionar produto ao carrinho

## User Story

Como usuario autenticado do Shop4u,
quero adicionar produtos ao carrinho,
para organizar minha compra antes de finalizar o pedido.

## Criterios de aceitacao

Cenario 1: Adicionar produto disponivel
Dado que o usuario esta na tela de detalhe de um produto com estoque
Quando ele clica em "Adicionar ao carrinho"
Entao o produto e adicionado e o contador do carrinho e atualizado

Cenario 2: Produto sem estoque
Dado que o usuario esta na tela de detalhe de um produto sem estoque
Quando ele visualiza a pagina
Entao o botao "Adicionar ao carrinho" esta desabilitado

Cenario 3: Usuario nao autenticado
Dado que o usuario nao esta autenticado
Quando ele tenta adicionar um produto ao carrinho
Entao ele e redirecionado para a tela de login

## Checklist tecnico

- [ ] Endpoint POST /cart/items implementado
- [ ] Verificacao de estoque antes de adicionar
- [ ] Redirecionamento para login se nao autenticado
- [ ] Contador do carrinho atualizado no frontend
- [ ] Teste unitario para a regra de estoque

## Evidencias esperadas

- Print do carrinho com produto adicionado
- Print do botao desabilitado para produto sem estoque
- Print do terminal com testes passando

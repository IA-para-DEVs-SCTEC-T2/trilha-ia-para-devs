# [US-02] Busca de produtos por nome

## User Story

Como usuario do Shop4u,
quero buscar produtos por nome,
para encontrar rapidamente o que preciso comprar.

## Criterios de aceitacao

Cenario 1: Busca com resultado
Dado que o usuario esta na tela principal
Quando ele digita um termo no campo de busca e pressiona buscar
Entao os produtos com nome correspondente sao exibidos

Cenario 2: Busca sem resultado
Dado que o usuario busca por um termo que nao corresponde a nenhum produto
Quando a busca e realizada
Entao uma mensagem "Nenhum produto encontrado" e exibida

Cenario 3: Campo de busca vazio
Dado que o usuario nao digitou nenhum termo
Quando ele pressiona buscar
Entao todos os produtos sao exibidos

## Checklist tecnico

- [ ] Endpoint GET /products?q={termo} implementado
- [ ] Busca case-insensitive
- [ ] Campo de busca no frontend
- [ ] Tratamento de resultado vazio
- [ ] Teste unitario para a funcao de busca

## Evidencias esperadas

- Print da tela de busca com resultado
- Print da tela com mensagem de resultado vazio
- Print do terminal com testes passando

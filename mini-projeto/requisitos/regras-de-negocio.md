# Regras de Negocio

Regras que o sistema deve respeitar independentemente da funcionalidade ou tela.

## O que e uma regra de negocio

Uma regra de negocio define uma restricao ou condicao que o sistema deve sempre respeitar. Ela nao descreve uma funcionalidade, mas uma restricao sobre como o sistema se comporta.

Exemplos:
- "Um usuario nao autenticado nao pode acessar o carrinho."
- "O desconto maximo permitido e de 50%."
- "Pedidos so podem ser cancelados antes do envio."

## Tabela de regras

| ID | Regra | Descricao |
|----|-------|-----------|
| RN01 | [Nome da regra] | [Descricao da restricao] |
| RN02 | [Nome da regra] | [Descricao da restricao] |
| RN03 | [Nome da regra] | [Descricao da restricao] |

## Exemplos (Shop4u)

| ID | Regra | Descricao |
|----|-------|-----------|
| RN01 | Autenticacao obrigatoria | Apenas usuarios autenticados podem adicionar itens ao carrinho |
| RN02 | Estoque | Nao e possivel adicionar ao carrinho um produto sem estoque |
| RN03 | Quantidade minima | A quantidade minima por item no carrinho e 1 |
| RN04 | Cancelamento | Pedidos so podem ser cancelados antes do status "enviado" |

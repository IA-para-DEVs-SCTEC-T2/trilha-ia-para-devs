# Diagrama de Caso de Uso

## Finalidade

O diagrama de caso de uso mostra os atores do sistema e as funcionalidades que cada um pode acessar. E util para comunicar o escopo do produto de forma visual.

## Quando usar

- Para apresentar as funcionalidades do sistema para stakeholders nao tecnicos.
- Para identificar os perfis de usuario e o que cada um pode fazer.
- Como complemento ao PRD e as User Stories.

## Exemplo em Mermaid (Shop4u)

```mermaid
graph TD
    UA[Usuario nao autenticado]
    UL[Usuario autenticado]
    SR[Sistema de recomendacao]

    UA --> F1[Visualizar produtos]
    UA --> F2[Buscar produtos]
    UA --> F3[Fazer login / cadastro]

    UL --> F1
    UL --> F2
    UL --> F4[Adicionar ao carrinho]
    UL --> F5[Finalizar compra]
    UL --> F6[Ver recomendacoes]

    SR --> F6
```

## Como preencher para o seu projeto

Substitua os atores e funcionalidades pelos do seu projeto. Mantenha o diagrama simples: foque nos casos de uso principais.

## Justificativa

[Descreva aqui as decisoes tomadas ao definir os atores e casos de uso do seu projeto.]

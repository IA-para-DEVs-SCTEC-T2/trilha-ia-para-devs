# Fluxo de Compra

## Finalidade

Documenta o fluxo completo de uma compra, do ponto de vista do usuario e do sistema.

## Fluxo do usuario (Shop4u)

```mermaid
graph TD
    A[Usuario busca produto] --> B[Visualiza detalhe]
    B --> C{Autenticado?}
    C -->|Nao| D[Redireciona para login]
    D --> E[Login realizado]
    E --> F[Adiciona ao carrinho]
    C -->|Sim| F
    F --> G[Acessa carrinho]
    G --> H[Informa endereco]
    H --> I[Informa pagamento]
    I --> J{Pagamento aprovado?}
    J -->|Sim| K[Pedido confirmado]
    J -->|Nao| L[Exibe erro de pagamento]
    L --> I
```

## Fluxo do sistema

```mermaid
sequenceDiagram
    participant App
    participant Backend
    participant Pagamento

    App->>Backend: POST /orders
    Backend->>Pagamento: Processa pagamento
    Pagamento-->>Backend: Aprovado
    Backend-->>App: Pedido criado (201)
    App->>App: Exibe confirmacao
```

## Como adaptar para o seu projeto

Substitua os passos pelos do seu fluxo principal. Documente tambem os fluxos de erro (pagamento recusado, produto sem estoque, etc.).

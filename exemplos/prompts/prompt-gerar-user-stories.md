# Prompt: Gerar User Stories

## Quando usar

Para gerar User Stories com criterios de aceitacao em BDD a partir de uma lista de funcionalidades ou de um PRD.

## Prompt

```
Contexto:
Estou desenvolvendo o Shop4u, um aplicativo mobile de e-commerce com recomendacoes por IA.
O publico-alvo sao compradores que usam o celular para fazer compras online.

Objetivo:
Gere User Stories para as funcionalidades listadas abaixo.

Entrada esperada:
Funcionalidades:
- Login com email e senha
- Busca de produtos por nome e categoria
- Adicionar produto ao carrinho
- Finalizar compra com endereco e pagamento

Restricoes:
- Use o formato: Como [perfil], quero [acao], para [beneficio].
- Para cada User Story, inclua pelo menos dois criterios de aceitacao em BDD (Given / When / Then).
- Inclua um checklist tecnico com as tarefas de implementacao.
- Nao crie User Stories para funcionalidades nao listadas.
- Nao use emojis.

Formato de saida:
Para cada funcionalidade, gere:
1. Titulo da User Story (ex: [US-01] Login com email e senha)
2. User Story no formato Como / Quero / Para
3. Criterios de aceitacao em BDD
4. Checklist tecnico
```

## Revisao humana necessaria

Apos gerar as User Stories:

- Verifique se o formato Como / Quero / Para esta correto.
- Confirme se os criterios de aceitacao cobrem os cenarios mais importantes.
- Ajuste o checklist tecnico para refletir a stack real do projeto.
- Numere as User Stories de forma sequencial.

# Prompt: Criar Diagrama UML

## Quando usar

Para gerar diagramas UML em formato Mermaid a partir de uma descricao de funcionalidades ou de User Stories.

## Prompt: Diagrama de Caso de Uso

```
Contexto:
Estou desenvolvendo o Shop4u, um aplicativo mobile de e-commerce.
Os atores principais sao: Usuario nao autenticado, Usuario autenticado e Sistema de recomendacao.

Objetivo:
Gere um diagrama de caso de uso em formato Mermaid para as funcionalidades abaixo.

Entrada esperada:
Funcionalidades:
- Login e cadastro (usuario nao autenticado)
- Busca de produtos (qualquer usuario)
- Adicionar ao carrinho (usuario autenticado)
- Finalizar compra (usuario autenticado)
- Receber recomendacoes (sistema de recomendacao + usuario autenticado)

Restricoes:
- Use sintaxe Mermaid valida.
- Inclua os atores e os casos de uso.
- Nao adicione casos de uso que nao foram mencionados.

Formato de saida:
Bloco de codigo Mermaid pronto para renderizacao.
```

## Prompt: Diagrama de Sequencia

```
Contexto:
Estou documentando o fluxo de login do Shop4u.
O frontend e React Native, o backend e Node.js com Express e o banco e PostgreSQL.

Objetivo:
Gere um diagrama de sequencia em formato Mermaid para o fluxo de login.

Entrada esperada:
Fluxo:
1. Usuario informa email e senha no app
2. App envia POST /auth/login para o backend
3. Backend valida as credenciais no banco
4. Backend retorna token JWT
5. App armazena o token e redireciona para a tela inicial

Restricoes:
- Use sintaxe Mermaid valida.
- Inclua os participantes: App, Backend, Banco de dados.
- Mostre o fluxo de erro (credenciais invalidas) tambem.

Formato de saida:
Bloco de codigo Mermaid pronto para renderizacao.
```

## Revisao humana necessaria

- Verifique se a sintaxe Mermaid esta correta renderizando o diagrama.
- Confirme se os atores e relacionamentos refletem o sistema real.
- Ajuste nomes de endpoints e componentes para os reais do projeto.

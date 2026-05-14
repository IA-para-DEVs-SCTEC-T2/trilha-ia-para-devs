# Exemplos de Testes com Postman

Referencia pratica de validacoes de API usando Postman e a biblioteca `pm`.

## Arquivos disponíveis

| Arquivo | Descricao |
|---------|-----------|
| `validacao-login.md` | Validacoes para o endpoint de login |
| `validacao-produtos.md` | Validacoes para o endpoint de produtos |
| `validacao-carrinho.md` | Validacoes para o endpoint de carrinho |
| `boas-praticas-postman.md` | Boas praticas gerais de testes no Postman |

## Como usar

Cada arquivo contem exemplos de scripts de teste para a aba "Tests" do Postman. Copie os trechos relevantes e adapte para o seu projeto.

## Estrutura basica de um teste no Postman

```javascript
pm.test("descricao do teste", function () {
    // assertiva aqui
});
```

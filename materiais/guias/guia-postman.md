# Guia de Postman

## O que e Postman

Postman e uma ferramenta para testar APIs HTTP. Permite enviar requisicoes, inspecionar respostas e escrever scripts de validacao automatizados.

## Como organizar collections

- Crie uma collection por projeto ou por modulo da API.
- Organize as requisicoes em pastas por recurso (ex: Auth, Produtos, Carrinho).
- Use variaveis de ambiente para URL base, tokens e IDs dinamicos.
- Documente cada requisicao com uma descricao na aba Description.

## Variaveis de ambiente

Crie um environment com variaveis como:

| Variavel | Exemplo de valor |
|----------|-----------------|
| `base_url` | `http://localhost:3000` |
| `auth_token` | _(preenchido pelo script de login)_ |

Use nas requisicoes: `{{base_url}}/products`

## Escrever testes

Os scripts de teste ficam na aba **Scripts > Post-response** de cada requisicao.

### Verificar status code

```javascript
pm.test("status 200", function () {
    pm.response.to.have.status(200);
});
```

### Verificar campo na resposta

```javascript
pm.test("resposta contem token", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("token");
});
```

### Verificar tipo de dado

```javascript
pm.test("price e um numero positivo", function () {
    const json = pm.response.json();
    pm.expect(json.price).to.be.a("number");
    pm.expect(json.price).to.be.greaterThan(0);
});
```

### Verificar array

```javascript
pm.test("resultado e um array nao vazio", function () {
    const json = pm.response.json();
    pm.expect(json).to.be.an("array");
    pm.expect(json.length).to.be.greaterThan(0);
});
```

### Salvar valor para proximas requisicoes

```javascript
pm.test("salva token", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("token");
    pm.environment.set("auth_token", json.token);
});
```

### Verificar tempo de resposta

```javascript
pm.test("resposta em menos de 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

## Executar a collection completa

Use o Collection Runner (botao "Run collection") para executar todos os testes em sequencia e ver o relatorio de resultados.

## Exportar e versionar

Exporte a collection como JSON e salve no repositorio em `docs/` ou `tests/` para que outros membros do time possam importar.

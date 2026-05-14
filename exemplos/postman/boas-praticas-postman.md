# Boas Praticas de Testes no Postman

## Estrutura de um teste

```javascript
pm.test("descricao clara do que esta sendo verificado", function () {
    // assertiva especifica
});
```

Cada `pm.test` deve verificar uma unica coisa. Evite agrupar multiplas assertivas em um unico teste sem necessidade.

## Verificar status code

```javascript
// Forma direta
pm.test("status 200", function () {
    pm.response.to.have.status(200);
});

// Verificar multiplos status aceitos
pm.test("status de sucesso", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 201]);
});
```

## Verificar campos obrigatorios

```javascript
pm.test("resposta tem campos obrigatorios", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("id");
    pm.expect(json).to.have.property("name");
    pm.expect(json).to.have.property("email");
});
```

## Verificar tipos de dados

```javascript
pm.test("campos tem tipos corretos", function () {
    const json = pm.response.json();
    pm.expect(json.id).to.be.a("number");
    pm.expect(json.name).to.be.a("string");
    pm.expect(json.active).to.be.a("boolean");
    pm.expect(json.tags).to.be.an("array");
});
```

## Verificar arrays

```javascript
pm.test("lista nao esta vazia", function () {
    const json = pm.response.json();
    pm.expect(json).to.be.an("array");
    pm.expect(json.length).to.be.greaterThan(0);
});

pm.test("cada item do array tem estrutura correta", function () {
    const json = pm.response.json();
    json.forEach(function (item) {
        pm.expect(item).to.have.property("id");
        pm.expect(item).to.have.property("name");
    });
});
```

## Verificar mensagens de erro

```javascript
pm.test("resposta de erro tem mensagem", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("message");
    pm.expect(json.message).to.be.a("string");
    pm.expect(json.message.length).to.be.greaterThan(0);
});
```

## Salvar valores para uso em outras requisicoes

```javascript
// Na aba Tests de uma requisicao de login
pm.test("salva token para proximas requisicoes", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("token");
    pm.environment.set("auth_token", json.token);
});
```

Nas requisicoes seguintes, use `{{auth_token}}` no header de Authorization.

## Verificar tempo de resposta

```javascript
pm.test("resposta em menos de 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

## Boas praticas gerais

- Use nomes descritivos nos testes: o que esta sendo verificado, nao como.
- Separe colecoes por funcionalidade (login, produtos, carrinho).
- Use variaveis de ambiente para URLs base, tokens e IDs dinamicos.
- Nao hardcode tokens ou senhas nos scripts.
- Organize as requisicoes em pastas dentro da colecao.
- Documente o proposito de cada requisicao na descricao.
- Execute a colecao completa antes de considerar a API validada.

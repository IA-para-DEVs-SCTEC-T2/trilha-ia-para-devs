# Validacao de Produtos - Postman

Scripts de teste para o endpoint de produtos do Shop4u.

## Endpoint

`GET /products`
`GET /products?q={termo}`
`GET /products/{id}`

## Cenario 1: Listar todos os produtos

**Script de teste:**
```javascript
pm.test("status 200 para listagem de produtos", function () {
    pm.response.to.have.status(200);
});

pm.test("resposta e um array", function () {
    const json = pm.response.json();
    pm.expect(json).to.be.an("array");
});

pm.test("cada produto tem campos obrigatorios", function () {
    const json = pm.response.json();
    json.forEach(function (produto) {
        pm.expect(produto).to.have.property("id");
        pm.expect(produto).to.have.property("name");
        pm.expect(produto).to.have.property("price");
        pm.expect(produto.price).to.be.a("number");
        pm.expect(produto.price).to.be.greaterThan(0);
    });
});
```

## Cenario 2: Busca por termo existente

**URL:** `GET /products?q=camiseta`

**Script de teste:**
```javascript
pm.test("status 200 para busca com resultado", function () {
    pm.response.to.have.status(200);
});

pm.test("resultado nao esta vazio", function () {
    const json = pm.response.json();
    pm.expect(json).to.be.an("array");
    pm.expect(json.length).to.be.greaterThan(0);
});

pm.test("produtos retornados contem o termo buscado", function () {
    const json = pm.response.json();
    json.forEach(function (produto) {
        pm.expect(produto.name.toLowerCase()).to.include("camiseta");
    });
});
```

## Cenario 3: Busca sem resultado

**URL:** `GET /products?q=xyzinexistente`

**Script de teste:**
```javascript
pm.test("status 200 para busca sem resultado", function () {
    pm.response.to.have.status(200);
});

pm.test("resultado e array vazio", function () {
    const json = pm.response.json();
    pm.expect(json).to.be.an("array");
    pm.expect(json.length).to.eql(0);
});
```

## Cenario 4: Buscar produto por ID valido

**URL:** `GET /products/1`

**Script de teste:**
```javascript
pm.test("status 200 para produto existente", function () {
    pm.response.to.have.status(200);
});

pm.test("produto retornado tem estrutura correta", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("id");
    pm.expect(json).to.have.property("name");
    pm.expect(json).to.have.property("price");
    pm.expect(json).to.have.property("description");
    pm.expect(json).to.have.property("category");
});
```

## Cenario 5: Buscar produto por ID inexistente

**URL:** `GET /products/99999`

**Script de teste:**
```javascript
pm.test("status 404 para produto inexistente", function () {
    pm.response.to.have.status(404);
});

pm.test("resposta contem mensagem de erro", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("message");
});
```

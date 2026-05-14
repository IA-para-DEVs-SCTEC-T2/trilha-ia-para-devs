# Validacao de Carrinho - Postman

Scripts de teste para os endpoints de carrinho do Shop4u.

## Endpoints

`GET /cart`
`POST /cart/items`
`DELETE /cart/items/{id}`

## Cenario 1: Adicionar item ao carrinho

**Endpoint:** `POST /cart/items`

**Request body:**
```json
{
  "productId": 1,
  "quantity": 2
}
```

**Script de teste:**
```javascript
pm.test("status 201 ao adicionar item", function () {
    pm.response.to.have.status(201);
});

pm.test("item adicionado tem campos obrigatorios", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("id");
    pm.expect(json).to.have.property("productId");
    pm.expect(json).to.have.property("quantity");
    pm.expect(json.quantity).to.eql(2);
});
```

## Cenario 2: Adicionar item com quantidade zero

**Request body:**
```json
{
  "productId": 1,
  "quantity": 0
}
```

**Script de teste:**
```javascript
pm.test("status 400 para quantidade zero", function () {
    pm.response.to.have.status(400);
});

pm.test("erro menciona campo quantity", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("errors");
    const campoQuantidade = json.errors.find(e => e.field === "quantity");
    pm.expect(campoQuantidade).to.not.be.undefined;
});
```

## Cenario 3: Visualizar carrinho

**Endpoint:** `GET /cart`

**Script de teste:**
```javascript
pm.test("status 200 ao visualizar carrinho", function () {
    pm.response.to.have.status(200);
});

pm.test("carrinho tem estrutura correta", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("items");
    pm.expect(json).to.have.property("total");
    pm.expect(json.items).to.be.an("array");
    pm.expect(json.total).to.be.a("number");
    pm.expect(json.total).to.be.at.least(0);
});

pm.test("total e consistente com os itens", function () {
    const json = pm.response.json();
    const totalCalculado = json.items.reduce(function (acc, item) {
        return acc + (item.price * item.quantity);
    }, 0);
    pm.expect(json.total).to.be.closeTo(totalCalculado, 0.01);
});
```

## Cenario 4: Remover item do carrinho

**Endpoint:** `DELETE /cart/items/1`

**Script de teste:**
```javascript
pm.test("status 204 ao remover item", function () {
    pm.response.to.have.status(204);
});
```

## Cenario 5: Remover item inexistente

**Endpoint:** `DELETE /cart/items/99999`

**Script de teste:**
```javascript
pm.test("status 404 ao remover item inexistente", function () {
    pm.response.to.have.status(404);
});
```

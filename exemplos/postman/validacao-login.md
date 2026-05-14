# Validacao de Login - Postman

Scripts de teste para o endpoint de autenticacao do Shop4u.

## Endpoint

`POST /auth/login`

## Cenario 1: Login com credenciais validas

**Request body:**
```json
{
  "email": "usuario@shop4u.com",
  "password": "senha123"
}
```

**Script de teste:**
```javascript
pm.test("status 200 para login valido", function () {
    pm.response.to.have.status(200);
});

pm.test("resposta contem token", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("token");
    pm.expect(json.token).to.be.a("string");
    pm.expect(json.token.length).to.be.greaterThan(0);
});

pm.test("resposta contem dados do usuario", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("user");
    pm.expect(json.user).to.have.property("email");
    pm.expect(json.user.email).to.eql("usuario@shop4u.com");
});
```

## Cenario 2: Login com senha incorreta

**Request body:**
```json
{
  "email": "usuario@shop4u.com",
  "password": "senhaerrada"
}
```

**Script de teste:**
```javascript
pm.test("status 401 para senha incorreta", function () {
    pm.response.to.have.status(401);
});

pm.test("resposta contem mensagem de erro", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("message");
    pm.expect(json.message).to.be.a("string");
});

pm.test("resposta nao contem token", function () {
    const json = pm.response.json();
    pm.expect(json).to.not.have.property("token");
});
```

## Cenario 3: Login com email vazio

**Request body:**
```json
{
  "email": "",
  "password": "senha123"
}
```

**Script de teste:**
```javascript
pm.test("status 400 para email vazio", function () {
    pm.response.to.have.status(400);
});

pm.test("resposta contem erro de validacao", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("errors");
    pm.expect(json.errors).to.be.an("array");
});
```

## Cenario 4: Login com email invalido

**Request body:**
```json
{
  "email": "nao-e-um-email",
  "password": "senha123"
}
```

**Script de teste:**
```javascript
pm.test("status 400 para email invalido", function () {
    pm.response.to.have.status(400);
});

pm.test("mensagem de erro menciona email", function () {
    const json = pm.response.json();
    pm.expect(json.errors[0].field).to.eql("email");
});
```

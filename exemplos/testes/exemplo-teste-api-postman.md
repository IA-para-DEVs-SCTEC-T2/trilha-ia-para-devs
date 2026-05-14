# Exemplo de Teste de API com Postman

## Endpoint testado

`POST /auth/login`

## Cenario positivo: login com credenciais validas

**Request:**
- Method: POST
- URL: `{{base_url}}/auth/login`
- Body (JSON):
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

pm.test("resposta contem token JWT", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("token");
    pm.expect(json.token).to.be.a("string");
    pm.expect(json.token.length).to.be.greaterThan(10);
});

pm.test("tempo de resposta abaixo de 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

// Salva o token para uso nas proximas requisicoes
pm.environment.set("auth_token", pm.response.json().token);
```

## Cenario negativo: senha incorreta

**Body:**
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

pm.test("resposta nao contem token", function () {
    const json = pm.response.json();
    pm.expect(json).to.not.have.property("token");
});

pm.test("mensagem de erro presente", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("message");
});
```

## Cenario de validacao: campos ausentes

**Body:**
```json
{}
```

**Script de teste:**
```javascript
pm.test("status 400 para body vazio", function () {
    pm.response.to.have.status(400);
});

pm.test("erros de validacao presentes", function () {
    const json = pm.response.json();
    pm.expect(json).to.have.property("errors");
    pm.expect(json.errors).to.be.an("array");
    pm.expect(json.errors.length).to.be.greaterThan(0);
});
```

## Como usar o token nas proximas requisicoes

Apos o login bem-sucedido, o token e salvo na variavel de ambiente `auth_token`. Use-o no header das requisicoes autenticadas:

```
Authorization: Bearer {{auth_token}}
```

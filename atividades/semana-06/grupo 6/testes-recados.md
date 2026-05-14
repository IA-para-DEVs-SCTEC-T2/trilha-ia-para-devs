# Casos de Teste — API de Recados

**Base URL:** `http://localhost:3000`  
**Collection:** `api-recados.postman_collection.json`

---

## Home

### CT-01 — GET / — Verifica API funcionando

**Método:** GET  
**Endpoint:** `/`

```javascript
pm.test('Status 200', function () {
    pm.response.to.have.status(200);
});

pm.test('Mensagem de boas-vindas presente', function () {
    var json = pm.response.json();
    pm.expect(json.message).to.eql('API de recados funcionando');
});

pm.test('Endpoints listados na resposta', function () {
    var json = pm.response.json();
    pm.expect(json.endpoints).to.have.property('listar_recados');
    pm.expect(json.endpoints).to.have.property('criar_recado');
});
```

---

## Cenário 1 — POST /recados — Criar recado

### CT-02 — Criar recado válido

**Método:** POST  
**Endpoint:** `/recados`  
**Body:**
```json
{
  "autor": "João Silva",
  "mensagem": "Não esqueça da reunião às 15h"
}
```

```javascript
pm.test('Status 201 - Recado criado', function () {
    pm.response.to.have.status(201);
});

pm.test('Resposta contém campo id', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('id');
    pm.expect(json.id).to.be.a('number');
});

pm.test('Resposta contém campo autor correto', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('autor');
    pm.expect(json.autor).to.eql('João Silva');
});

pm.test('Resposta contém campo mensagem correto', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('mensagem');
    pm.expect(json.mensagem).to.eql('Não esqueça da reunião às 15h');
});

pm.test('Campo lido deve ser false por padrão', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('lido');
    pm.expect(json.lido).to.eql(false);
});

pm.globals.set('ultimo_recado_id', pm.response.json().id);
```

## Cenário 2 — GET /recados — Listar recados

### CT-04 — Listar todos os recados

**Método:** GET  
**Endpoint:** `/recados`

```javascript
pm.test('Status 200', function () {
    pm.response.to.have.status(200);
});

pm.test('Retorna uma lista (array)', function () {
    var json = pm.response.json();
    pm.expect(json).to.be.an('array');
});

pm.test('Lista contém ao menos um recado', function () {
    var json = pm.response.json();
    pm.expect(json.length).to.be.greaterThan(0);
});

pm.test('Cada recado possui os campos obrigatórios', function () {
    var json = pm.response.json();
    json.forEach(function (recado) {
        pm.expect(recado).to.have.property('id');
        pm.expect(recado).to.have.property('autor');
        pm.expect(recado).to.have.property('mensagem');
        pm.expect(recado).to.have.property('lido');
    });
});

pm.test('Campo id é número em todos os recados', function () {
    var json = pm.response.json();
    json.forEach(function (recado) {
        pm.expect(recado.id).to.be.a('number');
    });
});

pm.test('Campo lido é booleano em todos os recados', function () {
    var json = pm.response.json();
    json.forEach(function (recado) {
        pm.expect(recado.lido).to.be.a('boolean');
    });
});
```

---

### CT-05 — Resposta é sempre um array (mesmo com lista vazia)

**Método:** GET  
**Endpoint:** `/recados`

```javascript
pm.test('Status 200 mesmo com lista vazia', function () {
    pm.response.to.have.status(200);
});

pm.test('Resposta é sempre um array', function () {
    var json = pm.response.json();
    pm.expect(json).to.be.an('array');
});
```

---

## Cenário 3 — POST /recados — Erros de validação

### CT-06 — Erro: sem campo `mensagem`

**Método:** POST  
**Endpoint:** `/recados`  
**Body:**
```json
{
  "autor": "João Silva"
}
```

```javascript
pm.test('Status 400 - Mensagem obrigatória', function () {
    pm.response.to.have.status(400);
});

pm.test('Resposta contém campo error', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('error');
});

pm.test('Campo error não está vazio', function () {
    var json = pm.response.json();
    pm.expect(json.error).to.be.a('string');
    pm.expect(json.error.length).to.be.greaterThan(0);
});
```

---

### CT-07 — Erro: sem campo `autor`

**Método:** POST  
**Endpoint:** `/recados`  
**Body:**
```json
{
  "mensagem": "Lembrete importante"
}
```

```javascript
pm.test('Status 400 - Autor obrigatório', function () {
    pm.response.to.have.status(400);
});

pm.test('Resposta contém campo error', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('error');
});

pm.test('Mensagem de erro menciona campos obrigatórios', function () {
    var json = pm.response.json();
    pm.expect(json.error).to.include('obrigatórios');
});
```

---

### CT-08 — Erro: sem `autor` e sem `mensagem`

**Método:** POST  
**Endpoint:** `/recados`  
**Body:**
```json
{}
```

```javascript
pm.test('Status 400 - Campos obrigatórios ausentes', function () {
    pm.response.to.have.status(400);
});

pm.test('Resposta contém campo error', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('error');
});
```

---

### CT-09 — Erro: body completamente vazio (sem JSON)

**Método:** POST  
**Endpoint:** `/recados`  
**Body:** nenhum (vazio)

```javascript
pm.test('Status 400 - Body obrigatório', function () {
    pm.response.to.have.status(400);
});

pm.test('Resposta contém campo error', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('error');
});

pm.test('Mensagem de erro: Body JSON obrigatório', function () {
    var json = pm.response.json();
    pm.expect(json.error).to.eql('Body JSON obrigatório');
});
```

---

## Resumo dos casos de teste

| ID | Endpoint | Método | Cenário | Status esperado |
|---|---|---|---|---|
| CT-01 | `/` | GET | API funcionando | 200 |
| CT-02 | `/recados` | POST | Criar recado válido | 201 |
| CT-04 | `/recados` | GET | Listar recados com dados | 200 |
| CT-05 | `/recados` | GET | Resposta sempre é array | 200 |
| CT-06 | `/recados` | POST | Sem campo `mensagem` | 400 |
| CT-07 | `/recados` | POST | Sem campo `autor` | 400 |
| CT-08 | `/recados` | POST | Sem `autor` e sem `mensagem` | 400 |
| CT-09 | `/recados` | POST | Body vazio | 400 |

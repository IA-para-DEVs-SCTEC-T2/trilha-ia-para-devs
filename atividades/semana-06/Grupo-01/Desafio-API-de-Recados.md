# Desafio — API de Recados

Testes realizados no Postman para a API Flask rodando em `http://localhost:3000`.

---

## Cenário 1 — Criar recado

| Campo | Valor |
|---|---|
| Método | POST |
| Endpoint | `/recados` |
| Status esperado | 201 |

### Prompt utilizado

> Gere scripts Post-response para o Postman usando JavaScript.
>
> Endpoint: POST http://localhost:3000/recados
>
> Body enviado:
> ```json
> {
>     "autor": "Ana",
>     "mensagem": "Revisar o material da aula"
> }
> ```
>
> Valide:
> - status code 201
> - campo id presente
> - autor igual a "Ana"
> - mensagem igual a "Revisar o material da aula"
> - lido igual a false

### Script Post-response

```javascript
const response = pm.response.json();

pm.test("Status code é 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Campo id está presente", function () {
    pm.expect(response).to.have.property("id");
});

pm.test("Autor é 'Ana'", function () {
    pm.expect(response.autor).to.eql("Ana");
});

pm.test("Mensagem é 'Revisar o material da aula'", function () {
    pm.expect(response.mensagem).to.eql("Revisar o material da aula");
});

pm.test("Lido é false", function () {
    pm.expect(response.lido).to.eql(false);
});
```

### Resultado dos testes

| Status | Teste |
|---|---|
| ✅ passed | Status code é 201 |
| ✅ passed | Campo id está presente |
| ✅ passed | Autor é 'Ana' |
| ✅ passed | Mensagem é 'Revisar o material da aula' |
| ✅ passed | Lido é false |

---

## Cenário 2 — Listar recados

| Campo | Valor |
|---|---|
| Método | GET |
| Endpoint | `/recados` |
| Status esperado | 200 |

### Prompt utilizado

> Gere scripts Post-response para o Postman usando JavaScript.
>
> Endpoint: GET http://localhost:3000/recados
>
> Valide:
> - status code 200
> - resposta é um array
> - lista não está vazia
> - cada recado possui os campos: id, autor, mensagem e lido

### Script Post-response

```javascript
const response = pm.response.json();

pm.test("Status code é 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Resposta é um array", function () {
    pm.expect(response).to.be.an("array");
});

pm.test("Lista não está vazia", function () {
    pm.expect(response.length).to.be.greaterThan(0);
});

pm.test("Todos os recados possuem campo id", function () {
    response.forEach(function (recado) {
        pm.expect(recado).to.have.property("id");
    });
});

pm.test("Todos os recados possuem campo autor", function () {
    response.forEach(function (recado) {
        pm.expect(recado).to.have.property("autor");
    });
});

pm.test("Todos os recados possuem campo mensagem", function () {
    response.forEach(function (recado) {
        pm.expect(recado).to.have.property("mensagem");
    });
});

pm.test("Todos os recados possuem campo lido", function () {
    response.forEach(function (recado) {
        pm.expect(recado).to.have.property("lido");
    });
});
```

### Resultado dos testes

| Status | Teste |
|---|---|
| ✅ passed | Status code é 200 |
| ✅ passed | Resposta é um array |
| ✅ passed | Lista não está vazia |
| ✅ passed | Todos os recados possuem campo id |
| ✅ passed | Todos os recados possuem campo autor |
| ✅ passed | Todos os recados possuem campo mensagem |
| ✅ passed | Todos os recados possuem campo lido |

---

## Cenário 3 — Erro sem mensagem

| Campo | Valor |
|---|---|
| Método | POST |
| Endpoint | `/recados` |
| Status esperado | 400 |

### Prompt utilizado

> Gere scripts Post-response para o Postman usando JavaScript.
>
> Endpoint: POST http://localhost:3000/recados
>
> Body enviado:
> ```json
> { "autor": "Ana" }
> ```
>
> Valide:
> - status code 400
> - campo error está presente
> - campo error não está vazio

### Script Post-response

```javascript
const response = pm.response.json();

pm.test("Status code é 400", function () {
    pm.response.to.have.status(400);
});

pm.test("Campo error está presente", function () {
    pm.expect(response).to.have.property("error");
});

pm.test("Campo error não está vazio", function () {
    pm.expect(response.error).to.be.a("string").and.not.empty;
});
```

### Resultado dos testes

| Status | Teste |
|---|---|
| ✅ passed | Status code é 400 |
| ✅ passed | Campo error está presente |
| ✅ passed | Campo error não está vazio |

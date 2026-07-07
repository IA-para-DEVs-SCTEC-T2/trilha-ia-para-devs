# Testar via terminal
pytest test_recados.py

# Testes Postman — API de Recados

Scripts prontos para colar na aba **Tests** de cada requisição no Postman.

---

## Cenário 1 — `POST /recados` (sucesso)

```javascript
pm.test("Status 201", () => {
    pm.response.to.have.status(201);
});

pm.test("Campos obrigatórios presentes", () => {
    const json = pm.response.json();
    pm.expect(json).to.have.property("id");
    pm.expect(json).to.have.property("autor");
    pm.expect(json).to.have.property("mensagem");
    pm.expect(json).to.have.property("lido");
});

pm.test("lido é false na criação", () => {
    pm.expect(pm.response.json().lido).to.be.false;
});

pm.test("id é um número", () => {
    pm.expect(pm.response.json().id).to.be.a("number");
});
```

---

## Cenário 2 — `GET /recados` (listar)

```javascript
pm.test("Status 200", () => {
    pm.response.to.have.status(200);
});

pm.test("Resposta é uma lista", () => {
    pm.expect(pm.response.json()).to.be.an("array");
});

pm.test("Cada item tem os campos obrigatórios", () => {
    pm.response.json().forEach(item => {
        pm.expect(item).to.have.property("id");
        pm.expect(item).to.have.property("autor");
        pm.expect(item).to.have.property("mensagem");
        pm.expect(item).to.have.property("lido");
    });
});
```

---

## Cenário 3 — `POST /recados` sem mensagem (erro)

```javascript
pm.test("Status 400", () => {
    pm.response.to.have.status(400);
});

pm.test("Campo error presente", () => {
    pm.expect(pm.response.json()).to.have.property("error");
});

pm.test("Mensagem de error não está vazia", () => {
    pm.expect(pm.response.json().error).to.be.a("string").and.not.empty;
});
```

# API de Recados — grupo-07

API REST simples para gerenciamento de recados, construída com Flask.

---

## Como rodar

```bash
pip install -r requirements.txt
python app.py
```

A API ficará disponível em `http://localhost:5000`.

---

## Como testar (automatizado)

```bash
pytest test_recados.py -v
```

---

## Endpoints

### POST /recados — Criar recado

**Request body:**
```json
{
  "autor": "Ana",
  "mensagem": "Olá, tudo bem?"
}
```

**Resposta de sucesso (201):**
```json
{
  "id": 1,
  "autor": "Ana",
  "mensagem": "Olá, tudo bem?",
  "lido": false
}
```

**Resposta de erro (400) — campo obrigatório ausente:**
```json
{
  "error": "mensagem é obrigatória"
}
```

---

### GET /recados — Listar recados

**Resposta (200):**
```json
[
  {
    "id": 1,
    "autor": "Ana",
    "mensagem": "Olá, tudo bem?",
    "lido": false
  }
]
```

---

## Testando no Postman

### Cenário 1 — Criar recado (sucesso)

| Campo | Valor |
|-------|-------|
| Método | POST |
| URL | `http://localhost:5000/recados` |
| Body | raw → JSON |

Body:
```json
{ "autor": "Ana", "mensagem": "Olá mundo" }
```

**Test script (aba Tests):**
```javascript
pm.test("Status 201", () => pm.response.to.have.status(201));
pm.test("Campos obrigatórios presentes", () => {
    const json = pm.response.json();
    pm.expect(json).to.have.property("id");
    pm.expect(json).to.have.property("autor");
    pm.expect(json).to.have.property("mensagem");
    pm.expect(json.lido).to.be.false;
});
```

---

### Cenário 2 — Listar recados

| Campo | Valor |
|-------|-------|
| Método | GET |
| URL | `http://localhost:5000/recados` |

**Test script:**
```javascript
pm.test("Status 200", () => pm.response.to.have.status(200));
pm.test("Resposta é lista", () => {
    pm.expect(pm.response.json()).to.be.an("array");
});
pm.test("Campos obrigatórios em cada item", () => {
    pm.response.json().forEach(item => {
        pm.expect(item).to.have.all.keys("id", "autor", "mensagem", "lido");
    });
});
```

---

### Cenário 3 — Criar recado sem mensagem (erro)

| Campo | Valor |
|-------|-------|
| Método | POST |
| URL | `http://localhost:5000/recados` |
| Body | raw → JSON |

Body:
```json
{ "autor": "Ana" }
```

**Test script:**
```javascript
pm.test("Status 400", () => pm.response.to.have.status(400));
pm.test("Campo error presente", () => {
    pm.expect(pm.response.json()).to.have.property("error");
});
```

---

## Testando no Insomnia

### Cenário 1 — Criar recado (sucesso)

- **Método:** POST
- **URL:** `http://localhost:5000/recados`
- **Body:** JSON
```json
{ "autor": "Ana", "mensagem": "Olá mundo" }
```
- **Validar:** status `201`, body contém `id`, `autor`, `mensagem`, `lido: false`

---

### Cenário 2 — Listar recados

- **Método:** GET
- **URL:** `http://localhost:5000/recados`
- **Validar:** status `200`, body é array, cada item tem `id`, `autor`, `mensagem`, `lido`

---

### Cenário 3 — Erro sem mensagem

- **Método:** POST
- **URL:** `http://localhost:5000/recados`
- **Body:** JSON
```json
{ "autor": "Ana" }
```
- **Validar:** status `400`, body contém campo `error`

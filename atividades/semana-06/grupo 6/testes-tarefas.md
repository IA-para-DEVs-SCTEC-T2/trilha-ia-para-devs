# Casos de Teste — API de Tarefas

**Base URL:** `http://localhost:3000`  
**Collection:** `api-tarefas.postman_collection.json`

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
    pm.expect(json.message).to.eql('API de tarefas funcionando');
});

pm.test('Endpoints listados na resposta', function () {
    var json = pm.response.json();
    pm.expect(json.endpoints).to.have.property('listar_tarefas');
    pm.expect(json.endpoints).to.have.property('criar_tarefa');
    pm.expect(json.endpoints).to.have.property('concluir_tarefa');
});
```

---

## Cenário 1 — POST /tarefas — Criar tarefa

### CT-02 — Criar tarefa válida

**Método:** POST  
**Endpoint:** `/tarefas`  
**Body:**
```json
{
  "titulo": "Implementar login",
  "responsavel": "João Silva"
}
```

```javascript
pm.test('Status 201 - Tarefa criada', function () {
    pm.response.to.have.status(201);
});

pm.test('Resposta contém campo id', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('id');
    pm.expect(json.id).to.be.a('number');
});

pm.test('Resposta contém campo titulo correto', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('titulo');
    pm.expect(json.titulo).to.eql('Implementar login');
});

pm.test('Resposta contém campo responsavel correto', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('responsavel');
    pm.expect(json.responsavel).to.eql('João Silva');
});

pm.test('Campo concluida deve ser false por padrão', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('concluida');
    pm.expect(json.concluida).to.eql(false);
});

pm.globals.set('ultima_tarefa_id', pm.response.json().id);
```

---

### CT-03 — Criar segunda tarefa (IDs incrementais)

**Método:** POST  
**Endpoint:** `/tarefas`  
**Body:**
```json
{
  "titulo": "Revisar pull request",
  "responsavel": "Maria Souza"
}
```

```javascript
pm.test('Status 201 - Segunda tarefa criada', function () {
    pm.response.to.have.status(201);
});

pm.test('ID da segunda tarefa é maior que o da primeira', function () {
    var json = pm.response.json();
    var primeiroId = pm.globals.get('ultima_tarefa_id');
    pm.expect(json.id).to.be.greaterThan(Number(primeiroId));
});

pm.test('Campo concluida deve ser false por padrão', function () {
    var json = pm.response.json();
    pm.expect(json.concluida).to.eql(false);
});
```

---

## Cenário 2 — GET /tarefas — Listar tarefas

### CT-04 — Listar todas as tarefas

**Método:** GET  
**Endpoint:** `/tarefas`

```javascript
pm.test('Status 200', function () {
    pm.response.to.have.status(200);
});

pm.test('Retorna uma lista (array)', function () {
    var json = pm.response.json();
    pm.expect(json).to.be.an('array');
});

pm.test('Lista contém ao menos uma tarefa', function () {
    var json = pm.response.json();
    pm.expect(json.length).to.be.greaterThan(0);
});

pm.test('Cada tarefa possui os campos obrigatórios', function () {
    var json = pm.response.json();
    json.forEach(function (tarefa) {
        pm.expect(tarefa).to.have.property('id');
        pm.expect(tarefa).to.have.property('titulo');
        pm.expect(tarefa).to.have.property('responsavel');
        pm.expect(tarefa).to.have.property('concluida');
    });
});

pm.test('Campo id é número em todas as tarefas', function () {
    var json = pm.response.json();
    json.forEach(function (tarefa) {
        pm.expect(tarefa.id).to.be.a('number');
    });
});

pm.test('Campo concluida é booleano em todas as tarefas', function () {
    var json = pm.response.json();
    json.forEach(function (tarefa) {
        pm.expect(tarefa.concluida).to.be.a('boolean');
    });
});
```

---

### CT-05 — Resposta é sempre um array (mesmo com lista vazia)

**Método:** GET  
**Endpoint:** `/tarefas`

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

## Cenário 3 — GET /tarefas/:id — Buscar tarefa por ID

### CT-06 — Buscar tarefa existente por ID

**Método:** GET  
**Endpoint:** `/tarefas/1`

```javascript
pm.test('Status 200 - Tarefa encontrada', function () {
    pm.response.to.have.status(200);
});

pm.test('Retorna a tarefa com id correto', function () {
    var json = pm.response.json();
    pm.expect(json.id).to.eql(1);
});

pm.test('Tarefa possui campos obrigatórios', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('id');
    pm.expect(json).to.have.property('titulo');
    pm.expect(json).to.have.property('responsavel');
    pm.expect(json).to.have.property('concluida');
});
```

---

### CT-07 — Buscar tarefa com ID inexistente

**Método:** GET  
**Endpoint:** `/tarefas/999`

```javascript
pm.test('Status 404 - Tarefa não encontrada', function () {
    pm.response.to.have.status(404);
});

pm.test('Resposta contém campo error', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('error');
});

pm.test('Mensagem de erro correta', function () {
    var json = pm.response.json();
    pm.expect(json.error).to.eql('Tarefa não encontrada');
});
```

---

## Cenário 4 — POST /tarefas/:id/concluir — Concluir tarefa

### CT-08 — Concluir tarefa existente

**Método:** POST  
**Endpoint:** `/tarefas/1/concluir`  
**Body:** nenhum

```javascript
pm.test('Status 200 - Tarefa concluída', function () {
    pm.response.to.have.status(200);
});

pm.test('Campo concluida deve ser true após concluir', function () {
    var json = pm.response.json();
    pm.expect(json.concluida).to.eql(true);
});

pm.test('Retorna a tarefa com id correto', function () {
    var json = pm.response.json();
    pm.expect(json.id).to.eql(1);
});

pm.test('Tarefa mantém os demais campos', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('titulo');
    pm.expect(json).to.have.property('responsavel');
});
```

---

### CT-09 — Concluir tarefa com ID inexistente

**Método:** POST  
**Endpoint:** `/tarefas/999/concluir`  
**Body:** nenhum

```javascript
pm.test('Status 404 - Tarefa não encontrada', function () {
    pm.response.to.have.status(404);
});

pm.test('Resposta contém campo error', function () {
    var json = pm.response.json();
    pm.expect(json).to.have.property('error');
});

pm.test('Mensagem de erro correta', function () {
    var json = pm.response.json();
    pm.expect(json.error).to.eql('Tarefa não encontrada');
});
```

---

## Cenário 5 — POST /tarefas — Erros de validação

### CT-10 — Erro: body vazio (sem JSON)

**Método:** POST  
**Endpoint:** `/tarefas`  
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

### CT-11 — Erro: sem campo `titulo`

**Método:** POST  
**Endpoint:** `/tarefas`  
**Body:**
```json
{
  "responsavel": "João Silva"
}
```

```javascript
pm.test('Status 400 - Titulo obrigatório', function () {
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

### CT-12 — Erro: sem campo `responsavel`

**Método:** POST  
**Endpoint:** `/tarefas`  
**Body:**
```json
{
  "titulo": "Implementar login"
}
```

```javascript
pm.test('Status 400 - Responsavel obrigatório', function () {
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

### CT-13 — Erro: sem `titulo` e sem `responsavel`

**Método:** POST  
**Endpoint:** `/tarefas`  
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

## Resumo dos casos de teste

| ID | Endpoint | Método | Cenário | Status esperado |
|---|---|---|---|---|
| CT-01 | `/` | GET | API funcionando | 200 |
| CT-02 | `/tarefas` | POST | Criar tarefa válida | 201 |
| CT-03 | `/tarefas` | POST | IDs incrementais | 201 |
| CT-04 | `/tarefas` | GET | Listar tarefas com dados | 200 |
| CT-05 | `/tarefas` | GET | Resposta sempre é array | 200 |
| CT-06 | `/tarefas/1` | GET | Buscar tarefa existente | 200 |
| CT-07 | `/tarefas/999` | GET | Buscar tarefa inexistente | 404 |
| CT-08 | `/tarefas/1/concluir` | POST | Concluir tarefa existente | 200 |
| CT-09 | `/tarefas/999/concluir` | POST | Concluir tarefa inexistente | 404 |
| CT-10 | `/tarefas` | POST | Body vazio | 400 |
| CT-11 | `/tarefas` | POST | Sem campo `titulo` | 400 |
| CT-12 | `/tarefas` | POST | Sem campo `responsavel` | 400 |
| CT-13 | `/tarefas` | POST | Sem `titulo` e sem `responsavel` | 400 |

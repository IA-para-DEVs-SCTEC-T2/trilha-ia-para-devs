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

### Resultado dos testes

| Status | Teste |
|---|---|
| ✅ passed | Status code é 400 |
| ✅ passed | Campo error está presente |
| ✅ passed | Campo error não está vazio |

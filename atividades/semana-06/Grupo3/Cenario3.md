# Prompt Usado:
Gere scripts Post-response para o Postman usando JavaScript.

Endpoint:
POST http://localhost:3000/recados

Body enviado:
{
    "autor": "Ana"
}

Resposta esperada:
{
    "error": "Campos obrigatórios: autor e mensagem"
}

Valide:
- status code 400
- campo error presente
- mensagem de erro igual a "Campos obrigatórios: autor e mensagem"
- validar que o campo error contém a palavra "mensagem"

Requisitos:
- Use pm.test()
- Use pm.response.to.have.status()
- Use pm.expect()
- Gere apenas o código, sem explicações.

# Script gerado:
pm.test("Status code deve ser 400", function () {
    pm.response.to.have.status(400);
});

pm.test("Resposta deve conter o campo error", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData).to.have.property("error");
});

pm.test("Mensagem de erro deve informar campos obrigatórios", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData.error).to.eql("Campos obrigatórios: autor e mensagem");
});

pm.test("Erro deve mencionar o campo mensagem", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData.error).to.include("mensagem");
});
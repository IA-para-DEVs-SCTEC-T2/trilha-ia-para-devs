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
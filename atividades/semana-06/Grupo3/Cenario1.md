pm.test("Status code deve ser 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Resposta deve conter o campo id", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData).to.have.property("id");
    pm.expect(jsonData.id).to.be.a("number");
});

pm.test("Autor deve ser Ana", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData.autor).to.eql("Ana");
});

pm.test("Mensagem deve ser 'Revisar o material da aula'", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData.mensagem).to.eql("Revisar o material da aula");
});

pm.test("Campo lido deve ser false", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData.lido).to.eql(false);
});
pm.test("Status code deve ser 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Resposta deve ser uma lista", function () {
    const jsonData = pm.response.json();

    pm.expect(jsonData).to.be.an("array");
});

pm.test("Todos os recados devem conter os campos obrigatórios", function () {
    const jsonData = pm.response.json();

    jsonData.forEach((recado) => {
        pm.expect(recado).to.have.property("id");
        pm.expect(recado).to.have.property("autor");
        pm.expect(recado).to.have.property("mensagem");
        pm.expect(recado).to.have.property("lido");
    });
});
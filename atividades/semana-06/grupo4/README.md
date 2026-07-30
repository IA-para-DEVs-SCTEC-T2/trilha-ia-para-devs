// Cenário 1 — POST /recados: criar recado com sucesso

const jsonData = pm.response.json();

pm.test("Status 201 Created", function () {
    pm.response.to.have.status(201);
});

pm.test("Resposta contém campo 'id'", function () {
    pm.expect(jsonData).to.have.property("id");
    pm.expect(jsonData.id).to.be.a("number");
});

pm.test("Campo 'autor' corresponde ao enviado", function () {
    const body = JSON.parse(pm.request.body.raw);
    pm.expect(jsonData.autor).to.eql(body.autor);
});

pm.test("Campo 'mensagem' corresponde ao enviado", function () {
    const body = JSON.parse(pm.request.body.raw);
    pm.expect(jsonData.mensagem).to.eql(body.mensagem);
});

pm.test("Campo 'lido' é false", function () {
    pm.expect(jsonData.lido).to.be.false;
});

// Cenário 2 — GET /recados: listar recados

const jsonData = pm.response.json();

pm.test("Status 200 OK", function () {
    pm.response.to.have.status(200);
});

pm.test("Resposta é um array", function () {
    pm.expect(jsonData).to.be.an("array");
});

pm.test("Cada recado contém os campos obrigatórios", function () {
    jsonData.forEach(function (recado) {
        pm.expect(recado).to.have.property("id");
        pm.expect(recado).to.have.property("autor");
        pm.expect(recado).to.have.property("mensagem");
        pm.expect(recado).to.have.property("lido");
    });
});

pm.test("Campo 'id' é um número em todos os recados", function () {
    jsonData.forEach(function (recado) {
        pm.expect(recado.id).to.be.a("number");
    });
});

pm.test("Campo 'autor' é uma string não vazia em todos os recados", function () {
    jsonData.forEach(function (recado) {
        pm.expect(recado.autor).to.be.a("string").and.not.empty;
    });
});

pm.test("Campo 'mensagem' é uma string não vazia em todos os recados", function () {
    jsonData.forEach(function (recado) {
        pm.expect(recado.mensagem).to.be.a("string").and.not.empty;
    });
});

pm.test("Campo 'lido' é um booleano em todos os recados", function () {
    jsonData.forEach(function (recado) {
        pm.expect(recado.lido).to.be.a("boolean");
    });
});

// Cenário 3 — POST /recados: erro ao enviar sem mensagem

const jsonData = pm.response.json();

pm.test("Status 400 Bad Request", function () {
    pm.response.to.have.status(400);
});

pm.test("Resposta contém campo 'error'", function () {
    pm.expect(jsonData).to.have.property("error");
});

pm.test("Campo 'error' é uma string não vazia", function () {
    pm.expect(jsonData.error).to.be.a("string").and.not.empty;
});

pm.test("Mensagem de erro menciona campos obrigatórios", function () {
    pm.expect(jsonData.error).to.include("obrigatórios");
});

pm.test("Resposta não contém campos de recado válido", function () {
    pm.expect(jsonData).to.not.have.property("id");
    pm.expect(jsonData).to.not.have.property("lido");
});
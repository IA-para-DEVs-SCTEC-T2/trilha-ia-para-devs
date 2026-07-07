
# Scripts

## Cenário 1
pm.test("Status code é 201 Created", function () {
    pm.response.to.have.status(201);
});

pm.test("Resposta contém os campos id, autor, mensagem e lido", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("id");
    pm.expect(jsonData).to.have.property("autor");
    pm.expect(jsonData).to.have.property("mensagem");
    pm.expect(jsonData).to.have.property("lido");
});

pm.test("Campo 'lido' deve ser false", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.lido).to.eql(false);
});

pm.test("Campo 'autor' deve corresponder ao enviado no body", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.autor).to.eql("João da Silva");
});

pm.test("Campo 'mensagem' deve corresponder ao enviado no body", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.mensagem).to.eql("Esse é meu primeiro recado");
});

## Cenário 2

pm.test("Status code é 200 OK", function () {
    pm.response.to.have.status(200);
});

pm.test("Resposta deve ser uma lista (array)", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an("array");
});

pm.test("Cada elemento da lista contém os campos id, autor, mensagem e lido", function () {
    const jsonData = pm.response.json();
    jsonData.forEach((recado) => {
        pm.expect(recado).to.have.property("id");
        pm.expect(recado).to.have.property("autor");
        pm.expect(recado).to.have.property("mensagem");
        pm.expect(recado).to.have.property("lido");
    });
});

## Cenário 3
pm.test("Status code é 400 Bad Request", function () {
    pm.response.to.have.status(400);
});

pm.test("Body deve conter o campo 'error'", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("error");
});

pm.test("Campo 'error' deve conter a mensagem esperada", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.error).to.eql("Campos obrigatórios: autor e mensagem");
});
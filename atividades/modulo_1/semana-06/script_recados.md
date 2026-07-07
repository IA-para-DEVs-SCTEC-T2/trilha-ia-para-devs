const json = pm.response.json();

pm.test("Status code é 201", () => {
    pm.response.to.have.status(201);
});

pm.test("Campo 'id' está presente", () => {
    pm.expect(json).to.have.property("id");
    pm.expect(json.id).to.not.be.null;
});

pm.test("Campo 'quantidade' é 2", () => {
    pm.expect(json.quantidade).to.equal(2);
});

pm.test("Campo 'subtotal' é 7000", () => {
    pm.expect(json.subtotal).to.equal(7000);
});

pm.test("Campo 'desconto' é 700", () => {
    pm.expect(json.desconto).to.equal(700);
});

pm.test("Campo 'total' é 6300", () => {
    pm.expect(json.total).to.equal(6300);
});

pm.test("Campo 'status' é 'criado'", () => {
    pm.expect(json.status).to.equal("criado");
});
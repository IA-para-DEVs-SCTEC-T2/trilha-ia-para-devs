const request = require('supertest');
const app = require('../src/app');

describe('FeedbackHub API', () => {
  test('deve retornar status de saúde da API', async () => {
    const response = await request(app).get('/health');

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('status', 'ok');
    expect(response.body).toHaveProperty('service', 'feedbackhub-api');
  });

  test('deve listar feedbacks', async () => {
    const response = await request(app).get('/feedbacks');

    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
    expect(response.body.length).toBeGreaterThan(0);
  });

  test('deve filtrar feedbacks por status', async () => {
    const response = await request(app).get('/feedbacks?status=new');

    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);

    response.body.forEach((feedback) => {
      expect(feedback.status).toBe('new');
    });
  });

  test('não deve aceitar filtro com status inválido', async () => {
    const response = await request(app).get('/feedbacks?status=invalid');

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error', 'Status inválido');
  });

  test('deve filtrar feedbacks por categoria', async () => {
    const response = await request(app).get('/feedbacks?category=bug');

    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);

    response.body.forEach((feedback) => {
      expect(feedback.category).toBe('bug');
    });
  });

  test('não deve aceitar filtro com categoria inválida', async () => {
    const response = await request(app).get('/feedbacks?category=invalid');

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error', 'Categoria inválida');
  });

  test('deve criar um novo feedback', async () => {
    const response = await request(app)
      .post('/feedbacks')
      .send({
        userName: 'Diego Alves',
        email: 'diego@example.com',
        category: 'question',
        message: 'Como posso acompanhar o status do meu feedback?',
        priority: 'medium'
      });

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.userName).toBe('Diego Alves');
    expect(response.body.category).toBe('question');
    expect(response.body.status).toBe('new');
  });

  test('não deve criar feedback sem userName', async () => {
    const response = await request(app)
      .post('/feedbacks')
      .send({
        email: 'semnome@example.com',
        category: 'question',
        message: 'Mensagem sem nome de usuário.'
      });

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error', 'Campo obrigatório: userName');
  });

  test('não deve criar feedback com categoria inválida', async () => {
    const response = await request(app)
      .post('/feedbacks')
      .send({
        userName: 'Usuário Teste',
        email: 'teste@example.com',
        category: 'other',
        message: 'Mensagem com categoria inválida.'
      });

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error', 'Categoria inválida');
  });

  test('deve consultar feedback por id', async () => {
    const response = await request(app).get('/feedbacks/1');

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('id', 1);
    expect(response.body).toHaveProperty('message');
  });

  test('deve retornar 404 para feedback inexistente', async () => {
    const response = await request(app).get('/feedbacks/999');

    expect(response.status).toBe(404);
    expect(response.body).toHaveProperty('error', 'Feedback não encontrado');
  });

  test('deve atualizar status de um feedback', async () => {
    const response = await request(app)
      .patch('/feedbacks/1/status')
      .send({
        status: 'in_review'
      });

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('status', 'in_review');
  });

  test('não deve atualizar feedback com status inválido', async () => {
    const response = await request(app)
      .patch('/feedbacks/1/status')
      .send({
        status: 'done'
      });

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error', 'Status inválido');
  });

  test('deve registrar resposta para um feedback', async () => {
    const response = await request(app)
      .post('/feedbacks/1/replies')
      .send({
        responderName: 'Equipe Produto',
        message: 'Obrigado pelo feedback. Essa sugestão será avaliada.'
      });

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.feedbackId).toBe(1);
    expect(response.body.responderName).toBe('Equipe Produto');
  });

  test('não deve registrar resposta sem mensagem', async () => {
    const response = await request(app)
      .post('/feedbacks/1/replies')
      .send({
        responderName: 'Equipe Produto'
      });

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error', 'Campo obrigatório: message');
  });

  test('deve listar respostas de um feedback', async () => {
    const response = await request(app).get('/feedbacks/3/replies');

    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });

  test('deve retornar métricas gerais', async () => {
    const response = await request(app).get('/metrics');

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('totalFeedbacks');
    expect(response.body).toHaveProperty('totalReplies');
    expect(response.body).toHaveProperty('feedbacksByStatus');
    expect(response.body).toHaveProperty('feedbacksByCategory');
  });
});
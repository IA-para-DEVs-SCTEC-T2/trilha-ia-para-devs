const express = require('express');

const app = express();

app.use(express.json());

let nextFeedbackId = 4;
let nextReplyId = 2;

const allowedStatuses = ['new', 'in_review', 'answered', 'archived'];
const allowedCategories = ['bug', 'suggestion', 'compliment', 'question'];

const feedbacks = [
  {
    id: 1,
    userName: 'Ana Souza',
    email: 'ana@example.com',
    category: 'suggestion',
    message: 'Seria interessante ter um modo escuro na aplicação.',
    status: 'new',
    priority: 'medium',
    createdAt: '2026-05-01T10:00:00.000Z'
  },
  {
    id: 2,
    userName: 'Bruno Lima',
    email: 'bruno@example.com',
    category: 'bug',
    message: 'O botão de salvar não funciona quando o formulário está muito longo.',
    status: 'in_review',
    priority: 'high',
    createdAt: '2026-05-02T14:30:00.000Z'
  },
  {
    id: 3,
    userName: 'Carla Mendes',
    email: 'carla@example.com',
    category: 'compliment',
    message: 'A nova interface ficou muito mais simples de usar.',
    status: 'answered',
    priority: 'low',
    createdAt: '2026-05-03T09:15:00.000Z'
  }
];

const replies = [
  {
    id: 1,
    feedbackId: 3,
    responderName: 'Equipe Produto',
    message: 'Obrigado pelo retorno. Ficamos felizes que a nova interface tenha ajudado.',
    createdAt: '2026-05-04T11:00:00.000Z'
  }
];

function isNonEmptyString(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

function findFeedbackById(id) {
  return feedbacks.find((feedback) => feedback.id === Number(id));
}

app.get('/health', (req, res) => {
  return res.status(200).json({
    status: 'ok',
    service: 'feedbackhub-api'
  });
});

app.get('/feedbacks', (req, res) => {
  const { status, category } = req.query;

  if (status && !allowedStatuses.includes(status)) {
    return res.status(400).json({
      error: 'Status inválido'
    });
  }

  if (category && !allowedCategories.includes(category)) {
    return res.status(400).json({
      error: 'Categoria inválida'
    });
  }

  let filteredFeedbacks = feedbacks;

  if (status) {
    filteredFeedbacks = filteredFeedbacks.filter(
      (feedback) => feedback.status === status
    );
  }

  if (category) {
    filteredFeedbacks = filteredFeedbacks.filter(
      (feedback) => feedback.category === category
    );
  }

  return res.status(200).json(filteredFeedbacks);
});

app.post('/feedbacks', (req, res) => {
  const { userName, email, category, message, priority } = req.body;

  if (!isNonEmptyString(userName)) {
    return res.status(400).json({
      error: 'Campo obrigatório: userName'
    });
  }

  if (!isNonEmptyString(email)) {
    return res.status(400).json({
      error: 'Campo obrigatório: email'
    });
  }

  if (!allowedCategories.includes(category)) {
    return res.status(400).json({
      error: 'Categoria inválida'
    });
  }

  if (!isNonEmptyString(message)) {
    return res.status(400).json({
      error: 'Campo obrigatório: message'
    });
  }

  const newFeedback = {
    id: nextFeedbackId,
    userName,
    email,
    category,
    message,
    status: 'new',
    priority: priority || 'medium',
    createdAt: new Date().toISOString()
  };

  nextFeedbackId += 1;
  feedbacks.push(newFeedback);

  return res.status(201).json(newFeedback);
});

app.get('/feedbacks/:id', (req, res) => {
  const feedback = findFeedbackById(req.params.id);

  if (!feedback) {
    return res.status(404).json({
      error: 'Feedback não encontrado'
    });
  }

  return res.status(200).json(feedback);
});

app.patch('/feedbacks/:id/status', (req, res) => {
  const feedback = findFeedbackById(req.params.id);

  if (!feedback) {
    return res.status(404).json({
      error: 'Feedback não encontrado'
    });
  }

  const { status } = req.body;

  if (!allowedStatuses.includes(status)) {
    return res.status(400).json({
      error: 'Status inválido'
    });
  }

  feedback.status = status;

  return res.status(200).json(feedback);
});

app.post('/feedbacks/:id/replies', (req, res) => {
  const feedback = findFeedbackById(req.params.id);

  if (!feedback) {
    return res.status(404).json({
      error: 'Feedback não encontrado'
    });
  }

  const { responderName, message } = req.body;

  if (!isNonEmptyString(responderName)) {
    return res.status(400).json({
      error: 'Campo obrigatório: responderName'
    });
  }

  if (!isNonEmptyString(message)) {
    return res.status(400).json({
      error: 'Campo obrigatório: message'
    });
  }

  const newReply = {
    id: nextReplyId,
    feedbackId: feedback.id,
    responderName,
    message,
    createdAt: new Date().toISOString()
  };

  nextReplyId += 1;
  replies.push(newReply);

  feedback.status = 'answered';

  return res.status(201).json(newReply);
});

app.get('/feedbacks/:id/replies', (req, res) => {
  const feedback = findFeedbackById(req.params.id);

  if (!feedback) {
    return res.status(404).json({
      error: 'Feedback não encontrado'
    });
  }

  const feedbackReplies = replies.filter(
    (reply) => reply.feedbackId === feedback.id
  );

  return res.status(200).json(feedbackReplies);
});

app.get('/metrics', (req, res) => {
  const metrics = {
    totalFeedbacks: feedbacks.length,
    totalReplies: replies.length,
    feedbacksByStatus: allowedStatuses.reduce((accumulator, status) => {
      accumulator[status] = feedbacks.filter(
        (feedback) => feedback.status === status
      ).length;

      return accumulator;
    }, {}),
    feedbacksByCategory: allowedCategories.reduce((accumulator, category) => {
      accumulator[category] = feedbacks.filter(
        (feedback) => feedback.category === category
      ).length;

      return accumulator;
    }, {})
  };

  return res.status(200).json(metrics);
});

module.exports = app;
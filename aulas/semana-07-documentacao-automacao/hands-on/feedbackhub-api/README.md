# FeedbackHub API

API demonstrativa para coleta e gestão de feedbacks de usuários.

Esta aplicação é usada em aula para demonstrar:

- testes automatizados;
- documentação técnica;
- validação de documentação;
- pipelines com GitHub Actions;
- deploy simulado.

## Tecnologias

- Node.js
- Express
- Jest
- Supertest
- GitHub Actions

## Como instalar

```bash
npm install
```

## Como executar

```bash
npm start
```

## Como testar

```bash
npm test
```

## Endpoints principais

- `GET /health`
- `GET /feedbacks`
- `POST /feedbacks`
- `GET /feedbacks/:id`
- `PATCH /feedbacks/:id/status`
- `POST /feedbacks/:id/replies`
- `GET /feedbacks/:id/replies`
- `GET /metrics`
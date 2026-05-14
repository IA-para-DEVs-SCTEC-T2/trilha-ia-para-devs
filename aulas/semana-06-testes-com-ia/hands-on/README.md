# Hands-on - Semana 06

Esta pasta contem os codigos demonstrados pelo professor durante a aula de testes com IA.

## Diferenca entre hands-on e desafio

| Hands-on | Desafio |
|----------|---------|
| Codigo demonstrado pelo professor em aula | Exercicio para o aluno resolver |
| Serve como referencia e modelo | Deve ser entregue pelo aluno |
| Nao e uma entrega do aluno | E uma entrega avaliada |
| Pode ser executado para aprendizado | Deve ser adaptado e expandido |

## Exemplos disponíveis

| Pasta | Descricao |
|-------|-----------|
| `01-testes-unitarios/` | Testes unitarios com pytest (desconto, frete, senha, chamado) |
| `02-testes-e2e/` | Testes E2E com Playwright (login, fluxo de compra) |
| `03-testes-api/` | Testes de API com Postman |

## Como executar os exemplos

### Testes unitarios (pytest)

```bash
cd hands-on/01-testes-unitarios
pip install pytest
pytest -v
```

### Testes E2E (Playwright)

```bash
cd hands-on/02-testes-e2e
pip install playwright pytest-playwright
playwright install
pytest -v
```

### Testes de API (Postman)

Importe a colecao disponivel em `03-testes-api/api-postman/` no Postman e execute as requisicoes.

## Como usar como referencia

- Leia o codigo dos testes para entender a estrutura.
- Observe como os cenarios sao nomeados.
- Veja como as assertivas sao escritas.
- Use como modelo para os seus proprios testes nos desafios e no mini-projeto.

## Aviso importante

Os codigos desta pasta sao exemplos guiados pelo professor. Eles nao devem ser copiados diretamente como entrega. Use-os como referencia para desenvolver sua propria solucao.

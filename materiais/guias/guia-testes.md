# Guia de Testes

## Tipos de teste

### Teste unitario

Testa uma funcao ou metodo isolado, sem dependencias externas.

- Rapido de executar.
- Facil de depurar.
- Nao depende de banco de dados, rede ou outros servicos.
- Ferramenta: pytest (Python), Jest (JavaScript).

### Teste de API

Testa endpoints HTTP verificando status code, estrutura da resposta e regras de negocio.

- Requer o servidor em execucao ou um mock.
- Verifica a integracao entre frontend e backend.
- Ferramenta: Postman, pytest + requests.

### Teste E2E (End-to-End)

Testa fluxos completos simulando a interacao do usuario no navegador ou no app.

- Mais lento e mais fragil que testes unitarios.
- Verifica a experiencia real do usuario.
- Ferramenta: Playwright, Cypress.

## Tipos de cenario

### Cenario positivo

Testa o fluxo esperado com dados validos.

Exemplo: login com email e senha corretos retorna token.

### Cenario negativo

Testa o comportamento com dados invalidos ou ausentes.

Exemplo: login com senha incorreta retorna erro 401.

### Valor limite

Testa os extremos do dominio de entrada.

Exemplo: senha com exatamente 8 caracteres (minimo permitido) deve ser aceita; senha com 7 caracteres deve ser rejeitada.

### Edge case

Testa situacoes incomuns ou inesperadas.

Exemplo: email com caracteres especiais validos (`usuario+tag@dominio.com`).

## Boas praticas de nomeacao

Use nomes que descrevam o que o teste verifica:

```
test_{funcao}_{cenario}_{resultado_esperado}
```

Exemplos:

```python
# Ruim
def test_login():
    ...

# Bom
def test_login_com_credenciais_validas_retorna_token():
    ...

def test_login_com_senha_incorreta_retorna_erro_401():
    ...

def test_login_com_email_vazio_levanta_validation_error():
    ...
```

## Estrutura de um teste unitario com pytest

```python
def test_calcular_frete_com_valores_validos_retorna_valor_correto():
    # Arrange: prepara os dados
    peso = 2.0
    distancia = 10.0

    # Act: executa a funcao
    resultado = calcular_frete(peso, distancia)

    # Assert: verifica o resultado
    assert resultado == 7.0
```

## Cobertura de testes

Para verificar a cobertura com pytest:

```bash
pytest --cov=. --cov-report=term-missing
```

Cobertura alta nao garante qualidade. Prefira testes que verificam comportamento real a testes que apenas aumentam o percentual de cobertura.

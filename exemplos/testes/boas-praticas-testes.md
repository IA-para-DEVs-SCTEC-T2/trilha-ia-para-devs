# Boas Praticas de Testes

## Nomeacao de testes

Use nomes que descrevam o que o teste verifica, nao como ele funciona.

```python
# Ruim
def test_login():
    ...

# Bom
def test_login_com_credenciais_validas_retorna_token():
    ...

def test_login_com_senha_incorreta_retorna_erro_401():
    ...
```

Formato sugerido: `test_{funcao}_{cenario}_{resultado_esperado}`

## Um teste, uma assertiva

Cada teste deve verificar uma unica coisa. Testes com multiplas assertivas independentes dificultam a identificacao do problema quando falham.

```python
# Ruim: duas verificacoes independentes no mesmo teste
def test_login():
    response = login("email@test.com", "senha123")
    assert response.status_code == 200
    assert response.json()["user"]["email"] == "email@test.com"

# Bom: separado
def test_login_retorna_status_200():
    response = login("email@test.com", "senha123")
    assert response.status_code == 200

def test_login_retorna_email_do_usuario():
    response = login("email@test.com", "senha123")
    assert response.json()["user"]["email"] == "email@test.com"
```

## Cobertura de cenarios

Para cada funcionalidade, cubra:

| Tipo | Descricao | Exemplo |
|------|-----------|---------|
| Positivo | Fluxo esperado com dados validos | Login com email e senha corretos |
| Negativo | Dados invalidos ou ausentes | Login com senha errada |
| Limite | Extremos do dominio de entrada | Senha com exatamente 8 caracteres |
| Edge case | Situacoes incomuns | Email com caracteres especiais validos |

## Isolamento

Testes unitarios nao devem depender de banco de dados, rede ou outros servicos externos. Use mocks quando necessario.

## Independencia

Cada teste deve poder ser executado de forma independente, em qualquer ordem. Nao crie dependencias entre testes.

## Arrange, Act, Assert

Estruture os testes em tres partes:

```python
def test_calcular_frete_com_valores_validos():
    # Arrange: prepara os dados
    peso = 2.0
    distancia = 10.0

    # Act: executa a funcao
    resultado = calcular_frete(peso, distancia)

    # Assert: verifica o resultado
    assert resultado == 7.0
```

## Nao teste o que voce nao controla

Nao escreva testes que dependem de dados externos, horario do sistema ou comportamento de APIs de terceiros sem mockar essas dependencias.

## Evidencias

Sempre inclua evidencias de execucao nas entregas: print do terminal com os testes passando ou arquivo de log gerado pelo pytest.

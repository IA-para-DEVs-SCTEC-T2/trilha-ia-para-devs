import pytest
from app import app, recados, resetar_recados, RECADOS_INICIAIS


@pytest.fixture(autouse=True)
def restaurar_recados():
    resetar_recados()
    yield
    resetar_recados()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# Cenário 1 — POST com dados válidos → 201
def test_criar_recado_sucesso(client):
    resp = client.post("/recados", json={"autor": "Ana", "mensagem": "Olá mundo"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert "id" in data
    assert data["autor"] == "Ana"
    assert data["mensagem"] == "Olá mundo"
    assert data["lido"] is False


# Garante que lido=true no input é ignorado
def test_criar_recado_lido_ignorado(client):
    resp = client.post("/recados", json={"autor": "Bob", "mensagem": "Teste", "lido": True})
    assert resp.status_code == 201
    assert resp.get_json()["lido"] is False


# Cenário 2 — GET → 200, lista inclui os recados mockados por default
def test_listar_recados(client):
    resp = client.get("/recados")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == len(RECADOS_INICIAIS)
    for item in data:
        assert "id" in item
        assert "autor" in item
        assert "mensagem" in item
        assert "lido" in item


def test_listar_recados_inclui_novo(client):
    client.post("/recados", json={"autor": "Delta", "mensagem": "Nova mensagem"})
    resp = client.get("/recados")
    assert resp.status_code == 200
    assert len(resp.get_json()) == len(RECADOS_INICIAIS) + 1


# Cenário 3 — POST sem mensagem → 400 com campo error
def test_criar_recado_sem_mensagem(client):
    resp = client.post("/recados", json={"autor": "Ana"})
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_criar_recado_sem_autor(client):
    resp = client.post("/recados", json={"mensagem": "Olá"})
    assert resp.status_code == 400
    assert "error" in resp.get_json()

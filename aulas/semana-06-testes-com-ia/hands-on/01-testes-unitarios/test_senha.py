from senha import validar_senha


def test_senha_valida():
    assert validar_senha("Senha123") is True

def test_senha_valida_com_caracteres_especiais():
    assert validar_senha("Senha@123") is True


# Senha curta
def test_senha_invalida_menos_de_8_caracteres():
    assert validar_senha("Sen1") is False

def test_senha_invalida_com_7_caracteres():
    assert validar_senha("Senha12") is False


# Sem letra maiúscula
def test_senha_invalida_sem_maiuscula():
    assert validar_senha("senha123") is False


# Sem número
def test_senha_invalida_sem_numero():
    assert validar_senha("Abcdefgh") is False


# Edge cases
def test_senha_invalida_vazia():
    assert validar_senha("") is False

def test_senha_valida_exatamente_8_caracteres():
    assert validar_senha("Senha12!") is True

def test_senha_invalida_apenas_maiusculas():
    assert validar_senha("ABCDEFGH") is False

def test_senha_invalida_apenas_numeros():
    # BUG: função retorna True para senha só com números — isalpha() e islower() não detectam esse caso
    assert validar_senha("12345678") is False  # comportamento atual (incorreto)

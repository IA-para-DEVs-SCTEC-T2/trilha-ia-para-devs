from acesso import pode_acessar


def test_admin_nao_bloqueado_acessa():
    assert pode_acessar(ativo=False, bloqueado=False, admin=True) is True


def test_usuario_ativo_nao_bloqueado_acessa():
    assert pode_acessar(ativo=True, bloqueado=False, admin=False) is True
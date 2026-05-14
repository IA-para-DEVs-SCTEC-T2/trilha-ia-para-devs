from chamado import classificar_chamado


# Regra: sem_sinal sempre retorna alta, independente do tipo de cliente
def test_sem_sinal_cliente_comum_retorna_alta():
    assert classificar_chamado("sem_sinal", False) == "alta"

def test_sem_sinal_cliente_premium_retorna_alta():
    assert classificar_chamado("sem_sinal", True) == "alta"


# Regra: cobrança + cliente premium retorna alta
def test_cobranca_cliente_premium_retorna_alta():
    assert classificar_chamado("cobranca", True) == "alta"


# Regra: cobrança + cliente comum retorna media
def test_cobranca_cliente_comum_retorna_media():
    assert classificar_chamado("cobranca", False) == "media"


# Regra: demais tipos retornam baixa
def test_tipo_desconhecido_retorna_baixa():
    assert classificar_chamado("outro", False) == "baixa"

def test_tipo_desconhecido_cliente_premium_retorna_baixa():
    # premium não eleva prioridade para tipos que não sejam cobranca
    assert classificar_chamado("outro", True) == "baixa"


# Edge cases
def test_string_vazia_retorna_baixa():
    assert classificar_chamado("", False) == "baixa"

def test_tipo_none_retorna_baixa():
    assert classificar_chamado(None, False) == "baixa"

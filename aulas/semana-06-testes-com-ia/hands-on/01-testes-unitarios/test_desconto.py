import pytest
from desconto import calcular_desconto


# Regra: valores negativos devem gerar ValueError
def test_valor_negativo_levanta_excecao():
    with pytest.raises(ValueError):
        calcular_desconto(-1, False)

def test_valor_negativo_com_cliente_vip_levanta_excecao():
    with pytest.raises(ValueError):
        calcular_desconto(-100, True)


# Regra: clientes VIP têm prioridade e recebem 15% de desconto
def test_cliente_vip_recebe_desconto_15_porcento():
    assert calcular_desconto(100, True) == 85.0

def test_cliente_vip_acima_300_ainda_usa_desconto_vip():
    # VIP tem prioridade sobre o desconto por valor
    assert calcular_desconto(300, True) == 255.0

def test_cliente_vip_com_valor_zero():
    assert calcular_desconto(0, True) == 0.0


# Regra: compras >= R$300 recebem 10% de desconto (não VIP)
def test_compra_exatamente_300_recebe_desconto_10_porcento():
    assert calcular_desconto(300, False) == 270.0

def test_compra_acima_300_recebe_desconto_10_porcento():
    assert calcular_desconto(500, False) == 450.0


# Regra: compras abaixo de R$300 sem VIP não recebem desconto
def test_compra_abaixo_300_sem_vip_sem_desconto():
    assert calcular_desconto(299, False) == 299

def test_compra_zero_sem_vip_sem_desconto():
    assert calcular_desconto(0, False) == 0

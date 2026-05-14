def calcular_desconto(valor_compra, cliente_vip):

    if valor_compra < 0:
        raise ValueError("Valor inválido")

    if cliente_vip:
        return valor_compra * 0.85

    if valor_compra >= 300:
        return valor_compra * 0.90

    return valor_compra
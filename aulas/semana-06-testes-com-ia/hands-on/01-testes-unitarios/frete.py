
def calcular_frete(valor_compra, distancia_km):
    if not isinstance(valor_compra, (int, float)):
        raise TypeError("valor_compra deve ser numérico")

    if not isinstance(distancia_km, (int, float)):
        raise TypeError("distancia_km deve ser numérico")

    if valor_compra < 0 or distancia_km < 0:
        raise ValueError("Valores inválidos")

    if valor_compra >= 200:
        return 0

    if distancia_km <= 10:
        return 10

    return 20
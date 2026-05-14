# Exemplo de Teste Unitario com Python e pytest

## Codigo sendo testado

```python
# frete.py
def calcular_frete(peso_kg: float, distancia_km: float) -> float:
    if peso_kg <= 0 or distancia_km <= 0:
        raise ValueError("Peso e distancia devem ser positivos")
    taxa_base = 5.0
    taxa_peso = peso_kg * 0.5
    taxa_distancia = distancia_km * 0.1
    return taxa_base + taxa_peso + taxa_distancia
```

## Testes

```python
# test_frete.py
import pytest
from frete import calcular_frete


# Cenario positivo
def test_calcular_frete_com_valores_validos_retorna_valor_correto():
    resultado = calcular_frete(peso_kg=2.0, distancia_km=10.0)
    # taxa_base=5.0 + taxa_peso=1.0 + taxa_distancia=1.0 = 7.0
    assert resultado == 7.0


# Cenario negativo: peso zero
def test_calcular_frete_com_peso_zero_levanta_value_error():
    with pytest.raises(ValueError):
        calcular_frete(peso_kg=0, distancia_km=10.0)


# Cenario negativo: distancia negativa
def test_calcular_frete_com_distancia_negativa_levanta_value_error():
    with pytest.raises(ValueError):
        calcular_frete(peso_kg=2.0, distancia_km=-5.0)


# Valor limite: peso minimo valido
def test_calcular_frete_com_peso_minimo_valido_retorna_valor_correto():
    resultado = calcular_frete(peso_kg=0.001, distancia_km=1.0)
    assert resultado > 5.0


# Edge case: valores muito grandes
def test_calcular_frete_com_valores_muito_grandes_retorna_valor_positivo():
    resultado = calcular_frete(peso_kg=1000.0, distancia_km=10000.0)
    assert resultado > 0
```

## Como executar

```bash
pip install pytest
pytest test_frete.py -v
```

## Saida esperada

```
test_frete.py::test_calcular_frete_com_valores_validos_retorna_valor_correto PASSED
test_frete.py::test_calcular_frete_com_peso_zero_levanta_value_error PASSED
test_frete.py::test_calcular_frete_com_distancia_negativa_levanta_value_error PASSED
test_frete.py::test_calcular_frete_com_peso_minimo_valido_retorna_valor_correto PASSED
test_frete.py::test_calcular_frete_com_valores_muito_grandes_retorna_valor_positivo PASSED
```

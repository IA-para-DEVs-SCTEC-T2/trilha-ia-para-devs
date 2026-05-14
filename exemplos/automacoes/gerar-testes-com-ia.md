# Gerar Testes com IA

## Objetivo

Usar IA para gerar testes automatizados a partir de uma funcao ou modulo existente, acelerando a cobertura de testes sem abrir mao da qualidade.

## Quando usar

- Para gerar um conjunto inicial de testes para uma funcao ja implementada.
- Para identificar cenarios de teste que voce pode ter esquecido.
- Para acelerar a escrita de testes repetitivos.

## Quando evitar

- Quando os testes gerados nao serao revisados antes de serem adicionados ao projeto.
- Quando a logica de negocio e complexa e a IA nao tem contexto suficiente.

## Fluxo passo a passo

1. Selecione a funcao ou modulo que deseja testar.
2. Envie o codigo e o contexto para a IA.
3. Revise os testes gerados.
4. Execute os testes e verifique se passam.
5. Ajuste os testes que nao estiverem corretos.
6. Adicione cenarios que a IA nao cobriu.

## Exemplo de prompt

```
Contexto:
Estou desenvolvendo o modulo de calculo de frete do Shop4u em Python.

Objetivo:
Gere testes unitarios com pytest para a funcao abaixo.

Entrada esperada:
```python
def calcular_frete(peso_kg: float, distancia_km: float) -> float:
    if peso_kg <= 0 or distancia_km <= 0:
        raise ValueError("Peso e distancia devem ser positivos")
    taxa_base = 5.0
    taxa_peso = peso_kg * 0.5
    taxa_distancia = distancia_km * 0.1
    return taxa_base + taxa_peso + taxa_distancia
```

Restricoes:
- Use pytest.
- Cubra: cenario positivo, peso zero, distancia zero, valores limite.
- Nomes de testes descritivos.
- Sem mocks desnecessarios.

Formato de saida:
Arquivo Python com os testes prontos para execucao.
```

## Cuidados

- Execute os testes gerados antes de aceita-los.
- Verifique se os valores esperados nas assertivas estao corretos.
- Adicione cenarios de edge case que a IA pode ter ignorado.
- Nao aceite testes que apenas verificam `assert True` sem logica real.

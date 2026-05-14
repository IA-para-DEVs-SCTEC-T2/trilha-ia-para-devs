# Prompt: Gerar Testes

## Quando usar

Para gerar testes automatizados para uma funcao ou modulo existente.

## Prompt: Testes unitarios com pytest

```
Contexto:
Estou desenvolvendo o modulo de calculo de frete do Shop4u em Python.

Objetivo:
Gere testes unitarios com pytest para a funcao abaixo.

Entrada esperada:
[Cole a funcao aqui]

Restricoes:
- Use pytest.
- Cubra: cenario positivo (valores validos), cenarios negativos (valores invalidos), valores limite e pelo menos um edge case.
- Use nomes descritivos no formato: test_{funcao}_{cenario}_{resultado_esperado}.
- Nao use mocks desnecessarios.
- Cada teste deve verificar uma unica coisa.

Formato de saida:
Arquivo Python com os testes prontos para execucao com pytest.
```

## Prompt: Testes de API com Postman

```
Contexto:
Estou testando o endpoint de busca de produtos do Shop4u.
Endpoint: GET /products?q={termo}
Retorno esperado: array de produtos com id, name, price e category.

Objetivo:
Gere scripts de teste para a aba Tests do Postman cobrindo os cenarios abaixo.

Entrada esperada:
Cenarios:
- Busca com termo que retorna resultados
- Busca com termo sem resultados
- Busca sem parametro q

Restricoes:
- Use pm.test() para cada assertiva.
- Verifique status code, estrutura da resposta e tipos dos campos.
- Nao use bibliotecas externas.

Formato de saida:
Scripts JavaScript prontos para colar na aba Tests do Postman.
```

## Revisao humana necessaria

- Execute os testes gerados antes de aceita-los.
- Verifique se os valores esperados nas assertivas estao corretos.
- Adicione cenarios que a IA pode ter ignorado.
- Nao aceite testes que apenas verificam `assert True` sem logica real.

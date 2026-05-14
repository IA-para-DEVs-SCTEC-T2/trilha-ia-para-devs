# Prompt: Revisar Codigo

## Quando usar

Para obter uma revisao critica de um trecho de codigo antes de abrir um Pull Request ou entregar uma atividade.

## Prompt

```
Contexto:
Estou desenvolvendo o modulo de autenticacao do Shop4u em Node.js com Express.
As convencoes do projeto estao em CONTRIBUTING.md: funcoes com nomes descritivos, tratamento de erros com try/catch, sem console.log em producao.

Objetivo:
Revise o codigo abaixo e aponte problemas.

Entrada esperada:
[Cole o codigo aqui]

Restricoes:
- Aponte apenas problemas reais, nao sugestoes esteticas desnecessarias.
- Para cada problema, informe: o que esta errado, por que e um problema e como corrigir.
- Verifique: logica incorreta, erros nao tratados, seguranca, performance e convencoes do projeto.
- Nao sugira refatoracoes que nao sejam necessarias para a corretude.

Formato de saida:
Lista numerada de problemas encontrados. Para cada um:
1. Descricao do problema
2. Linha ou funcao afetada
3. Sugestao de correcao
```

## Revisao humana necessaria

- Avalie cada problema apontado antes de aplicar a correcao.
- A IA pode apontar falsos positivos ou sugerir correcoes incorretas.
- Decisoes de arquitetura devem ser validadas com o time, nao apenas com a IA.
- Nao envie codigo com tokens, senhas ou dados sensiveis para servicos externos.

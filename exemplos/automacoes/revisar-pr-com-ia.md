# Revisar Pull Request com IA

## Objetivo

Usar IA para apoiar a revisao de Pull Requests, identificando problemas de codigo, documentacao ausente e melhorias possiveis.

## Quando usar

- Para uma primeira passagem antes da revisao humana.
- Para identificar padroes de codigo que nao seguem as convencoes do projeto.
- Para verificar se a documentacao foi atualizada junto com o codigo.

## Quando evitar

- Como substituto da revisao humana.
- Para decisoes de arquitetura ou de negocio.
- Quando o codigo contem informacoes sensiveis que nao devem ser enviadas para servicos externos.

## Fluxo passo a passo

1. Obtenha o diff do Pull Request.
2. Envie o diff e o contexto do projeto para a IA.
3. Analise as sugestoes recebidas.
4. Aplique as que fazem sentido e descarte as que nao se aplicam.
5. Documente as decisoes tomadas.

## Obter o diff de um PR via GitHub CLI

```bash
gh pr diff 42
```

## Exemplo de prompt

```
Contexto:
Estou revisando um Pull Request do projeto Shop4u, um e-commerce mobile em React Native.
As convencoes do projeto estao em CONTRIBUTING.md.

Objetivo:
Revise o diff abaixo e aponte:
1. Problemas de logica ou bugs potenciais.
2. Codigo que nao segue as convencoes do projeto.
3. Testes ausentes para o codigo adicionado.
4. Documentacao que deveria ter sido atualizada.

Entrada esperada:
[cole o diff aqui]

Restricoes:
- Seja objetivo e especifico.
- Aponte a linha ou funcao com o problema.
- Nao sugira refatoracoes que nao sejam necessarias para a corretude do codigo.

Formato de saida:
Lista de problemas encontrados com justificativa e sugestao de correcao.
```

## Cuidados

- Nao envie codigo com tokens, senhas ou dados sensiveis para servicos de IA externos.
- A IA pode sugerir alteracoes incorretas. Sempre valide antes de aplicar.
- Use a revisao da IA como complemento, nao como substituto da revisao humana.

# Prompt: Documentacao Tecnica

## Quando usar

Para gerar documentacao tecnica de um modulo, servico ou componente a partir do codigo ou de uma descricao.

## Prompt

```
Contexto:
Estou documentando o modulo de busca de produtos do Shop4u.
O modulo e implementado em JavaScript e expoe uma funcao de busca que filtra produtos por nome e categoria.

Objetivo:
Gere a documentacao tecnica do modulo abaixo.

Entrada esperada:
[Cole o codigo do modulo aqui]

Restricoes:
- Documente: proposito do modulo, funcoes exportadas, parametros, retorno, exemplos de uso e erros possiveis.
- Use linguagem tecnica e objetiva.
- Nao repita o codigo, apenas documente o comportamento.
- Nao invente comportamentos que nao estao no codigo.
- Nao use emojis.

Formato de saida:
Documento Markdown com secoes: Descricao, Funcoes, Exemplos de uso, Erros e excecoes.
```

## Revisao humana necessaria

- Verifique se os parametros e retornos documentados correspondem ao codigo real.
- Confirme os exemplos de uso executando-os.
- Ajuste a descricao para refletir o contexto real do projeto.
- Adicione informacoes de contexto que a IA nao tinha acesso (ex: dependencias externas, configuracoes necessarias).

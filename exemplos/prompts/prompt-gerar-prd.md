# Prompt: Gerar PRD

## Quando usar

Para gerar um Product Requirements Document a partir de uma descricao inicial do produto ou de uma ata de reuniao.

## Prompt

```
Contexto:
Estou desenvolvendo um aplicativo mobile de e-commerce chamado Shop4u.
O produto foi discutido em uma reuniao de kickoff e as principais necessidades foram levantadas.

Objetivo:
Gere um PRD (Product Requirements Document) completo para o Shop4u com base nas informacoes abaixo.

Entrada esperada:
[Cole aqui a ata de reuniao ou a descricao do produto]

Restricoes:
- Nao invente funcionalidades que nao foram mencionadas.
- Use linguagem tecnica e objetiva.
- Organize em secoes: Visao geral, Objetivo, Publico-alvo, Funcionalidades principais, Funcionalidades fora do escopo, Criterios de sucesso, Restricoes tecnicas.
- Nao use emojis.
- Cada funcionalidade deve ter uma descricao de uma a tres frases.

Formato de saida:
Documento Markdown estruturado com titulos e subtitulos.
```

## Revisao humana necessaria

Apos gerar o PRD:

- Verifique se todas as funcionalidades mencionadas foram incluidas.
- Remova funcionalidades que a IA inventou sem base na entrada.
- Ajuste a linguagem para o contexto real do projeto.
- Valide os criterios de sucesso com o time ou professor.

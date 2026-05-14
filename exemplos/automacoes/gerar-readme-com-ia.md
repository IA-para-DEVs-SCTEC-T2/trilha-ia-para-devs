# Gerar README com IA

## Objetivo

Usar IA para gerar um README inicial completo para um projeto de software, acelerando a documentacao sem abrir mao da qualidade.

## Quando usar

- Ao iniciar um novo projeto e precisar de um README estruturado rapidamente.
- Para padronizar a documentacao de multiplos projetos.
- Para gerar um ponto de partida que sera revisado e personalizado.

## Quando evitar

- Quando o projeto tem caracteristicas muito especificas que a IA nao conhece.
- Quando o README sera publicado sem revisao humana.

## Fluxo passo a passo

1. Reuna as informacoes do projeto: nome, objetivo, tecnologias, como instalar, como usar.
2. Envie o prompt para a IA com essas informacoes.
3. Revise o resultado gerado.
4. Ajuste o que nao estiver correto ou completo.
5. Salve o arquivo como `README.md` na raiz do projeto.

## Exemplo de prompt

```
Contexto:
Estou desenvolvendo um aplicativo mobile de e-commerce chamado Shop4u.
O projeto usa React Native no frontend e Node.js com Express no backend.
O banco de dados e PostgreSQL.

Objetivo:
Gere um README.md completo para este projeto.

Entrada esperada:
- Nome do projeto: Shop4u
- Descricao: Aplicativo mobile de e-commerce com recomendacoes por IA
- Tecnologias: React Native, Node.js, Express, PostgreSQL
- Como instalar: npm install
- Como executar: npm start
- Como testar: npm test

Restricoes:
- Nao use emojis.
- Use Markdown bem organizado com titulos e subtitulos.
- Inclua secoes: Descricao, Tecnologias, Como instalar, Como executar, Como testar, Estrutura de pastas, Contribuicao.

Formato de saida:
Arquivo Markdown pronto para uso.
```

## Cuidados

- Revise todos os comandos gerados antes de publicar.
- Verifique se as versoes de dependencias estao corretas.
- Nao publique informacoes sensiveis (tokens, senhas, URLs internas).
- Adapte o conteudo ao contexto real do projeto.

# Prompt: Criar README

## Quando usar

Para gerar um README completo para um projeto de software a partir de uma descricao das tecnologias e funcionalidades.

## Prompt

```
Contexto:
Estou desenvolvendo o Shop4u, um aplicativo mobile de e-commerce com recomendacoes por IA.
Tecnologias: React Native (frontend), Node.js com Express (backend), PostgreSQL (banco de dados).

Objetivo:
Gere um README.md completo para o repositorio do projeto.

Entrada esperada:
- Nome: Shop4u
- Descricao: Aplicativo mobile de e-commerce com recomendacoes personalizadas por IA
- Funcionalidades: login, busca de produtos, carrinho, checkout, recomendacoes
- Como instalar: npm install (frontend e backend separados)
- Como executar: npm start
- Como testar: npm test
- Variaveis de ambiente necessarias: DATABASE_URL, JWT_SECRET, PORT

Restricoes:
- Nao use emojis.
- Use Markdown bem organizado.
- Inclua secoes: Descricao, Tecnologias, Pre-requisitos, Como instalar, Como executar, Como testar, Variaveis de ambiente, Estrutura de pastas, Contribuicao, Licenca.
- Para variaveis de ambiente, use nomes genericos como exemplo, nao valores reais.
- Nao invente comandos que nao foram informados.

Formato de saida:
Arquivo Markdown pronto para uso como README.md.
```

## Revisao humana necessaria

- Verifique se os comandos de instalacao e execucao estao corretos.
- Confirme a estrutura de pastas com a estrutura real do projeto.
- Remova ou ajuste secoes que nao se aplicam.
- Nao publique variaveis de ambiente reais no README.

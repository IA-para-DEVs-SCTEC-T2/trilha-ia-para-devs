# Diagramas

Esta pasta contem orientacoes e exemplos para os diagramas do mini-projeto.

## Arquivos disponíveis

| Arquivo | Descricao |
|---------|-----------|
| `diagrama-caso-de-uso.md` | Orientacoes e exemplo de diagrama de caso de uso |
| `diagrama-c4.md` | Orientacoes e exemplo de diagrama C4 |
| `fluxo-navegacao.md` | Orientacoes para fluxo de navegacao |
| `fluxo-compra.md` | Exemplo de fluxo de compra |

## Quando usar UML

Use UML quando precisar documentar casos de uso, sequencia de interacoes ou estrutura de entidades.

## Quando usar C4

Use C4 para documentar a arquitetura em niveis:

- Nivel 1 (Context): o sistema, seus usuarios e sistemas externos.
- Nivel 2 (Container): frontend, backend, banco de dados.
- Nivel 3 (Component): modulos internos de um container.

## Salvar imagens exportadas

Se exportar o diagrama como imagem, salve nesta pasta com nome descritivo:

```
diagramas/
├── caso-de-uso.png
├── c4-context.png
└── fluxo-compra.png
```

## Justificar decisoes

Para cada diagrama, inclua uma breve justificativa das decisoes tomadas: por que essa arquitetura, quais alternativas foram consideradas.

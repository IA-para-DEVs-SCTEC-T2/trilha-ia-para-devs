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

Use UML quando precisar documentar:

- Casos de uso (atores e funcionalidades).
- Sequencia de interacoes entre componentes.
- Estrutura de classes ou entidades.

## Quando usar C4

Use C4 quando precisar documentar a arquitetura do sistema em diferentes niveis de detalhe:

- Nivel 1 (Context): o sistema e seus usuarios e sistemas externos.
- Nivel 2 (Container): os principais componentes do sistema (frontend, backend, banco).
- Nivel 3 (Component): os modulos internos de um container.

## Salvar imagens exportadas

Se voce exportar o diagrama como imagem, salve na propria pasta `diagramas/` com nome descritivo:

```
diagramas/
├── caso-de-uso.png
├── c4-context.png
└── fluxo-compra.png
```

## Justificar decisoes arquiteturais

Para cada diagrama, inclua uma breve justificativa das decisoes tomadas. Exemplo: por que escolheu essa arquitetura, quais alternativas foram consideradas e por que foram descartadas.

# Guia de Markdown

## Titulos

```markdown
# Titulo nivel 1
## Titulo nivel 2
### Titulo nivel 3
#### Titulo nivel 4
```

## Listas

```markdown
# Lista nao ordenada
- Item 1
- Item 2
  - Subitem

# Lista ordenada
1. Primeiro
2. Segundo
3. Terceiro
```

## Links

```markdown
[Texto do link](https://exemplo.com)
[Link relativo](../outra-pasta/arquivo.md)
```

## Blocos de codigo

Inline: `` `codigo` ``

Bloco com linguagem:

````markdown
```python
def soma(a, b):
    return a + b
```
````

## Tabelas

```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Valor A  | Valor B  | Valor C  |
| Valor D  | Valor E  | Valor F  |
```

## Checklists

```markdown
- [x] Tarefa concluida
- [ ] Tarefa pendente
- [ ] Outra tarefa
```

## Negrito e italico

```markdown
**negrito**
*italico*
~~tachado~~
```

## Citacao

```markdown
> Texto em citacao
```

## Linha horizontal

```markdown
---
```

## Boas praticas

- Use titulos para organizar o conteudo hierarquicamente.
- Nao pule niveis de titulo (ex: de `#` direto para `###`).
- Use tabelas para comparacoes e listas de itens com multiplos atributos.
- Use blocos de codigo com a linguagem especificada para syntax highlighting.
- Mantenha linhas em branco entre secoes para melhor legibilidade.
- Nao use HTML desnecessario dentro de arquivos Markdown.

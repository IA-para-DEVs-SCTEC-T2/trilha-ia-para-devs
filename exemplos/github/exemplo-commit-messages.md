# Convencoes de Mensagens de Commit

Referencia para escrever mensagens de commit claras e padronizadas.

## Formato

```
tipo: descricao curta no imperativo
```

Opcionalmente, com escopo:

```
tipo(escopo): descricao curta no imperativo
```

## Tipos

| Tipo | Quando usar |
|------|-------------|
| `feat` | Nova funcionalidade |
| `fix` | Correcao de bug |
| `docs` | Alteracao em documentacao |
| `test` | Adicao ou correcao de testes |
| `refactor` | Refatoracao sem mudanca de comportamento |
| `chore` | Tarefas de manutencao (dependencias, configs) |
| `style` | Formatacao, espacos, ponto e virgula (sem logica) |
| `perf` | Melhoria de performance |

## Regras

- Use o imperativo: "adiciona", "corrige", "remove" (nao "adicionado", "corrigido").
- Primeira letra minuscula.
- Sem ponto final.
- Maximo de 72 caracteres na primeira linha.
- Seja especifico: descreva o que foi feito, nao o que voce fez.

## Exemplos corretos

```
feat: adiciona tela de login com validacao de campos
fix: corrige redirecionamento apos login bem-sucedido
docs: atualiza README com instrucoes de instalacao
test: adiciona testes unitarios para calculo de frete
refactor: extrai logica de validacao para funcao separada
chore: atualiza dependencias do projeto
feat(auth): adiciona suporte a login com Google
fix(cart): corrige calculo de total com desconto aplicado
```

## Exemplos incorretos

```
# Muito vago
fix: corrige bug

# Passado em vez de imperativo
feat: adicionei tela de login

# Com ponto final
docs: atualiza README.

# Muito longo
feat: adiciona a nova tela de login do usuario com validacao de todos os campos obrigatorios e integracao com o backend
```

## Commits atomicos

Cada commit deve representar uma unica alteracao logica. Evite commits que misturam multiplas mudancas nao relacionadas.

```
# Ruim: um commit com tudo
feat: adiciona login, corrige bug do carrinho e atualiza README

# Bom: commits separados
feat: adiciona tela de login
fix: corrige calculo de total no carrinho
docs: atualiza README com instrucoes de autenticacao
```

# Exemplo de Pull Request

Modelo de Pull Request com descricao, issue relacionada, instrucoes de teste e checklist.

## Estrutura

```markdown
## O que foi feito

[Descricao objetiva das alteracoes realizadas]

## Issue relacionada

Closes #[numero]

## Como testar

1. [Passo 1]
2. [Passo 2]
3. [Resultado esperado]

## Checklist

- [ ] Testes adicionados ou atualizados
- [ ] Documentacao atualizada
- [ ] Sem erros de lint
- [ ] Revisado localmente antes de abrir o PR
```

## Exemplo preenchido: Login

**Titulo:** feat: adiciona tela de login com validacao (#1)

```markdown
## O que foi feito

Implementacao da tela de login com validacao de campos e integracao com o endpoint de autenticacao.

Alteracoes:
- Tela de login com campos de email e senha
- Validacao de campos obrigatorios no frontend
- Integracao com endpoint POST /auth/login
- Armazenamento do token JWT no AsyncStorage
- Tratamento de erro 401 com mensagem ao usuario

## Issue relacionada

Closes #1

## Como testar

1. Acesse a tela de login
2. Informe email e senha validos (ex: usuario@shop4u.com / senha123)
3. Verifique o redirecionamento para a tela inicial
4. Tente login com senha incorreta e verifique a mensagem de erro
5. Tente login com campo vazio e verifique a mensagem de validacao

## Checklist

- [x] Testes unitarios adicionados para a funcao de autenticacao
- [x] Teste E2E adicionado para o fluxo de login
- [x] README atualizado com instrucoes de autenticacao
- [x] Sem erros de lint
- [x] Revisado localmente antes de abrir o PR
```

## Boas praticas

- Titulos concisos: `tipo: descricao curta (#numero-da-issue)`.
- Descricao clara do que foi feito, nao apenas "implementei a feature".
- Sempre referencie a Issue com `Closes #numero` para fechar automaticamente.
- Instrucoes de teste especificas o suficiente para qualquer revisor executar.
- Checklist honesto: nao marque o que nao foi feito.

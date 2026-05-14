# Orientacoes Gerais - Desafios de Testes

## Objetivo

Os desafios desta pasta tem como objetivo praticar a criacao, revisao e correcao de testes automatizados com apoio de IA.

## Antes de comecar

- Leia o enunciado completo do desafio antes de escrever qualquer codigo.
- Entenda o codigo base disponivel na pasta do desafio.
- Identifique quais funcionalidades precisam ser testadas.
- Planeje os cenarios de teste antes de implementa-los.

## Acesso ao codigo base

Cada desafio contem um codigo base na propria pasta. Nao e necessario clonar repositorios externos.

Para instalar dependencias (quando houver `requirements.txt`):

```bash
pip install -r requirements.txt
```

## O que os alunos devem fazer

- Criar testes para as funcionalidades indicadas no enunciado.
- Cobrir cenarios positivos, negativos, valores limite e edge cases.
- Revisar testes existentes e corrigir os que estiverem incorretos, quando solicitado.
- Registrar evidencias de execucao dos testes.

## Registro de prompts

Crie um arquivo `prompts-usados.md` na sua entrega com os prompts utilizados para gerar ou revisar testes com IA. Inclua:

- O prompt enviado.
- O resultado obtido.
- O que foi aceito, ajustado ou descartado.

## Boas praticas de nomeacao de testes

Use nomes descritivos que expliquem o que o teste verifica:

```python
# Ruim
def test_login():
    ...

# Bom
def test_login_com_credenciais_validas_retorna_sucesso():
    ...

def test_login_com_senha_incorreta_retorna_erro_401():
    ...

def test_login_com_email_vazio_retorna_erro_de_validacao():
    ...
```

## Tipos de cenarios

| Tipo | Descricao | Exemplo |
|------|-----------|---------|
| Positivo | Fluxo esperado com dados validos | Login com email e senha corretos |
| Negativo | Fluxo com dados invalidos ou ausentes | Login com senha errada |
| Limite | Valores nos extremos do dominio | Senha com exatamente 8 caracteres |
| Edge case | Situacoes incomuns ou inesperadas | Email com caracteres especiais |

## Execucao dos testes

Para testes com pytest:

```bash
pytest nome_do_arquivo_de_teste.py -v
```

Para ver a cobertura:

```bash
pytest --cov=. --cov-report=term-missing
```

# Prompts Utilizados — Geração de Testes das APIs

Registro dos prompts enviados ao Kiro (IA) para gerar as collections do Postman e os casos de teste das APIs de recados e tarefas.

---

## API de Recados

### Prompt 1 — Gerar a collection do Postman (API de Pedidos)

> Gere a collection pra mim do postman, para testar a api 02-api-pedidos-postman, baseado no arquivo app.py

**Contexto fornecido:** arquivo `app.py` da API de pedidos aberto no editor.  
**Resultado:** collection `api-pedidos.postman_collection.json` gerada com todos os endpoints e cenários de teste.

---

### Prompt 2 — Gerar a collection da API de Recados

> Gere a collection no postman para cobrir todos os casos de teste dessa aplicação. Não esqueça dos seguintes cenários de teste:
>
> Cenário 1:  
> POST /recados  
> Criar recado  
> Status 201  
> Validar: id, autor, mensagem, lido=false
>
> Cenário 2:  
> GET /recados  
> Listar recados  
> Status 200  
> Validar: lista e campos obrigatórios
>
> Cenário 3:  
> POST /recados  
> Erro sem mensagem  
> Status 400  
> Validar: campo error

**Contexto fornecido:** arquivo `app.py` da API de recados aberto no editor.  
**Resultado:** collection `api-recados.postman_collection.json` gerada com 9 casos de teste cobrindo os 3 cenários solicitados mais casos adicionais de validação.

---

### Prompt 3 — Documentar os casos de teste em Markdown

> Gere os casos de teste do postman da api recados, dentro de atividades\semana-06\grupo 6\arquivo testes-recados.md

**Contexto fornecido:** collection `api-recados.postman_collection.json`.  
**Resultado:** arquivo `testes-recados.md` criado com tabelas descritivas de cada caso de teste.

---

### Prompt 4 — Reescrever o arquivo com os scripts reais do Postman

> Os casos de testes devem ser os próprios scripts do postman que preciso que seja incluído no arquivo testes-recados.md. Reescreva ele

**Contexto fornecido:** arquivo `testes-recados.md` gerado no prompt anterior.  
**Resultado:** arquivo `testes-recados.md` reescrito com os scripts JavaScript reais (`pm.test`) de cada caso de teste, prontos para colar na aba Tests do Postman.

---

### Prompt 5 — Gerar arquivo de prompts

> Gere dentro da pasta um arquivo md com os prompts utilizados para gerar os testes da api.

**Contexto fornecido:** arquivo `testes-recados.md` aberto no editor.  
**Resultado:** arquivo `prompts-utilizados.md` criado com o registro de todos os prompts utilizados.

---

## API de Tarefas

### Prompt 6 — Executar a aplicação de tarefas

> Execute a aplicação aulas\semana-06-testes-com-ia\desafios\03-teste-api-tarefas-postman\app.py

**Contexto fornecido:** arquivo `app.py` da API de tarefas aberto no editor.  
**Resultado:** aplicação Flask iniciada em `http://localhost:3000`.

---

### Prompt 7 — Gerar scripts de teste e arquivo testes-tarefas.md

> Gere os scripts de teste do postman para os distintos cenários da api de tarefas e crie um arquivo md testes-tarefas dentro de atividades\semana-06\grupo 6, assim como fez para a aplicação de recados e atualize o arquivo prompts-utilizados.md

**Contexto fornecido:** arquivo `app.py` da API de tarefas aberto no editor.  
**Resultado:** arquivo `testes-tarefas.md` criado com 13 casos de teste cobrindo os cenários: criar tarefa, listar tarefas, buscar por ID, concluir tarefa e erros de validação. Arquivo `prompts-utilizados.md` atualizado.

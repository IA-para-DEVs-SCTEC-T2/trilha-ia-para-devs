# Guia de Uso de IA no Desenvolvimento

## Como usar IA para apoiar o desenvolvimento

A IA e uma ferramenta de apoio, nao um substituto para o raciocinio do desenvolvedor. Use-a para:

- Gerar um ponto de partida para artefatos (PRD, User Stories, testes, documentacao).
- Revisar codigo e identificar problemas potenciais.
- Explorar alternativas de implementacao.
- Acelerar tarefas repetitivas e previsíveis.

Nao use IA para:

- Tomar decisoes de arquitetura sem validacao humana.
- Publicar codigo ou documentacao sem revisao.
- Substituir o entendimento do problema de negocio.

## Como escrever bons prompts

Um bom prompt tem quatro elementos:

1. **Contexto**: quem voce e, qual e o projeto, qual e a stack.
2. **Objetivo**: o que voce quer que a IA produza.
3. **Restricoes**: o que nao deve ser feito, formato esperado, limites.
4. **Entrada**: os dados ou o codigo que a IA deve usar.

Exemplo de prompt estruturado:

```
Contexto:
Estou desenvolvendo o modulo de autenticacao do Shop4u em Node.js.

Objetivo:
Gere testes unitarios com Jest para a funcao validatePassword abaixo.

Entrada:
[cole a funcao aqui]

Restricoes:
- Use Jest.
- Cubra cenarios positivos, negativos e valores limite.
- Nomes de testes descritivos.
- Sem mocks desnecessarios.

Formato de saida:
Arquivo JavaScript pronto para execucao.
```

## Como revisar respostas geradas por IA

Antes de usar qualquer saida da IA:

- Leia o resultado completo antes de aceitar.
- Verifique se o resultado atende ao objetivo do prompt.
- Identifique informacoes inventadas (alucinacoes).
- Teste o codigo gerado antes de commitar.
- Ajuste o que nao estiver correto ou adequado ao contexto.

## Como validar codigo gerado

- Execute o codigo e verifique se funciona.
- Leia o codigo linha a linha e entenda o que cada parte faz.
- Verifique se ha problemas de seguranca (ex: SQL injection, dados sensiveis expostos).
- Confirme que o codigo segue as convencoes do projeto.
- Adicione testes para o codigo gerado.

## Cuidados com alucinacoes

Modelos de linguagem podem gerar informacoes incorretas com aparencia de confianca. Sinais de alerta:

- Funcoes ou bibliotecas que nao existem.
- Versoes de dependencias incorretas.
- Comportamentos de API que nao correspondem a documentacao oficial.
- Logica que parece correta mas produz resultados errados.

Sempre verifique informacoes criticas na documentacao oficial.

## Responsabilidade humana

O desenvolvedor e responsavel pelo que entrega, independentemente de ter usado IA. Isso inclui:

- A corretude do codigo.
- A qualidade da documentacao.
- A seguranca da implementacao.
- O registro honesto do uso de IA.

Registre os prompts utilizados em `docs/prompts.md` para rastreabilidade e aprendizado.

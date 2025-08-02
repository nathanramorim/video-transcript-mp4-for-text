# Prompt RIPER-Copilot: /organize-transcricao

## Descrição
Organiza automaticamente o conteúdo de um arquivo de transcrição de reunião, identificando empresa, cliente e responsável, e gerando um documento markdown estruturado com tópicos, prioridades e próximos passos.

## Como usar
```
/organize-transcricao <caminho-do-arquivo-transcricao>
```

- O Copilot irá:
  1. Ler o arquivo de transcrição.
  2. Identificar automaticamente nome da empresa, cliente e responsável.
  3. Caso não encontre algum desses dados, solicitar ao usuário para informar antes de gerar o resumo.
  4. Gerar o documento organizado com todos os campos essenciais preenchidos.

## Exemplo
```
/organize-transcricao input/transcricao-de-reuniao-LS_ASSESSORIA_JURIDICA.md
```

## Observações
- O comando pode ser usado para qualquer transcrição gerada pelo sistema.
- Garante que o documento final sempre terá as informações essenciais para uso consultivo e documentação.
- Se faltar empresa, cliente ou responsável, o Copilot solicita ao usuário antes de finalizar o documento.

---

**Este prompt faz parte do workflow RIPER-Copilot e pode ser registrado na documentação do projeto para uso recorrente.**

# Padrões do Sistema: video-transcript
*Versão: 1.0*
*Criado: 2025-08-02*
*Última Atualização: 2025-08-02*

## Visão Geral da Arquitetura
Arquitetura simples baseada em processamento batch:
- Vídeos mp4 são colocados na pasta `input/`
- O sistema processa cada vídeo, gera transcrição e documentação consultiva em markdown
- Arquivos de saída são salvos em `output/` com nome: `transcricao-de-reuniao-[nome-cliente].md`

## Componentes Chave
- Input Handler: Detecta vídeos na pasta `input/`
- Processor: Executa transcrição e análise consultiva
- Output Writer: Gera arquivo markdown em `output/` nomeado por cliente

## Padrões de Design em Uso
- Modularidade: Separação clara entre entrada, processamento e saída
- Automação: Processamento batch sem intervenção manual

## Fluxo de Dados
1. Usuário coloca vídeo mp4 em `input/`
2. Sistema identifica o vídeo e solicita/recebe nome do cliente
3. Processor executa transcrição e análise
4. Output Writer salva resultado em `output/transcricao-de-reuniao-[nome-cliente].md`

## Decisões Técnicas Chave
- Processamento via console, sem interface gráfica
- Nome do cliente usado para identificar arquivo de saída

## Relacionamentos de Componentes
- Input Handler → Processor → Output Writer

---

*Este documento captura a arquitetura do sistema e padrões de design usados no projeto.*

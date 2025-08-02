# General Development Guidelines: video-transcript

## Project Context
**Project**: video-transcript
**Primary Language**: A definir
**Main Framework**: N/A
**Architecture**: Processamento batch via console, input/output folders

Projeto para gerar documentação consultiva e executiva a partir de vídeos mp4, identificando dores do cliente e mapeando oportunidades estratégicas e comerciais. Sem interface gráfica, todo processamento ocorre via console.

## Development Philosophy
Automação, modularidade, rastreabilidade e simplicidade. Separação clara entre entrada, processamento e saída. Foco em não perder conteúdo do vídeo e gerar documentação útil para stakeholders estratégicos, comerciais e clientes.

## Naming Conventions
- **Files**: transcricao-de-reuniao-[nome-cliente].md
- **Folders**: input, output
- **Variables/Functions**: nomes claros e descritivos

## Project Structure
- input/: vídeos mp4 para processar
- output/: transcrições geradas em markdown

## Code Organization Patterns
- Separação entre detecção de arquivos, processamento e escrita de saída
- Processamento batch automatizado

## Technology Stack
- A definir conforme escolha de linguagem

## Antipatterns to Avoid
- Misturar lógica de negócio com manipulação de arquivos
- Processamento manual (deve ser automatizado)
- Nomes de arquivos genéricos ou pouco descritivos

## Quality Guidelines
- Documentação gerada deve cobrir todo conteúdo do vídeo
- Saída em markdown estruturado

## Error Handling
- Mensagens claras para erros de leitura/escrita
- Validação do nome do cliente

## Performance Considerations
- Processamento eficiente de arquivos grandes

---
*General development guidelines for video-transcript using GitHub Copilot*

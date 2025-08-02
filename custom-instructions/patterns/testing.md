# Testing Guidelines: video-transcript

## Testing Philosophy
Testes devem garantir que todo vídeo mp4 colocado em input/ gera uma transcrição completa e fiel em output/. Testes unitários e de integração devem validar processamento, geração de markdown e nomeação correta dos arquivos.

## Test Organization
- Testes organizados por funcionalidade: detecção de arquivos, processamento, geração de saída
- Testes de integração para fluxo completo

## Unit Testing
- Funções de processamento devem ser testadas isoladamente
- Validação de entrada (nome do cliente, formato do vídeo)

## Mocking and Stubbing
- Mock para leitura de arquivos mp4
- Mock para escrita de arquivos markdown

## Test Data Management
- Fixtures de vídeos mp4 de exemplo
- Dados de clientes fictícios para nomeação

## Integration Testing
- Testar fluxo completo: input → processamento → output

## End-to-End Testing
- Simular uso real: colocar vídeo em input/, informar nome do cliente, verificar saída

## Performance Testing
- Testar processamento de vídeos grandes

## Test Automation
- Automatizar execução dos testes

## Test Quality and Maintenance
- Cobertura de testes deve ser alta
- Testes devem ser claros e fáceis de manter

---
*Testing guidelines for video-transcript using GitHub Copilot*

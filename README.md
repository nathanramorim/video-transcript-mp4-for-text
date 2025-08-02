# video-transcript

Sistema para transcrição automática de vídeos mp4 e organização consultiva de reuniões, utilizando o framework RIPER-Copilot.

## Opções de Transcrição

### Dois motores disponíveis:

**1. Vosk (offline, gratuito)**
- Motor padrão para transcrição offline
- Sem custos, mas qualidade pode variar
- Requer modelo português na pasta `model/`

**2. OpenAI GPT-4o-mini-transcribe (online, pago)**
- Qualidade superior de transcrição
- **Custo aproximado: ~$0,05 USD para áudio de 45 minutos** 
- Requer token da OpenAI no arquivo `.env`
- Divisão automática para áudios longos (limite: 1400s por parte)

## Como executar a transcrição

1. Coloque o vídeo mp4 desejado na pasta `input/`.
2. Configure o ambiente (veja seção "Configuração" abaixo).
3. Execute o script:

```bash
python main.py
```

4. Escolha o motor de transcrição no menu interativo.
5. Selecione os vídeos e informe o nome do cliente.
6. O resultado será gerado na pasta `output/` como um arquivo markdown.

## Configuração

### Para usar Vosk (offline):
- Baixe o modelo português em: https://alphacephei.com/vosk/models
- Extraia na pasta `model/` do projeto

### Para usar OpenAI (online):
1. Crie um arquivo `.env` na raiz do projeto:
```bash
OPENAI_API_KEY=sua_chave_aqui
```
2. Instale dependências adicionais:
```bash
pip install openai python-dotenv
```

## Como funciona

1. **Transcrição de vídeo**
   - Coloque o arquivo mp4 na pasta `input/`.
   - Execute o script principal para gerar a transcrição em markdown.
   - O áudio é extraído automaticamente e processado pelo modelo Vosk (offline, gratuito).

2. **Organização da transcrição**
   - Use o prompt `/organize-transcricao <caminho-do-arquivo-transcricao>` para gerar um documento estruturado com tópicos, responsável, prioridades e próximos passos.
   - O Copilot identifica automaticamente empresa, cliente e responsável. Caso não encontre, solicita ao usuário.

3. **Workflow RIPER-Copilot**
   - O projeto segue o fluxo: RESEARCH → INNOVATE → PLAN → EXECUTE → REVIEW.
   - Prompts e instruções customizadas estão em `custom-instructions/` e `.github/prompts/`.

## Requisitos

- Python 3.13+
- ffmpeg instalado no sistema
- Dependências básicas: `vosk` (para modo offline)
- Dependências adicionais: `openai python-dotenv` (para modo online)

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

## Custos e Performance

### Comparação dos motores

| Motor | Custo | Qualidade | Velocidade | Requisitos |
|-------|--------|-----------|------------|------------|
| Vosk | Gratuito | Boa | Média | Modelo local |
| OpenAI GPT-4o-mini | ~$0,05 USD/45min | Excelente | Rápida | Token API |

**Detalhes de custo OpenAI:**

- Áudio de 45 minutos: aproximadamente $0,05 USD
- Divisão automática para áudios > 23 minutos (limite técnico)
- Cobrança por minuto de áudio processado

## Observações

- Não é necessário subir os arquivos das pastas `input/` e `output/` para o repositório.
- O sistema é totalmente offline e pode ser adaptado para outros idiomas/modelos.
- Para dúvidas ou personalizações, consulte os arquivos de instrução do projeto.

---

**Este projeto é mantido por LS_ASSESSORIA_JURIDICA e segue boas práticas de documentação e automação consultiva.**

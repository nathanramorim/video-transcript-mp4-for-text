# video-transcript

Sistema para transcrição automática de vídeos mp4 e organização consultiva de reuniões, utilizando o framework RIPER-Copilot.

## Como executar a transcrição

1. Coloque o vídeo mp4 desejado na pasta `input/`.
2. Certifique-se de que o modelo Vosk para português está na pasta `model/`.
3. No terminal, execute:

```bash
python main.py --cliente NOME_DO_CLIENTE
```

4. O resultado será gerado na pasta `output/` como um arquivo markdown com a transcrição.

**Exemplo:**
```bash
python main.py --cliente LS_ASSESSORIA_JURIDICA
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
- Modelo Vosk para português na pasta `model/`
- Dependências: `vosk`, `argparse`, etc. (veja instruções no script principal)

## Observações
- Não é necessário subir os arquivos das pastas `input/` e `output/` para o repositório.
- O sistema é totalmente offline e pode ser adaptado para outros idiomas/modelos.
- Para dúvidas ou personalizações, consulte os arquivos de instrução do projeto.

---

**Este projeto é mantido por LS_ASSESSORIA_JURIDICA e segue boas práticas de documentação e automação consultiva.**

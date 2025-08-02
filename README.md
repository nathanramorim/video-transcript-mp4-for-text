# MP4 for Text 🚀✨

<p align="center">
  <img src="capa-video-to-text.jpeg" alt="Capa MP4 for Text" width="600" />
</p>

Transforme vídeos em conhecimento, gere valor e surpreenda seus clientes!

**Bem-vindo ao MP4 for Text!**

🎥 **De vídeo para texto, de texto para ação!**

Imagine: aquele briefing, reunião ou depoimento em vídeo se tornando um documento consultivo, pronto para análise, decisão e resultado. Tudo em minutos, com automação, segurança e controle total de custos.

---

## Benefícios

- Documentação instantânea: gere relatórios, atas e insights a partir de vídeos mp4
- Privacidade e controle: escolha entre transcrição offline (Vosk) ou online (OpenAI)
- Automação total: do vídeo ao markdown, sem esforço manual
- Custo sob medida: saiba exatamente quanto vai gastar antes de transcrever
- Consultivo e flexível: ideal para advogados, consultores, equipes remotas, educadores e inovadores

---

## Exemplo de uso real

> "Com o MP4 for Text, transformei reuniões em relatórios prontos para enviar ao cliente. Ganhei tempo, clareza e profissionalismo!" — Cliente satisfeito

---

## Requisitos

- Python 3.13+
- ffmpeg instalado no sistema (obrigatório para extrair áudio dos vídeos mp4)
- Dependências básicas: `vosk` (para modo offline)
- Dependências adicionais: `openai python-dotenv` (para modo online)

### Instalação do ffmpeg

**macOS:**
```bash
brew install ffmpeg
```
**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```
**Windows:**
Acesse: [ffmpeg.org/download.html](https://ffmpeg.org/download.html)

---

## Ambiente virtual recomendado

Para evitar conflitos de dependências, recomenda-se criar um ambiente virtual Python:

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate    # Windows
```

Depois, instale todas as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração

### Para usar Vosk (offline):
- Baixe o modelo português em: [alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
- Extraia na pasta `model/` do projeto

### Para usar OpenAI (online):
1. Crie um arquivo `.env` na raiz do projeto:
```env
OPENAI_API_KEY=seu_token_aqui
OPENAI_MAX_SECONDS=900
OPENAI_OVERLAP_SECONDS=15
OPENAI_TRANSCRIBE_PROMPT="Transcreva todo o conteúdo do áudio, sem resumir ou omitir partes. Mantenha a ordem e o máximo de detalhes possível."
```

---

## Como Usar

<p align="center">
  <img src="how-is.png" alt="Como funciona" width="600" />
</p>

1. Coloque o vídeo mp4 na pasta `input/`
2. Execute o script principal:
   ```bash
   python main.py
   ```
3. Siga o menu interativo para escolher motor, vídeos e cliente
4. Confira o custo estimado antes de prosseguir (OpenAI)
5. O resultado será gerado em `output/` como Markdown

---

## Novidades: Transcrição GPT/OpenAI aprimorada

- **Chunking inteligente:** Áudio dividido em partes de até 900 segundos (15min) com sobreposição de 15 segundos entre partes. Evita cortes de frases e perda de contexto.
- **Prompt customizado:** O modelo OpenAI recebe um prompt configurável para garantir máxima completude.
- **Recomendação para reuniões de 30-60min:** Use chunks de 900s e overlap de 15s para máxima confiabilidade.
- **Custo por minuto:** O valor cobrado é por minuto de áudio processado, não por tokens gerados.
- **Dica:** Sempre coloque valores com espaços entre aspas no `.env`.

---

## Como garantir transcrição completa

- Use chunking inteligente e sobreposição para evitar cortes de frases.
- Ajuste o prompt para pedir transcrição integral, sem resumos.
- Confira os logs: o sistema mostra quantos caracteres cada parte gerou e alerta se alguma parte ficou vazia.
- Para áudios longos, revise o resultado final e ajuste os parâmetros se necessário.

---

## Custos e Performance

| Motor                | Custo           | Qualidade   | Limite        | Requisitos         |
|----------------------|-----------------|-------------|---------------|--------------------|
| Vosk (offline)       | Gratuito        | Boa         | Ilimitado     | Modelo local       |
| OpenAI GPT-4o-mini   | ~$0,006/minuto  | Excelente   | 900s/parte    | Token OpenAI       |

**Detalhes de custo OpenAI:**
- Áudio de 45 minutos: aproximadamente $0,05 USD
- Divisão automática para áudios > 15 minutos (limite técnico)
- Cobrança por minuto de áudio processado

---

## FAQ

**Posso usar só offline?**
Sim, basta escolher Vosk no menu.

**O que acontece se o áudio for muito longo?**
OpenAI divide automaticamente em partes de até 900s (configurável).

**Como validar se a transcrição está completa?**
Confira os logs detalhados no console. O sistema mostra quantos caracteres cada parte gerou.

**Como adaptar para outros clientes?**
Edite os prompts em `custom-instructions/` para personalizar a análise consultiva.

---

## Observações

- Não é necessário subir os arquivos das pastas `input/` e `output/` para o repositório.
- O sistema é totalmente offline e pode ser adaptado para outros idiomas/modelos.
- Para dúvidas ou personalizações, consulte os arquivos de instrução do projeto.

---

## Licença e Créditos

Projeto mantido por **Nathan Amorim**.
- [GitHub](https://github.com/nathanramorim)
- [Instagram](https://www.instagram.com/nathan.ramorim/)
- [LinkedIn](https://www.linkedin.com/in/nathanramorim/)

Uso livre para fins consultivos, educacionais e profissionais.


# MP4 for Text 🚀✨

<p align="center">
   <img src="how-is.png" alt="Como funciona" width="600" />
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

## Dica para usuários Google Meet, Zoom, Teams

Gravou sua reunião no Google Meet, Zoom ou Teams e não tem transcrição automática?

Muitos planos permitem gravar reuniões mas não oferecem transcrição automática. O MP4 for Text resolve esse problema: basta baixar o vídeo gravado, colocar na pasta `input/` e transformar tudo em texto consultivo, pronto para análise, relatório ou envio ao cliente!

Ideal para quem precisa registrar decisões, demandas e conversas importantes sem depender de recursos pagos ou limitados das plataformas de reunião.

---

## Sumário

- [Requisitos](#requisitos)
- [Instalação](#instalacao)
- [Como Usar](#como-usar)
- [Motores de Transcrição](#motores-de-transcricao)
- [Calculadora de Custo](#calculadora-de-custo)
- [FAQ](#faq)
- [Licença e Créditos](#licenca-e-creditos)

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
Baixe em: https://ffmpeg.org/download.html

---

## Ambiente virtual recomendado

Para evitar conflitos de dependências, recomenda-se criar um ambiente virtual Python:

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate    # Windows
```

Depois, instale as dependências normalmente:

```bash
pip install -r requirements.txt
```

---

## Como Usar

1. Coloque o vídeo mp4 na pasta `input/`
2. Execute o script principal:
   ```bash
   python main.py
   ```
3. Siga o menu interativo para escolher motor, vídeos e cliente
4. Confira o custo estimado antes de prosseguir (OpenAI)
5. O resultado será gerado em `output/` como Markdown

---

## Motores de Transcrição

| Motor                | Custo           | Qualidade   | Limite        | Requisitos         |
|----------------------|-----------------|-------------|---------------|--------------------|
| Vosk (offline)       | Gratuito        | Boa         | Ilimitado     | Modelo local       |
| OpenAI GPT-4o-mini   | ~$0,006/minuto  | Excelente   | 1400s/parte   | Token OpenAI       |

---

## Calculadora de Custo

Antes de transcrever com OpenAI, o sistema mostra:

```
💰 CALCULADORA DE CUSTO OPENAI
📊 Duração do áudio: 2725.0 segundos (45.4 minutos)
💵 Custo estimado: $0.2724 USD (~R$ 1.50)
⚠️  Áudio será dividido em 2 partes (limite: 1400s por parte)
🔄 Deseja prosseguir com a transcrição? [s/n]:
```

---

## FAQ

**Posso usar só offline?**
Sim, basta escolher Vosk no menu.

**O que acontece se o áudio for muito longo?**
OpenAI divide automaticamente em partes de até 1400s.

**Como validar se a transcrição está completa?**
Confira os logs detalhados no console. O sistema mostra quantos caracteres cada parte gerou.

**Como adaptar para outros clientes?**
Edite os prompts em `custom-instructions/` para personalizar a análise consultiva.

---

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


## Licença e Créditos

Projeto mantido por **Nathan Amorim**.


Redes sociais:

<p align="left">
   <a href="https://github.com/nathanramorim">
      <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
   </a>
   <a href="https://www.instagram.com/nathan.ramorim/">
      <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
   </a>
   <a href="https://www.linkedin.com/in/nathanramorim/">
      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
   </a>
</p>

Uso livre para fins consultivos, educacionais e profissionais.

---

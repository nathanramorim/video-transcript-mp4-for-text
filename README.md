---

## Nota Importante

⚠️ **Atenção:** Em áudios longos divididos automaticamente, pode ocorrer perda de informação no final da transcrição. Estamos investigando e ajustando o algoritmo de divisão para garantir que todo o conteúdo seja preservado. Assim que o problema for resolvido, esta nota será atualizada!

---
---

## Instalação das dependências

Para instalar todas as dependências necessárias, basta rodar:

```bash
pip install -r requirements.txt
```

Isso garante que o ambiente está pronto para usar tanto o motor offline (Vosk) quanto o online (OpenAI).

---
---

## Por que usar MP4 for Text?

🌟 **Documentação instantânea:** gere relatórios, atas e insights a partir de vídeos mp4
🔒 **Privacidade e controle:** escolha entre transcrição offline (Vosk) ou online (OpenAI)
🤖 **Automação total:** do vídeo ao markdown, sem esforço manual
💸 **Custo sob medida:** saiba exatamente quanto vai gastar antes de transcrever
👩‍💼 **Consultivo e flexível:** ideal para advogados, consultores, equipes remotas, educadores e inovadores

---

## Como transformar gravações de reuniões em texto consultivo?

🎥 **Google Meet, Zoom, Teams e outros**: Muitos planos permitem gravar reuniões, mas não oferecem transcrição automática. Com o MP4 for Text, basta baixar o vídeo gravado, colocar na pasta `input/` e transformar tudo em texto consultivo, pronto para análise, relatório ou envio ao cliente!

Ideal para quem precisa registrar decisões, demandas e conversas importantes sem depender de recursos pagos ou limitados das plataformas de reunião.

---
---

## Dica para usuários Google Meet, Zoom, Teams

🎥 **Gravou sua reunião no Google Meet, Zoom ou Teams e não tem transcrição automática?**

Muitos planos, como o Google One, permitem gravar reuniões mas não oferecem transcrição automática. O MP4 for Text resolve esse problema: basta baixar o vídeo gravado, colocar na pasta `input/` e transformar tudo em texto consultivo, pronto para análise, relatório ou envio ao cliente!

Ideal para quem precisa registrar decisões, demandas e conversas importantes sem depender de recursos pagos ou limitados das plataformas de reunião.

---
# MP4 for Text 🚀✨

Transforme vídeos em conhecimento, gere valor e surpreenda seus clientes! 

**Bem-vindo ao MP4 for Text!**

🎥 **De vídeo para texto, de texto para ação!**

Imagine: aquele briefing, reunião ou depoimento em vídeo se tornando um documento consultivo, pronto para análise, decisão e resultado. Tudo em minutos, com automação, segurança e controle total de custos.

---

## Por que usar MP4 for Text?

🌟 **Documentação instantânea:** gere relatórios, atas e insights a partir de vídeos mp4
🔒 **Privacidade e controle:** escolha entre transcrição offline (Vosk) ou online (OpenAI)
🤖 **Automação total:** do vídeo ao markdown, sem esforço manual
💸 **Custo sob medida:** saiba exatamente quanto vai gastar antes de transcrever
👩‍💼 **Consultivo e flexível:** ideal para advogados, consultores, equipes remotas, educadores e inovadores

---

## Exemplo de uso real

> "Com o MP4 for Text, transformei reuniões em relatórios prontos para enviar ao cliente. Ganhei tempo, clareza e profissionalismo!" — Cliente satisfeito

---

## Chamada para ação

✨ **Experimente agora!** Coloque seu vídeo em `input/`, rode o script e veja a mágica acontecer. Surpreenda seu cliente, equipe ou gestor com documentação consultiva de alto nível!

---
# video-transcript

![Python](https://img.shields.io/badge/python-3.13%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini--transcribe-00aaff)
![Vosk](https://img.shields.io/badge/Vosk-offline-green)
![RIPER](https://img.shields.io/badge/Framework-RIPER--Copilot-ff69b4)

---

## Sumário

- [Visão Geral](#visão-geral)
- [Diferenciais](#diferenciais)
- [Como Usar](#como-usar)
- [Configuração](#configuração)
- [Motores de Transcrição](#motores-de-transcrição)
- [Calculadora de Custo](#calculadora-de-custo)
- [Exemplo de Uso](#exemplo-de-uso)
- [FAQ](#faq)
- [Licença](#licença)

---

## Visão Geral

Sistema consultivo para transcrição automática de vídeos mp4, geração de documentação e análise de reuniões. Permite workflow híbrido (offline/online), cálculo de custos, automação e integração com o framework RIPER-Copilot.

---

## Diferenciais

- **Transcrição híbrida:** escolha entre Vosk (offline, gratuito) ou OpenAI GPT-4o-mini (online, pago)
- **Calculadora de custo automática** antes de transcrever
- **Divisão inteligente de áudios longos** para OpenAI
- **Workflow consultivo:** prompts para organizar e analisar reuniões
- **Automação total:** limpeza de arquivos temporários, logs detalhados
- **Documentação estruturada:** saída em Markdown pronta para consulta

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

## Configuração

### Vosk (offline)
- Baixe o modelo português: [Vosk Models](https://alphacephei.com/vosk/models)
- Extraia na pasta `model/`

### OpenAI GPT-4o-mini (online)
- Crie `.env` com sua chave:
   ```env
   OPENAI_API_KEY=sua_chave_aqui
   ```
- Instale dependências:
   ```bash
   pip install openai python-dotenv
   ```

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

## Exemplo de Uso

```bash
python main.py
# Escolha motor, vídeo e cliente no menu
# Veja o custo estimado antes de confirmar
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

## Licença e Créditos

 Projeto mantido por Nathan Amorim:
 - [GitHub](https://github.com/nathanramorim)
 - [Instagram](https://www.instagram.com/nathan.ramorim/)
 - [LinkedIn](https://www.linkedin.com/in/nathanramorim/)
 
 Uso livre para fins consultivos, educacionais e profissionais.
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

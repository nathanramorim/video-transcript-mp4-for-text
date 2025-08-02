# 🎥 Video Transcript API - From MP4 to Text 🚀

<p align="center">
  <img src="capa-video-to-text.jpeg" alt="Capa MP4 for Text" width="600" />
</p>

**Transforme vídeos em conhecimento, agora com uma API moderna e escalável!**

Este projeto evoluiu de um **script CLI** para uma **API FastAPI completa**, oferecendo transcrição de vídeos com autenticação, controle de concorrência e muito mais.

## 📁 Estrutura do Projeto

```
video-transcript-api/
├── 📚 feature-instructions/        # � Documentação da nova API
│   ├── IMPLEMENTACAO_MASTER.md     # 🚀 Manual principal (COMECE AQUI)
│   ├── ARQUITETURA_API.md          # 🏗️ Arquitetura técnica
│   ├── PLANO_MIGRACAO_API.md       # 📋 Plano de migração
│   └── [outros documentos...]      # 📊 Especificações detalhadas
│
├── 🕰️ legacy-transcription/        # 💾 Código CLI original (preservado)
│   ├── main.py                     # ⚙️ Script original funcional
│   ├── input/                      # 📥 Vídeos de teste
│   ├── output/                     # 📤 Transcrições geradas
│   └── README.md                   # 📖 Documentação do CLI
│
├── 🤖 model/                       # 🧠 Modelo Vosk (português)
├── 🖼️ [imagens e docs]             # 📸 Recursos do projeto
└── 🚀 [nova API - em desenvolvimento]
```

## 🚀 Duas Versões Disponíveis

### **🆕 Nova API FastAPI** (Recomendada)
- 🔐 **Autenticação JWT** com tipos de usuário
- ⚡ **Processamento assíncrono** com filas
- 🛡️ **Rate limiting** e fair usage
- 🌐 **API REST** moderna e documentada
- 🐳 **Deploy containerizado**
- 📊 **Monitoramento** e métricas

**👉 Para implementar a nova API:**
```bash
# Consulte o manual principal
cat feature-instructions/IMPLEMENTACAO_MASTER.md
```

### **🕰️ CLI Legacy** (Funcional, mantido para compatibilidade)
- ✅ **Transcrição Vosk** (offline, gratuita)
- ✅ **Transcrição OpenAI** (online, paga)
- ✅ **Processamento em lotes**
- ✅ **Formatação Markdown**

**👉 Para usar o CLI original:**
```bash
# Navegar para a pasta legacy
cd legacy-transcription/

# Seguir instruções do README
cat README.md
```

## 💡 Recursos e Benefícios

### **🎯 Funcionalidades Core**
- ✅ **Extração de áudio** de vídeos (MP4, MOV)
- ✅ **Transcrição Vosk** (offline, gratuita, português)
- ✅ **Transcrição OpenAI** (online, paga, alta qualidade)
- ✅ **Processamento assíncrono** com filas por prioridade
- ✅ **Autenticação JWT** com tipos de usuário (Free/Premium/Admin)
- ✅ **Rate limiting** e fair usage
- ✅ **Zero persistência** de dados temporários
- ✅ **Documentação automática** (Swagger/OpenAPI)

### **📈 Vantagens do Novo Sistema**
- **Escalabilidade**: Suporte a múltiplos usuários simultâneos
- **Segurança**: Autenticação robusta e controle de acesso
- **Eficiência**: Filas inteligentes com priorização
- **Monitoramento**: Logs estruturados e métricas
- **Deploy**: Containerização com Docker
- **API REST**: Integração fácil com outros sistemas

## 🚀 Quick Start

### **Para a Nova API (Recomendado)**

1. **📖 Consulte o manual principal:**
   ```bash
   cat feature-instructions/IMPLEMENTACAO_MASTER.md
   ```

2. **⚡ Implementação rápida:**
   - Siga o manual passo a passo
   - Tempo total: 20-25 horas
   - Resultado: API production-ready

### **Para o CLI Legacy**

1. **📂 Acesse a pasta legacy:**
   ```bash
   cd legacy-transcription/
   ```

2. **📖 Siga as instruções:**
   ```bash
   cat README.md
   ```

## 📋 Pré-requisitos

### **Sistema**
- Python 3.11+
- FFmpeg instalado
- Redis (para a nova API)
- Docker (opcional, para deploy)

### **Instalação FFmpeg**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian  
sudo apt-get install ffmpeg

# Windows
# Baixe em: https://ffmpeg.org/download.html
```

### **Modelo Vosk**
- Baixe o modelo português em: [alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
- Extraia na pasta `model/` do projeto

## 🔧 Configuração

### **Ambiente Virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

### **Variáveis de Ambiente**
Copie `.env.example` para `.env` e configure:
```env
# OpenAI (opcional)
OPENAI_API_KEY=sua-chave-aqui

# API Settings (nova API)
JWT_SECRET_KEY=sua-chave-jwt-super-secreta
REDIS_URL=redis://localhost:6379/0
```

## 📊 Custos e Performance

| Método | Custo | Qualidade | Velocidade | Requisitos |
|--------|-------|-----------|------------|------------|
| **Vosk** | Gratuito | Boa | Média | Modelo local |
| **OpenAI** | ~$0.006/min | Excelente | Rápida | API Key |

## 🎯 Roadmap

### **✅ Concluído**
- [x] Script CLI funcional
- [x] Planejamento completo da API
- [x] Arquitetura detalhada
- [x] Documentação abrangente

### **🚧 Em Desenvolvimento**
- [ ] Implementação da API FastAPI
- [ ] Sistema de autenticação JWT
- [ ] Queue manager com Redis
- [ ] Endpoints REST
- [ ] Testes automatizados

### **🔮 Próximos Passos**
- [ ] Deploy em produção
- [ ] Monitoramento avançado
- [ ] Interface web
- [ ] Mobile app
- [ ] Integração com terceiros

## 📚 Documentação

| Documento | Propósito | Público |
|-----------|-----------|---------|
| `feature-instructions/IMPLEMENTACAO_MASTER.md` | Manual principal de implementação | Desenvolvedores |
| `feature-instructions/ARQUITETURA_API.md` | Arquitetura técnica detalhada | Arquitetos/Lead Devs |
| `legacy-transcription/README.md` | Uso do CLI original | Usuários finais |

## 🤝 Contribuição

1. **Fork** o projeto
2. **Crie** uma branch para sua feature
3. **Implemente** seguindo a arquitetura documentada
4. **Teste** thoroughly
5. **Submeta** um Pull Request

## 📄 Licença

Projeto mantido por **Nathan Amorim**.

- [GitHub](https://github.com/nathanramorim)
- [Instagram](https://www.instagram.com/nathan.ramorim/)
- [LinkedIn](https://www.linkedin.com/in/nathanramorim/)

Uso livre para fins consultivos, educacionais e profissionais.

---

**🚀 Ready to build? Comece pelo manual de implementação em `feature-instructions/IMPLEMENTACAO_MASTER.md`!**

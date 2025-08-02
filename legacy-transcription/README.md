# 🕰️ Legacy Transcription - CLI Original

## 📋 Visão Geral

Esta pasta contém o **código original CLI** de transcrição de vídeos, preservado para referência e compatibilidade durante a migração para a nova API FastAPI.

## 📁 Estrutura do Código Legacy

```
legacy-transcription/
├── 📄 Scripts Python
│   ├── main.py                 # 🔧 Script principal CLI
│   ├── main_backup.py          # 🔒 Backup de segurança
│   └── requirements.txt        # 📋 Dependências originais
│
├── 📂 Dados de Processamento
│   ├── input/                  # 📥 Vídeos de entrada
│   ├── output/                 # 📤 Transcrições geradas
│   └── memory-bank/            # 💾 Cache e memória
│
└── 📖 README.md               # 📝 Esta documentação
```

## 🔧 Como Usar o CLI Original

### **⚡ Setup Rápido (Recomendado)**
```bash
# 1. Execute o script de correção automática
./fix-legacy-env.sh

# 2. Ative o ambiente virtual (se necessário)
source ../venv/bin/activate

# 3. Execute o script
python3 main.py
```

### **🛠️ Setup Manual (Alternativo)**

#### **Pré-requisitos**
```bash
# 1. Ativar ambiente virtual do projeto principal
cd /caminho/para/transcript-video
source venv/bin/activate

# 2. Voltar para pasta legacy
cd legacy-transcription

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Criar links simbólicos necessários
ln -s ../model model     # Acesso ao modelo Vosk
ln -s ../.env .env       # Acesso às configurações
```

#### **Executar Transcrição**
```bash
# Com ambiente virtual ativo
python3 main.py

# O script irá processar os vídeos da pasta input/
# e gerar as transcrições na pasta output/
```

## ⚙️ Funcionalidades do CLI

### **🎯 Recursos Implementados**
- ✅ **Extração de áudio** de vídeos (MP4)
- ✅ **Transcrição Vosk** (offline, gratuita)
- ✅ **Transcrição OpenAI** (online, paga)
- ✅ **Processamento em lotes**
- ✅ **Segmentação inteligente** para arquivos grandes
- ✅ **Correção via GPT** das transcrições Vosk
- ✅ **Formatação em Markdown**
- ✅ **Logs detalhados**

### **🔧 Configurações Atuais**
- **Modelo Vosk**: Português brasileiro
- **OpenAI**: Whisper API com GPT-4 para correções
- **Formatos suportados**: MP4, MOV
- **Tamanho máximo**: Limitado pela API OpenAI
- **Segmentação**: 15 minutos por chunk

## 📊 Status de Migração

| Funcionalidade | CLI Legacy | Nova API | Status |
|----------------|------------|----------|--------|
| Extração de áudio | ✅ | 📋 Planejado | Em migração |
| Transcrição Vosk | ✅ | 📋 Planejado | Em migração |
| Transcrição OpenAI | ✅ | 📋 Planejado | Em migração |
| Autenticação | ❌ | 📋 Planejado | Nova funcionalidade |
| Rate Limiting | ❌ | 📋 Planejado | Nova funcionalidade |
| API REST | ❌ | 📋 Planejado | Nova funcionalidade |
| Filas | ❌ | 📋 Planejado | Nova funcionalidade |

## 🔄 Migração para Nova API

### **📚 Documentação da Nova API**
A documentação completa da nova API FastAPI está em:
```
../feature-instructions/
├── IMPLEMENTACAO_MASTER.md     # 🚀 Manual principal
├── ARQUITETURA_API.md          # 🏗️ Arquitetura técnica
└── [outros documentos]         # 📋 Especificações detalhadas
```

### **🎯 Benefícios da Nova API**
- 🔐 **Autenticação JWT** com tipos de usuário
- ⚡ **Processamento assíncrono** com filas
- 🛡️ **Rate limiting** e proteção contra abuso
- 🌐 **API REST** moderna e documentada
- 🐳 **Deploy containerizado** com Docker
- 📊 **Monitoramento** e métricas
- 🔄 **Escalabilidade** horizontal

## 🚨 Importante

### **⚠️ Avisos de Compatibilidade**
- Este código CLI será **descontinuado** após a migração
- Use apenas para **referência** durante o desenvolvimento da API
- **Não faça alterações** nestes arquivos - eles são preservados como backup

### **🔄 Durante a Migração**
- O CLI original permanece **funcional** para casos de emergência
- A nova API será desenvolvida em **paralelo**
- **Testes comparativos** serão feitos entre CLI e API

## 📝 Notas de Desenvolvimento

### **🧩 Componentes Reutilizáveis**
1. **Lógica de extração de áudio** (moviepy) → `audio_service.py`
2. **Integração Vosk** → `vosk_service.py`
3. **Integração OpenAI** → `openai_service.py`
4. **Processamento de texto** → `text_utils.py`
5. **Formatação Markdown** → `format_utils.py`

### **🔧 Refatorações Necessárias**
- Separar lógica de apresentação da lógica de negócio
- Implementar injeção de dependências
- Adicionar tratamento de erros robusto
- Implementar logging estruturado
- Criar testes unitários

---

## 📖 Histórico

**Versão Original**: Script CLI funcional para transcrição
**Data de Preservação**: 02/08/2025
**Status**: Preservado como referência durante migração para FastAPI

**🚀 Para implementar a nova API, consulte: `../feature-instructions/IMPLEMENTACAO_MASTER.md`**

# 🚀 Plano de Migração para API FastAPI - Video Transcript Service

## 📋 Visão Geral

Este documento detalha o plano completo para transformar o script atual de transcrição de vídeos em uma API RESTful moderna usando FastAPI, mantendo todas as funcionalidades existentes e adicionando novos recursos.

## 🎯 Objetivos

- ✅ Transformar script CLI em API REST
- ✅ Separar serviços Vosk e OpenAI
- ✅ Criar endpoint para extração de áudio
- ✅ Manter toda lógica existente
- ✅ Implementar Swagger/OpenAPI automático
- ✅ Documentação API atualizada
- ✅ Priorizar implementação Vosk (gratuito)

## 🏗️ Arquitetura Proposta

```text
transcript-video-api/
├── main.py                    # Backup do código original
├── main_backup.py            # Backup automático
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app principal
│   ├── config.py            # Configurações
│   ├── models/
│   │   ├── __init__.py
│   │   ├── requests.py      # Modelos de request
│   │   └── responses.py     # Modelos de response
│   ├── services/
│   │   ├── __init__.py
│   │   ├── audio_service.py    # Extração de áudio
│   │   ├── vosk_service.py     # Transcrição Vosk
│   │   └── openai_service.py   # Transcrição OpenAI
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── audio.py           # Endpoints de áudio
│   │   ├── vosk.py           # Endpoints Vosk
│   │   └── openai.py         # Endpoints OpenAI
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py     # Utilitários de arquivo
│       └── audio_utils.py    # Utilitários de áudio
├── requirements_api.txt      # Dependências da API
├── README_API.md            # Documentação da API
├── docker-compose.yml       # Para containerização
└── Dockerfile              # Para containerização
```

## 📊 Endpoints Propostos

### 🎵 Audio Service

- `POST /api/v1/audio/extract` - Extrai áudio de vídeo MP4
- `GET /api/v1/audio/{audio_id}/info` - Informações do áudio
- `DELETE /api/v1/audio/{audio_id}` - Remove áudio temporário

### 🗣️ Vosk Service

- `POST /api/v1/vosk/transcribe` - Transcrição usando Vosk (retorna texto no body + opção markdown)
- `GET /api/v1/vosk/models` - Lista modelos disponíveis
- `GET /api/v1/vosk/status` - Status do serviço Vosk

### 🤖 OpenAI Service

- `POST /api/v1/openai/transcribe` - Transcrição usando OpenAI (retorna texto no body + opção markdown)
- `POST /api/v1/openai/estimate-cost` - Estimativa de custo
- `GET /api/v1/openai/status` - Status do serviço OpenAI

### �️ Endpoints da API

- `POST /api/v1/auth/token` - **Autenticação JWT (NOVO)**
- `POST /api/v1/auth/refresh` - **Refresh token (NOVO)**

### 🎵 Audio Service

- `POST /api/v1/audio/extract` - Extrai áudio de vídeo MP4 (🔒 JWT required)
- `GET /api/v1/audio/{audio_id}/info` - Informações do áudio (🔒 JWT required)
- `DELETE /api/v1/audio/{audio_id}` - Remove áudio temporário (🔒 JWT required)

### 🗣️ Vosk Service

- `POST /api/v1/vosk/transcribe` - Transcrição usando Vosk (🔒 JWT required + 🚦 Queue)
- `GET /api/v1/vosk/queue/status` - **Status da fila de processamento (NOVO)**
- `GET /api/v1/vosk/models` - Lista modelos disponíveis (🔒 JWT required)
- `GET /api/v1/vosk/status` - Status do serviço Vosk (🔒 JWT required)

### 📄 Utility Endpoints

- `GET /api/v1/health` - Health check (público, sem JWT)
- `GET /api/v1/docs` - Swagger UI (público, sem JWT)
- `GET /api/v1/redoc` - ReDoc documentação (público, sem JWT)

## 🔧 Etapas de Implementação

### **Fase 1: Preparação e Estrutura Base** ⏱️ 2-3h

- [ ] 1.1 Criar backup do código original
- [ ] 1.2 Criar estrutura de diretórios
- [ ] 1.3 Configurar FastAPI básico
- [ ] 1.4 Implementar health check
- [ ] 1.5 Configurar CORS e middleware básico

### **Fase 2: Modelos e Configurações** ⏱️ 2-3h

- [ ] 2.1 Criar modelos Pydantic para requests/responses
- [ ] 2.2 Configurar variáveis de ambiente
- [ ] 2.3 Implementar validações de entrada
- [ ] 2.4 Configurar logging estruturado
- [ ] 2.5 **Implementar autenticação JWT (NOVO)**
- [ ] 2.6 **Configurar sistema de rate limiting e controle de concorrência (NOVO)**

### **Fase 3: Serviço de Áudio (Prioridade Alta)** ⏱️ 3-4h

- [ ] 3.1 Migrar função `extract_audio()` para serviço
- [ ] 3.2 Implementar upload de arquivo MP4
- [ ] 3.3 Criar endpoint de extração de áudio
- [ ] 3.4 Implementar gerenciamento de arquivos temporários com auto-cleanup
- [ ] 3.5 Adicionar validações de formato de vídeo
- [ ] 3.6 Criar sistema de limpeza automática pós-processamento

### **Fase 4: Serviço Vosk (Prioridade Alta)** ⏱️ 5-6h

- [ ] 4.1 Migrar função `transcribe_audio()` para serviço
- [ ] 4.2 Implementar função `split_wav()` para áudios longos
- [ ] 4.3 Criar endpoint de transcrição Vosk com retorno direto no body
- [ ] 4.4 Implementar processamento assíncrono com cleanup automático
- [ ] 4.5 Adicionar endpoint de status/progresso
- [ ] 4.6 Validar modelo Vosk disponível
- [ ] 4.7 Implementar limpeza de arquivos temporários pós-transcrição
- [ ] 4.8 **Implementar queue de processamento para controle de concorrência (NOVO)**
- [ ] 4.9 **Configurar limite de processamentos simultâneos (NOVO)**

### **Fase 5: Serviço OpenAI (Prioridade Média)** ⏱️ 3-4h

- [ ] 5.1 Migrar função `transcribe_audio_openai()` para serviço
- [ ] 5.2 Implementar calculadora de custo
- [ ] 5.3 Criar endpoint de estimativa de custo
- [ ] 5.4 Implementar endpoint de transcrição OpenAI com retorno direto no body
- [ ] 5.5 Adicionar prompt customizável no body
- [ ] 5.6 Implementar chunking automático para áudios longos
- [ ] 5.7 Garantir limpeza automática de arquivos temporários

### **Fase 6: Integração e Testes** ⏱️ 2-3h

- [ ] 6.1 Integrar todos os serviços
- [ ] 6.2 Implementar tratamento de erros global
- [ ] 6.3 Adicionar testes unitários básicos
- [ ] 6.4 Configurar documentação Swagger
- [ ] 6.5 Validar todos os endpoints

### **Fase 7: Documentação e Deploy** ⏱️ 2h

- [ ] 7.1 Criar README da API
- [ ] 7.2 Documentar exemplos de uso
- [ ] 7.3 Configurar Docker (opcional)
- [ ] 7.4 Preparar para deploy

## 📝 Modelos de Dados

### Request Models

```python
class AudioExtractionRequest(BaseModel):
    video_file: UploadFile
    client_name: str
    output_format: str = "wav"

class VoskTranscriptionRequest(BaseModel):
    audio_file: UploadFile
    client_name: str
    language: str = "pt-br"

class OpenAITranscriptionRequest(BaseModel):
    audio_file: UploadFile
    client_name: str
    custom_prompt: Optional[str] = None
    max_seconds: int = 900
    overlap_seconds: int = 15
```

### Response Models

```python
class AudioExtractionResponse(BaseModel):
    audio_id: str
    duration_seconds: float
    file_size_bytes: int
    sample_rate: int
    status: str

```python
class TranscriptionResponse(BaseModel):
    transcription_id: str
    client_name: str
    transcription_text: str
    duration_seconds: float
    method: str  # "vosk" or "openai"
    created_at: datetime
    markdown_download_url: Optional[str] = None  # URL para download do markdown (opcional)
    temp_files_cleaned: bool = True  # Confirma limpeza dos arquivos temporários
```

class CostEstimateResponse(BaseModel):
    duration_minutes: float
    estimated_cost_usd: float
    estimated_cost_brl: float
    parts_needed: int
```

## 🛠️ Tecnologias e Dependências

### Principais

- **FastAPI** - Framework web moderno
- **Uvicorn** - Servidor ASGI
- **Pydantic** - Validação de dados
- **Python-multipart** - Upload de arquivos

### Processamento

- **Vosk** - Transcrição offline
- **OpenAI** - Transcrição online
- **FFmpeg** - Processamento de áudio/vídeo
- **Wave** - Manipulação de arquivos WAV

### Utilitários

- **Python-dotenv** - Variáveis de ambiente
- **Loguru** - Logging avançado
- **Pytest** - Testes (futuro)

## 🚀 Comandos de Execução

```bash
# Desenvolvimento
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Produção
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4

# Docker (futuro)
docker-compose up --build
```

## 📚 URLs da Documentação

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

## 🔒 Considerações de Segurança

- [ ] Validação rigorosa de tipos de arquivo
- [ ] Limite de tamanho de upload
- [ ] Rate limiting por IP
- [ ] Sanitização de nomes de arquivo
- [ ] **Limpeza automática de arquivos temporários (OBRIGATÓRIO)**
- [ ] **Não persistir dados de usuário pós-processamento**
- [ ] Logs de auditoria para transcrições

### **Política de Limpeza de Arquivos**

```python
# Arquivos devem ser removidos automaticamente após:
1. Upload MP4 → Removido após extração de áudio
2. Arquivo WAV → Removido após transcrição completa  
3. Chunks de áudio → Removidos após consolidação
4. Arquivos markdown → Opcionais, apenas se solicitado download
5. Logs temporários → Limpeza diária automática

# Timeline de limpeza:
- Imediato: Após cada etapa do pipeline
- Backup: Job de limpeza a cada 1 hora para arquivos órfãos
- Segurança: Job de limpeza diária para garantir zero persistência
```

## 📈 Próximos Passos

1. **Começar pela Fase 1** - Estrutura base e backup
2. **Focar no Vosk primeiro** - Funcionalidade gratuita
3. **Implementar OpenAI depois** - Funcionalidade premium
4. **Manter compatibilidade** - Não quebrar funcionalidades existentes
5. **Documentar progressivamente** - Atualizar docs a cada fase

## 🎯 Priorização de Desenvolvimento

### **ALTA PRIORIDADE** 🔴

- Backup do código original
- Estrutura FastAPI básica
- Serviço de extração de áudio
- Serviço Vosk de transcrição

### **MÉDIA PRIORIDADE** 🟡

- Serviço OpenAI
- Estimativa de custos
- Processamento assíncrono

### **BAIXA PRIORIDADE** 🟢

- Containerização Docker
- Testes automatizados
- Deploy em produção

---

## 📅 Cronograma Estimado

| Fase | Duração | Dependências |
|------|---------|--------------|
| Fase 1 | 2-3h | - |
| Fase 2 | 1-2h | Fase 1 |
| Fase 3 | 3-4h | Fase 1, 2 |
| Fase 4 | 4-5h | Fase 1, 2, 3 |
| Fase 5 | 3-4h | Fase 1, 2, 3 |
| Fase 6 | 2-3h | Todas anteriores |
| Fase 7 | 2h | Todas anteriores |

### Total Estimado: 17-23 horas

---

*Documento criado em: 2 de agosto de 2025*  
*Última atualização: A ser atualizada conforme progresso*

# 🏛️ Arquitetura da API - Video Transcript Service

## 📐 Visão Geral da Arquitetura

Esta API seguirá uma arquitetura modular baseada em **Clean Architecture** e **Domain-Driven Design (DDD)**, utilizando FastAPI como framework principal.

## 🎯 Princípios Arquiteturais

### 1. **Separação de Responsabilidades**
- Cada serviço tem uma responsabilidade única
- Camadas bem definidas e desacopladas
- Interfaces claras entre componentes

### 2. **Inversão de Dependência**
- Serviços dependem de abstrações, não implementações
- Facilita testes e manutenção
- Permite troca de implementações

### 3. **Escalabilidade**
- Processamento assíncrono para operações longas
- Gerenciamento eficiente de recursos
- Cache quando necessário

### 4. **Zero Persistência (Privacy-First)**
- **Arquivos temporários apenas durante processamento**
- **Limpeza automática obrigatória pós-transcrição**
- **Retorno direto no body da API (padrão)**
- **Download markdown opcional e temporário**
- **Nenhum dado de usuário mantido permanentemente**

## 🏗️ Estrutura de Diretórios Detalhada

```text
transcript-video-api/
├── main.py                           # ⚠️ Código original (backup)
├── main_backup.py                    # 📦 Backup automático
├── requirements.txt                  # 📋 Dependências originais
├── requirements_api.txt              # 🆕 Dependências da API
├── .env.example                      # 🔧 Exemplo de variáveis de ambiente
├── .gitignore                        # 🚫 Arquivos ignorados
├── README_API.md                     # 📚 Documentação da API
├── PLANO_MIGRACAO_API.md            # 📋 Plano de migração
├── ARQUITETURA_API.md               # 🏛️ Este documento
│
├── app/                              # 🚀 Aplicação principal
│   ├── __init__.py
│   ├── main.py                       # 🎯 Ponto de entrada FastAPI
│   ├── config.py                     # ⚙️ Configurações globais
│   ├── dependencies.py               # 🔗 Dependências injetáveis
│   ├── exceptions.py                 # ❌ Exceções customizadas
│   │
│   ├── core/                         # 🧠 Núcleo da aplicação
│   │   ├── __init__.py
│   │   ├── events.py                 # 📢 Eventos de sistema
│   │   ├── middleware.py             # 🔄 Middlewares customizados
│   │   ├── security.py               # 🔒 Autenticação/Autorização JWT
│   │   ├── auth.py                   # 🔐 Sistema de autenticação
│   │   └── queue_manager.py          # 🚦 Gerenciador de filas de processamento
│   │
│   ├── models/                       # 📊 Modelos de dados
│   │   ├── __init__.py
│   │   ├── base.py                   # 🏗️ Modelo base
│   │   ├── audio.py                  # 🎵 Modelos de áudio
│   │   ├── transcription.py          # 📝 Modelos de transcrição
│   │   ├── requests.py               # 📥 Modelos de request
│   │   └── responses.py              # 📤 Modelos de response
│   │
│   ├── services/                     # 🔧 Lógica de negócio
│   │   ├── __init__.py
│   │   ├── interfaces/               # 🔌 Contratos/Interfaces
│   │   │   ├── __init__.py
│   │   │   ├── audio_interface.py
│   │   │   ├── transcription_interface.py
│   │   │   └── storage_interface.py
│   │   │
│   │   ├── audio_service.py          # 🎵 Extração de áudio
│   │   ├── vosk_service.py           # 🗣️ Transcrição Vosk
│   │   ├── openai_service.py         # 🤖 Transcrição OpenAI
│   │   ├── file_service.py           # 📁 Gerenciamento de arquivos
│   │   ├── cleanup_service.py        # 🧹 LIMPEZA AUTOMÁTICA (CRÍTICO)
│   │   ├── auth_service.py           # 🔐 Serviço de autenticação JWT
│   │   ├── queue_service.py          # 🚦 Controle de filas e concorrência
│   │   └── transcription_manager.py  # 🎯 Orquestrador de transcrições
│   │
│   ├── routers/                      # 🛣️ Endpoints da API
│   │   ├── __init__.py
│   │   ├── v1/                       # 📈 Versão 1 da API
│   │   │   ├── __init__.py
│   │   │   ├── auth.py               # 🔐 Endpoints de autenticação JWT
│   │   │   ├── audio.py              # 🎵 Endpoints de áudio
│   │   │   ├── vosk.py               # 🗣️ Endpoints Vosk
│   │   │   ├── openai.py             # 🤖 Endpoints OpenAI
│   │   │   └── health.py             # ❤️ Health checks
│   │   │
│   │   └── api.py                    # 🔗 Agregador de routers
│   │
│   ├── utils/                        # 🛠️ Utilitários
│   │   ├── __init__.py
│   │   ├── audio_utils.py            # 🎵 Utilitários de áudio
│   │   ├── file_utils.py             # 📁 Utilitários de arquivo
│   │   ├── validation_utils.py       # ✅ Validações customizadas
│   │   ├── logging_utils.py          # 📝 Configuração de logs
│   │   └── async_utils.py            # ⚡ Utilitários assíncronos
│   │
│   └── schemas/                      # 📋 Schemas Pydantic
│       ├── __init__.py
│       ├── audio_schemas.py          # 🎵 Schemas de áudio
│       ├── transcription_schemas.py  # 📝 Schemas de transcrição
│       └── common_schemas.py         # 🔄 Schemas comuns
│
├── storage/                          # 💾 Armazenamento
│   ├── temp/                         # ⏰ Arquivos temporários
│   ├── uploads/                      # 📤 Uploads de usuários
│   └── outputs/                      # 📥 Saídas processadas
│
├── tests/                            # 🧪 Testes
│   ├── __init__.py
│   ├── conftest.py                   # ⚙️ Configuração de testes
│   ├── unit/                         # 🔬 Testes unitários
│   ├── integration/                  # 🔗 Testes de integração
│   └── e2e/                          # 🎭 Testes end-to-end
│
├── scripts/                          # 📜 Scripts utilitários
│   ├── setup_models.py               # 🏗️ Setup de modelos Vosk
│   ├── cleanup.py                    # 🧹 Limpeza de arquivos
│   └── health_check.py               # ❤️ Verificação de saúde
│
└── docs/                             # 📚 Documentação
    ├── api/                          # 📖 Docs da API
    ├── deployment/                   # 🚀 Docs de deploy
    └── examples/                     # 💡 Exemplos de uso
```

## 🔧 Camadas da Arquitetura

### 1. **Presentation Layer (Routers)**
```python
# Responsabilidades:
- Receber requisições HTTP
- Validar entrada via Pydantic
- Chamar serviços apropriados
- Retornar respostas formatadas
- Tratamento de erros HTTP
```

### 2. **Business Logic Layer (Services)**
```python
# Responsabilidades:
- Lógica de negócio principal
- Orquestração de operações
- Validações de regras de negócio
- Transformação de dados
- Integração com APIs externas
```

### 3. **Infrastructure Layer (Utils/External)**
```python
# Responsabilidades:
- Acesso a sistemas externos
- Operações de I/O
- Configurações de sistema
- Logging e monitoramento
- Cache e persistência
```

## 🎵 Fluxo de Processamento de Áudio

### Diagrama de Fluxo
```text
📱 Client Request
    ↓
🛣️ Router (Validation)
    ↓
🎯 Transcription Manager
    ↓
🎵 Audio Service → 📁 File Service
    ↓
🗣️ Vosk/OpenAI Service
    ↓
📝 Response Formatting
    ↓
📱 Client Response
```

### Detalhamento por Etapa

#### **1. Upload e Validação**
```python
# POST /api/v1/audio/extract
1. Recebe arquivo MP4
2. Valida formato e tamanho
3. Gera ID único para sessão
4. Salva temporariamente
5. Inicia processamento assíncrono
```

#### **2. Extração de Áudio**
```python
# Audio Service
1. Converte MP4 para WAV
2. Normaliza parâmetros (16kHz, mono)
3. Calcula duração e metadados
4. Remove arquivo de vídeo temporário
5. Retorna informações do áudio
```

#### **3. Transcrição**

```python
# Vosk/OpenAI Service
1. Verifica duração do áudio
2. Divide em chunks se necessário
3. Processa cada chunk
4. Consolida transcrições
5. **REMOVE TODOS OS ARQUIVOS TEMPORÁRIOS**
6. Retorna transcrição no body da resposta
7. Opcionalmente gera link temporário para markdown
```

## 📊 Modelos de Dados Principais

### **AudioFile**
```python
class AudioFile(BaseModel):
    id: str = Field(..., description="ID único do arquivo")
    original_filename: str
    file_path: str
    duration_seconds: float
    sample_rate: int
    channels: int
    file_size_bytes: int
    format: str = "wav"
    created_at: datetime
    status: AudioStatus
```

### **TranscriptionJob**
```python
class TranscriptionJob(BaseModel):
    id: str = Field(..., description="ID único do job")
    audio_id: str
    client_name: str
    method: TranscriptionMethod  # VOSK | OPENAI
    status: JobStatus  # PENDING | PROCESSING | COMPLETED | FAILED
    progress: float = 0.0
    transcription_text: Optional[str] = None
    output_file_path: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None
    metadata: Dict[str, Any] = {}
```

### **CostEstimate**
```python
class CostEstimate(BaseModel):
    audio_duration_minutes: float
    estimated_cost_usd: float
    estimated_cost_brl: float
    parts_needed: int
    max_seconds_per_part: int
    overlap_seconds: int
```

## 🔐 Sistema de Autenticação JWT

### **Fluxo de Autenticação**

```python
# 1. Login/Registro
POST /api/v1/auth/token
{
  "username": "user@example.com",
  "password": "senha_segura"
}

# Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user_id": "uuid-v4",
  "permissions": ["transcribe:vosk", "transcribe:openai"]
}

# 2. Uso da API
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...

# 3. Refresh Token
POST /api/v1/auth/refresh
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### **Estrutura do Token JWT**

```python
# Payload do Access Token
{
  "sub": "user_id",           # Subject (user ID)
  "exp": 1659467400,          # Expiration (1 hora)
  "iat": 1659463800,          # Issued at
  "jti": "token_id",          # JWT ID (para revogação)
  "permissions": [            # Permissões do usuário
    "transcribe:vosk",
    "transcribe:openai",
    "admin:stats"
  ],
  "user_type": "free",        # free, premium, admin
  "rate_limit": {
    "vosk_daily": 10,         # 10 transcrições Vosk por dia
    "openai_monthly": 5,      # 5 transcrições OpenAI por mês
    "concurrent_jobs": 1      # 1 job simultâneo para free users
  }
}
```

## 🚦 Sistema de Controle de Concorrência

### **Estratégia Multi-Nível**

Para o **Vosk (gratuito)**, implementamos controle rigoroso de concorrência para evitar sobrecarga:

```python
# Configurações por tipo de usuário
USER_LIMITS = {
    "free": {
        "max_concurrent_vosk": 1,      # 1 job simultâneo
        "max_daily_vosk": 10,          # 10 transcrições por dia
        "queue_priority": 3,           # Prioridade baixa
        "max_file_size_mb": 100,       # 100MB máximo
        "max_duration_minutes": 60,    # 1 hora máximo
    },
    "premium": {
        "max_concurrent_vosk": 3,      # 3 jobs simultâneos
        "max_daily_vosk": 100,         # 100 transcrições por dia
        "queue_priority": 2,           # Prioridade média
        "max_file_size_mb": 500,       # 500MB máximo
        "max_duration_minutes": 180,   # 3 horas máximo
    },
    "admin": {
        "max_concurrent_vosk": 10,     # 10 jobs simultâneos
        "max_daily_vosk": 1000,        # Ilimitado
        "queue_priority": 1,           # Prioridade alta
        "max_file_size_mb": 1000,      # 1GB máximo
        "max_duration_minutes": 480,   # 8 horas máximo
    }
}
```

### **Queue Manager Implementation**

```python
class QueueManager:
    def __init__(self):
        self.vosk_queue = asyncio.Queue(maxsize=50)  # Fila máxima
        self.active_jobs = {}                        # Jobs ativos por usuário
        self.processing_slots = 3                    # Slots de processamento simultâneo
        
    async def enqueue_vosk_job(self, user_id: str, job: TranscriptionJob):
        # Verifica limites do usuário
        user_limits = await self.get_user_limits(user_id)
        
        # Verifica jobs concurrent por usuário
        active_count = len(self.active_jobs.get(user_id, []))
        if active_count >= user_limits["max_concurrent_vosk"]:
            raise HTTPException(429, "Limite de jobs simultâneos atingido")
        
        # Verifica limite diário
        daily_count = await self.get_daily_usage(user_id, "vosk")
        if daily_count >= user_limits["max_daily_vosk"]:
            raise HTTPException(429, "Limite diário atingido")
        
        # Adiciona à fila com prioridade
        priority = user_limits["queue_priority"]
        await self.vosk_queue.put((priority, job))
        
        return {
            "job_id": job.id,
            "queue_position": await self.get_queue_position(job.id),
            "estimated_wait_seconds": await self.estimate_wait_time()
        }
    
    async def process_queue(self):
        """Background task que processa a fila"""
        while True:
            if len(self.active_jobs) < self.processing_slots:
                try:
                    # Pega próximo job da fila (por prioridade)
                    priority, job = await asyncio.wait_for(
                        self.vosk_queue.get(), timeout=1.0
                    )
                    
                    # Inicia processamento assíncrono
                    task = asyncio.create_task(self.process_job(job))
                    self.active_jobs[job.id] = task
                    
                except asyncio.TimeoutError:
                    continue
            
            await asyncio.sleep(1)  # Check a cada segundo
```

### **Rate Limiting Distribuído**

```python
class RateLimiter:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    async def check_rate_limit(self, user_id: str, action: str) -> bool:
        """Verifica se usuário pode executar ação"""
        limits = await self.get_user_limits(user_id)
        
        if action == "vosk_transcribe":
            # Verifica limite diário
            daily_key = f"rate_limit:daily:vosk:{user_id}:{date.today()}"
            daily_count = await self.redis.get(daily_key) or 0
            
            if int(daily_count) >= limits["max_daily_vosk"]:
                return False
            
            # Incrementa contador
            await self.redis.incr(daily_key)
            await self.redis.expire(daily_key, 86400)  # 24 horas
            
        return True
    
    async def get_user_stats(self, user_id: str) -> dict:
        """Retorna estatísticas de uso do usuário"""
        daily_key = f"rate_limit:daily:vosk:{user_id}:{date.today()}"
        daily_usage = await self.redis.get(daily_key) or 0
        
        limits = await self.get_user_limits(user_id)
        
        return {
            "daily_vosk_usage": int(daily_usage),
            "daily_vosk_limit": limits["max_daily_vosk"],
            "concurrent_jobs": len(self.active_jobs.get(user_id, [])),
            "max_concurrent": limits["max_concurrent_vosk"]
        }
```

## 🔒 Middleware de Segurança

### **JWT Authentication Middleware**

```python
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> User:
    """Extrai e valida token JWT"""
    try:
        payload = jwt.decode(
            credentials.credentials, 
            JWT_SECRET_KEY, 
            algorithms=[JWT_ALGORITHM]
        )
        
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(401, "Token inválido")
        
        # Verifica se token foi revogado
        if await is_token_revoked(payload.get("jti")):
            raise HTTPException(401, "Token revogado")
        
        user = await get_user_by_id(user_id)
        if user is None:
            raise HTTPException(401, "Usuário não encontrado")
        
        return user
        
    except JWTError:
        raise HTTPException(401, "Token inválido")

async def require_permission(permission: str):
    """Decorator para verificar permissões específicas"""
    def permission_dependency(current_user: User = Depends(get_current_user)):
        if permission not in current_user.permissions:
            raise HTTPException(403, f"Permissão '{permission}' necessária")
        return current_user
    return permission_dependency
```

### **Rate Limiting Middleware**

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

# Rate limits por endpoint
@app.post("/api/v1/vosk/transcribe")
@limiter.limit("5/minute")  # 5 requests por minuto por IP
async def transcribe_vosk(
    request: Request,
    current_user: User = Depends(require_permission("transcribe:vosk"))
):
    # Verifica rate limit por usuário (mais específico)
    if not await rate_limiter.check_rate_limit(current_user.id, "vosk_transcribe"):
        raise HTTPException(429, "Limite diário de transcrições atingido")
    
    # Processa transcrição...
```

### **Política Zero Persistência**

O sistema deve garantir que **NENHUM arquivo de usuário seja mantido** após o processamento. Esta é uma exigência fundamental de privacidade e segurança.

### **Pipeline de Limpeza**

```python
# Cleanup automático por etapa:

UPLOAD MP4 → EXTRACT AUDIO → REMOVE MP4
WAV FILE → TRANSCRIBE → REMOVE WAV  
CHUNKS → MERGE → REMOVE CHUNKS
TRANSCRIPT → RETURN BODY → REMOVE TEMP FILES

# Timeline de remoção:
- MP4 original: Removido imediatamente após extração de áudio
- Arquivo WAV: Removido após transcrição completa
- Chunks de áudio: Removidos após consolidação
- Arquivos de log temporários: Removidos após resposta
- Markdown temporário: Removido após 5 minutos (se gerado)
```

### **CleanupService Implementation**

```python
class CleanupService:
    def __init__(self):
        self.temp_files = []
        self.cleanup_jobs = []
    
    def track_file(self, file_path: str, cleanup_after: int = 0):
        """Registra arquivo para limpeza automática"""
        
    def immediate_cleanup(self, file_paths: List[str]):
        """Remove arquivos imediatamente"""
        
    def schedule_cleanup(self, file_paths: List[str], delay_minutes: int):
        """Agenda remoção com delay"""
        
    def emergency_cleanup(self):
        """Limpeza de emergência - remove tudo"""
        
    def orphan_cleanup(self):
        """Job que roda a cada hora removendo arquivos órfãos"""
```

### **Garantias de Segurança**

- ✅ Context manager para garantir limpeza mesmo em caso de erro
- ✅ Job de limpeza backup executado a cada hora
- ✅ Limpeza de emergência em caso de falha
- ✅ Logs de auditoria de todas as remoções
- ✅ Monitoramento de espaço em disco

### 1. **Dependency Injection**
```python
# dependencies.py
def get_audio_service() -> AudioServiceInterface:
    return AudioService()

def get_vosk_service() -> VoskServiceInterface:
    return VoskService()

# router usage
async def extract_audio(
    audio_service: AudioServiceInterface = Depends(get_audio_service)
):
    return await audio_service.extract(...)
```

### 2. **Strategy Pattern**
```python
class TranscriptionManager:
    def __init__(self):
        self.strategies = {
            TranscriptionMethod.VOSK: VoskService(),
            TranscriptionMethod.OPENAI: OpenAIService()
        }
    
    async def transcribe(self, method: TranscriptionMethod, ...):
        return await self.strategies[method].transcribe(...)
```

### 3. **Factory Pattern**
```python
class ServiceFactory:
    @staticmethod
    def create_transcription_service(method: TranscriptionMethod):
        if method == TranscriptionMethod.VOSK:
            return VoskService()
        elif method == TranscriptionMethod.OPENAI:
            return OpenAIService()
        else:
            raise ValueError(f"Unknown method: {method}")
```

## ⚡ Processamento Assíncrono

### **Background Tasks**
```python
# Para operações longas (transcrição)
@router.post("/transcribe")
async def transcribe_audio(
    background_tasks: BackgroundTasks,
    request: TranscriptionRequest
):
    job_id = generate_job_id()
    background_tasks.add_task(
        process_transcription, 
        job_id, 
        request
    )
    return {"job_id": job_id, "status": "processing"}
```

### **Status Tracking**
```python
# Endpoint para acompanhar progresso
@router.get("/transcribe/{job_id}/status")
async def get_transcription_status(job_id: str):
    job = await get_job_status(job_id)
    return {
        "job_id": job_id,
        "status": job.status,
        "progress": job.progress,
        "result": job.result if job.completed else None
    }
```

## 🔒 Segurança e Validação

### **Validações de Arquivo**
```python
ALLOWED_VIDEO_TYPES = {"video/mp4", "video/quicktime"}
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
MAX_DURATION = 7200  # 2 horas

def validate_video_file(file: UploadFile):
    if file.content_type not in ALLOWED_VIDEO_TYPES:
        raise ValidationError("Tipo de arquivo não suportado")
    
    if file.size > MAX_FILE_SIZE:
        raise ValidationError("Arquivo muito grande")
```

### **Rate Limiting**
```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)

@router.post("/transcribe")
@limiter.limit("5/minute")  # 5 transcrições por minuto
async def transcribe_audio(...):
    pass
```

### **Sanitização**
```python
def sanitize_filename(filename: str) -> str:
    # Remove caracteres perigosos
    safe_filename = re.sub(r'[^\w\-_\.]', '_', filename)
    return safe_filename[:100]  # Limita tamanho
```

## 📝 Logging e Monitoramento

### **Structured Logging**
```python
import structlog

logger = structlog.get_logger()

async def transcribe_audio(audio_id: str):
    logger.info(
        "transcription_started",
        audio_id=audio_id,
        method="vosk",
        duration=audio_duration
    )
```

### **Health Checks**
```python
@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "services": {
            "vosk_model": check_vosk_model(),
            "openai_api": await check_openai_api(),
            "storage": check_storage_access()
        }
    }
```

## 🔧 Configurações e Environment

### **Config Class**
```python
class Settings(BaseSettings):
    # API
    app_name: str = "Video Transcript API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # OpenAI
    openai_api_key: Optional[str] = None
    openai_max_seconds: int = 900
    openai_overlap_seconds: int = 15
    
    # Vosk
    vosk_model_path: str = "./model"
    
    # Storage
    temp_dir: str = "./storage/temp"
    upload_dir: str = "./storage/uploads"
    output_dir: str = "./storage/outputs"
    
    # Limits
    max_file_size: int = 500 * 1024 * 1024
    max_duration: int = 7200
    
    class Config:
        env_file = ".env"
```

## 🚀 Deployment e Escalabilidade

### **Docker Configuration**
```yaml
# docker-compose.yml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./storage:/app/storage
      - ./model:/app/model
    restart: unless-stopped
```

### **Horizontal Scaling**
```python
# Para escalar horizontalmente:
1. Usar Redis para cache de sessões
2. Armazenamento externo (S3/MinIO)
3. Queue de processamento (Celery/RQ)
4. Load balancer (nginx/traefik)
```

## 📈 Métricas e Performance

### **Métricas Importantes**
- Tempo de extração de áudio
- Tempo de transcrição por método
- Taxa de erro por serviço
- Uso de recursos (CPU/Memory)
- Throughput de requests

### **Otimizações**
```python
# Cache de modelos em memória
# Processamento em chunks otimizados
# Cleanup automático de arquivos temporários
# Compression de responses
```

## 🎯 Pontos de Extensão Futuros

### **Novos Serviços de Transcrição**
- Azure Speech Service
- Google Cloud Speech-to-Text
- AWS Transcribe

### **Funcionalidades Avançadas**
- Identificação de speakers
- Timestamps precisos
- Tradução automática
- Análise de sentimento

### **Integrações**
- Webhook notifications
- API de callback
- Integração com S3/GCS
- Queue de processamento distribuído

---

## 📋 Checklist de Implementação

### **Phase 1: Core Infrastructure** ✅
- [ ] Estrutura de diretórios
- [ ] Configuração FastAPI básica
- [ ] Modelos base Pydantic
- [ ] Health check endpoint

### **Phase 2: Audio Processing** 🎵
- [ ] Audio service implementation
- [ ] File upload handling
- [ ] Validation and security
- [ ] Temporary file management

### **Phase 3: Transcription Services** 🗣️
- [ ] Vosk service integration
- [ ] OpenAI service integration
- [ ] Background task processing
- [ ] Status tracking

### **Phase 4: API Endpoints** 🛣️
- [ ] Audio endpoints
- [ ] Transcription endpoints
- [ ] Status and monitoring endpoints
- [ ] Error handling

### **Phase 5: Testing & Documentation** 🧪
- [ ] Unit tests
- [ ] Integration tests
- [ ] API documentation
- [ ] Deployment guides

---

*Este documento serve como guia arquitetural completo para a implementação da API de transcrição de vídeos. Deve ser atualizado conforme a evolução do projeto.*

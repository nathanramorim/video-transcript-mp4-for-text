# 🎯 Manual de Implementação - Video Transcript API

## 📋 Visão Geral do Projeto

Este documento é o **orquestrador principal** para implementação completa da API de transcrição de vídeos. Contém todas as instruções, comandos e sequências necessárias para criar uma API moderna, segura e escalável.

### 🎯 **Objetivo Final**
Transformar o script CLI atual em uma API REST robusta com:
- ✅ **Autenticação JWT** com níveis de usuário
- ✅ **Controle de concorrência** para fair usage
- ✅ **Zero persistência** de dados sensíveis
- ✅ **Processamento assíncrono** com filas
- ✅ **Documentação automática** (Swagger)

## 📚 Documentação de Referência

### **Documentos Principais**
| Documento | Propósito | Status |
|-----------|-----------|--------|
| `PLANO_MIGRACAO_API.md` | Plano detalhado de migração | ✅ Completo |
| `ARQUITETURA_API.md` | Arquitetura técnica detalhada | ✅ Completo |
| `DIAGRAMA_ARQUITETURA.md` | Diagramas visuais e fluxos | ✅ Completo |
| `ESPECIFICACAO_ENDPOINTS.md` | Especificação completa de endpoints | ✅ Completo |
| `CONTROLE_CONCORRENCIA.md` | Sistema de filas e rate limiting | ✅ Completo |
| **`IMPLEMENTACAO_MASTER.md`** | **Este documento (orquestrador)** | 🚧 Em execução |

### **Código de Referência**
- `main.py` - Script original (preservado)
- `main_backup.py` - Backup de segurança

## 🗂️ Estrutura Final do Projeto

```
transcript-video-api/
├── 📄 Documentação
│   ├── PLANO_MIGRACAO_API.md
│   ├── ARQUITETURA_API.md  
│   ├── DIAGRAMA_ARQUITETURA.md
│   ├── ESPECIFICACAO_ENDPOINTS.md
│   ├── CONTROLE_CONCORRENCIA.md
│   └── IMPLEMENTACAO_MASTER.md (este arquivo)
│
├── 🔧 Configuração
│   ├── requirements_api.txt
│   ├── .env.example
│   ├── .gitignore
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── 📦 Código Original (Preservado)
│   ├── main.py
│   ├── main_backup.py
│   ├── requirements.txt
│   └── README.md
│
├── 🚀 API Principal
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── dependencies.py
│       ├── exceptions.py
│       │
│       ├── core/
│       │   ├── auth.py
│       │   ├── security.py
│       │   ├── middleware.py
│       │   └── queue_manager.py
│       │
│       ├── models/
│       │   ├── base.py
│       │   ├── user.py
│       │   ├── audio.py
│       │   └── transcription.py
│       │
│       ├── services/
│       │   ├── auth_service.py
│       │   ├── audio_service.py
│       │   ├── vosk_service.py
│       │   ├── openai_service.py
│       │   ├── cleanup_service.py
│       │   └── queue_service.py
│       │
│       ├── routers/
│       │   └── v1/
│       │       ├── auth.py
│       │       ├── audio.py
│       │       ├── vosk.py
│       │       ├── openai.py
│       │       └── health.py
│       │
│       └── utils/
│           ├── audio_utils.py
│           ├── file_utils.py
│           └── logging_utils.py
│
├── 💾 Storage (Temporário)
│   ├── temp/
│   ├── uploads/
│   └── outputs/
│
└── 🧪 Testes
    ├── test_auth.py
    ├── test_vosk.py
    └── test_cleanup.py
```

## 🚀 Implementação Passo a Passo

### **FASE 1: Preparação e Estrutura Base** ⏱️ 2-3h

#### **1.1 Configuração Inicial**

```bash
# 1. Criar estrutura de diretórios
mkdir -p app/{core,models,services,routers/v1,utils,schemas}
mkdir -p storage/{temp,uploads,outputs}
mkdir -p tests

# 2. Criar arquivos base
touch app/__init__.py
touch app/{main,config,dependencies,exceptions}.py
touch app/core/{__init__,auth,security,middleware,queue_manager}.py
touch app/models/{__init__,base,user,audio,transcription}.py
touch app/services/{__init__,auth_service,audio_service,vosk_service,openai_service,cleanup_service,queue_service}.py
touch app/routers/__init__.py
touch app/routers/v1/{__init__,auth,audio,vosk,openai,health}.py
touch app/utils/{__init__,audio_utils,file_utils,logging_utils}.py
```

#### **1.2 Dependências da API**

```bash
# Criar requirements_api.txt
cat > requirements_api.txt << EOF
# Framework principal
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6

# Autenticação e segurança
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-decouple==3.8

# Database e Cache
redis==5.0.1
sqlalchemy==2.0.23
alembic==1.12.1

# Processamento de áudio (do projeto original)
vosk==0.3.45
openai==1.3.7
moviepy==1.0.3

# Utilitários
python-dotenv==1.0.0
pydantic==2.5.0
structlog==23.2.0
slowapi==0.1.9

# Background tasks
celery==5.3.4
flower==2.0.1

# Monitoramento
psutil==5.9.6
prometheus-client==0.19.0

# Testes
pytest==7.4.3
pytest-asyncio==0.21.1
httpx==0.25.2
EOF
```

#### **1.3 Configuração de Ambiente**

```bash
# Criar .env.example
cat > .env.example << EOF
# API Configuration
APP_NAME="Video Transcript API"
APP_VERSION="1.0.0"
DEBUG=false
API_HOST=0.0.0.0
API_PORT=8000

# JWT Configuration
JWT_SECRET_KEY="your-super-secret-jwt-key-change-this-in-production"
JWT_ALGORITHM="HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
JWT_REFRESH_TOKEN_EXPIRE_DAYS=30

# Redis Configuration
REDIS_URL="redis://localhost:6379/0"

# OpenAI Configuration
OPENAI_API_KEY=""
OPENAI_MAX_SECONDS=900
OPENAI_OVERLAP_SECONDS=15
OPENAI_TRANSCRIBE_PROMPT="Transcreva todo o conteúdo do áudio..."

# Vosk Configuration
VOSK_MODEL_PATH="./model"

# Storage Configuration
TEMP_DIR="./storage/temp"
UPLOAD_DIR="./storage/uploads"
OUTPUT_DIR="./storage/outputs"

# Limits Configuration
MAX_FILE_SIZE_MB=500
MAX_DURATION_MINUTES=120
MAX_CONCURRENT_VOSK=3

# Queue Configuration
QUEUE_MAX_SIZE=50
CLEANUP_INTERVAL_HOURS=1

# User Limits
FREE_DAILY_LIMIT=10
FREE_CONCURRENT_LIMIT=1
PREMIUM_DAILY_LIMIT=50
PREMIUM_CONCURRENT_LIMIT=3
EOF

# Copiar para .env real
cp .env.example .env
```

#### **1.4 Configuração Docker**

```bash
# Criar Dockerfile
cat > Dockerfile << EOF
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \\
    ffmpeg \\
    redis-server \\
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements_api.txt .
RUN pip install -r requirements_api.txt

# Copiar código
COPY . .

# Criar diretórios necessários
RUN mkdir -p storage/{temp,uploads,outputs}

# Expor porta
EXPOSE 8000

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

# Criar docker-compose.yml
cat > docker-compose.yml << EOF
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_URL=redis://redis:6379/0
    volumes:
      - ./storage:/app/storage
      - ./model:/app/model
    depends_on:
      - redis
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    restart: unless-stopped

  flower:
    build: .
    command: celery -A app.core.celery flower
    ports:
      - "5555:5555"
    environment:
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - redis
    restart: unless-stopped
EOF
```

### **FASE 2: Modelos e Configurações** ⏱️ 2-3h

#### **2.1 Configuração Principal**

```python
# app/config.py
from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # API
    app_name: str = "Video Transcript API"
    app_version: str = "1.0.0"
    debug: bool = False
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    
    # JWT
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60
    jwt_refresh_token_expire_days: int = 30
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # OpenAI
    openai_api_key: Optional[str] = None
    openai_max_seconds: int = 900
    openai_overlap_seconds: int = 15
    openai_transcribe_prompt: str = "Transcreva todo o conteúdo..."
    
    # Vosk
    vosk_model_path: str = "./model"
    
    # Storage
    temp_dir: str = "./storage/temp"
    upload_dir: str = "./storage/uploads"
    output_dir: str = "./storage/outputs"
    
    # Limits
    max_file_size_mb: int = 500
    max_duration_minutes: int = 120
    max_concurrent_vosk: int = 3
    
    # Queue
    queue_max_size: int = 50
    cleanup_interval_hours: int = 1
    
    # User limits
    free_daily_limit: int = 10
    free_concurrent_limit: int = 1
    premium_daily_limit: int = 50
    premium_concurrent_limit: int = 3

    class Config:
        env_file = ".env"

settings = Settings()
```

#### **2.2 Modelos Base**

```python
# app/models/base.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid

class BaseModelWithId(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

class ResponseModel(BaseModel):
    success: bool = True
    message: str = "Success"
    data: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
```

#### **2.3 Modelos de Usuário**

```python
# app/models/user.py
from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .base import BaseModelWithId

class UserType(str, Enum):
    FREE = "free"
    PREMIUM = "premium"
    ADMIN = "admin"

class UserLimits(BaseModel):
    max_concurrent_vosk: int
    max_daily_vosk: int
    max_monthly_vosk: int
    max_concurrent_openai: int
    max_monthly_openai: int
    max_file_size_mb: int
    max_duration_minutes: int
    queue_priority: int

class User(BaseModelWithId):
    email: EmailStr
    username: str
    user_type: UserType = UserType.FREE
    permissions: List[str] = []
    limits: UserLimits
    is_active: bool = True
    hashed_password: str

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    user_type: UserType = UserType.FREE

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    user_id: str
    user_type: UserType
    permissions: List[str]
    limits: UserLimits
```

### **FASE 3: Autenticação e Segurança** ⏱️ 3-4h

#### **3.1 Sistema JWT**

```python
# app/core/auth.py
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from app.config import settings
from app.models.user import User, UserType, UserLimits

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

USER_CONFIGS = {
    UserType.FREE: UserLimits(
        max_concurrent_vosk=1,
        max_daily_vosk=10,
        max_monthly_vosk=100,
        max_concurrent_openai=0,
        max_monthly_openai=0,
        max_file_size_mb=100,
        max_duration_minutes=60,
        queue_priority=3
    ),
    UserType.PREMIUM: UserLimits(
        max_concurrent_vosk=3,
        max_daily_vosk=50,
        max_monthly_vosk=1000,
        max_concurrent_openai=2,
        max_monthly_openai=100,
        max_file_size_mb=500,
        max_duration_minutes=180,
        queue_priority=2
    ),
    UserType.ADMIN: UserLimits(
        max_concurrent_vosk=10,
        max_daily_vosk=999999,
        max_monthly_vosk=999999,
        max_concurrent_openai=5,
        max_monthly_openai=999999,
        max_file_size_mb=1000,
        max_duration_minutes=480,
        queue_priority=1
    )
}

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.jwt_access_token_expire_minutes)
    
    to_encode.update({"exp": expire, "iat": datetime.utcnow()})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def create_refresh_token(user_id: str):
    expire = datetime.utcnow() + timedelta(days=settings.jwt_refresh_token_expire_days)
    to_encode = {"sub": user_id, "exp": expire, "type": "refresh"}
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def verify_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
```

### **FASE 4: Serviços Core** ⏱️ 4-5h

#### **4.1 Serviço de Autenticação**

```python
# app/services/auth_service.py
import redis
import json
from typing import Optional
from app.models.user import User, UserCreate, UserLogin, Token, UserType
from app.core.auth import verify_password, get_password_hash, create_access_token, create_refresh_token, USER_CONFIGS
from app.config import settings
from fastapi import HTTPException, status

class AuthService:
    def __init__(self):
        self.redis_client = redis.from_url(settings.redis_url)
        
    async def create_user(self, user_data: UserCreate) -> User:
        """Criar novo usuário"""
        # Verificar se usuário já existe
        existing_user = await self.get_user_by_username(user_data.username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Usuário já existe"
            )
        
        # Criar usuário
        user = User(
            email=user_data.email,
            username=user_data.username,
            user_type=user_data.user_type,
            hashed_password=get_password_hash(user_data.password),
            limits=USER_CONFIGS[user_data.user_type],
            permissions=self._get_permissions_for_user_type(user_data.user_type)
        )
        
        # Salvar no Redis
        await self._save_user(user)
        return user
    
    async def authenticate_user(self, login_data: UserLogin) -> Token:
        """Autenticar usuário e retornar tokens"""
        user = await self.get_user_by_username(login_data.username)
        if not user or not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas"
            )
        
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário inativo"
            )
        
        # Criar tokens
        access_token = create_access_token(
            data={
                "sub": user.id,
                "username": user.username,
                "user_type": user.user_type,
                "permissions": user.permissions
            }
        )
        refresh_token = create_refresh_token(user.id)
        
        # Salvar refresh token
        await self.redis_client.setex(
            f"refresh_token:{user.id}",
            settings.jwt_refresh_token_expire_days * 24 * 3600,
            refresh_token
        )
        
        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=settings.jwt_access_token_expire_minutes * 60,
            user_id=user.id,
            user_type=user.user_type,
            permissions=user.permissions,
            limits=user.limits
        )
    
    async def get_user_by_username(self, username: str) -> Optional[User]:
        """Buscar usuário por username"""
        user_data = await self.redis_client.get(f"user:username:{username}")
        if user_data:
            return User(**json.loads(user_data))
        return None
    
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Buscar usuário por ID"""
        user_data = await self.redis_client.get(f"user:id:{user_id}")
        if user_data:
            return User(**json.loads(user_data))
        return None
    
    async def _save_user(self, user: User):
        """Salvar usuário no Redis"""
        user_json = user.model_dump_json()
        await self.redis_client.set(f"user:id:{user.id}", user_json)
        await self.redis_client.set(f"user:username:{user.username}", user_json)
    
    def _get_permissions_for_user_type(self, user_type: UserType) -> list:
        """Retornar permissões baseadas no tipo de usuário"""
        if user_type == UserType.FREE:
            return ["transcribe:vosk"]
        elif user_type == UserType.PREMIUM:
            return ["transcribe:vosk", "transcribe:openai"]
        elif user_type == UserType.ADMIN:
            return ["transcribe:vosk", "transcribe:openai", "admin:stats", "admin:users"]
        return []
```

### **FASE 5: Sistema de Filas** ⏱️ 3-4h

#### **5.1 Queue Manager**

```python
# app/core/queue_manager.py
import asyncio
import time
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from app.models.user import User
from app.models.transcription import TranscriptionJob
from app.config import settings
import redis

@dataclass
class QueueItem:
    priority: int
    timestamp: float
    user_id: str
    job: TranscriptionJob

@dataclass
class QueueResponse:
    job_id: str
    status: str
    queue_position: int
    estimated_wait_minutes: int
    message: str

class QueueManager:
    def __init__(self):
        self.redis_client = redis.from_url(settings.redis_url)
        self.max_concurrent = settings.max_concurrent_vosk
        self.active_jobs: Dict[str, List[str]] = {}
        self.processing_times: List[float] = []
        
        # Filas por prioridade
        self.queues = {
            1: asyncio.PriorityQueue(),  # Admin
            2: asyncio.PriorityQueue(),  # Premium
            3: asyncio.PriorityQueue(),  # Free
        }
    
    async def enqueue_job(self, user: User, job: TranscriptionJob) -> QueueResponse:
        """Adiciona job à fila com verificações"""
        
        # Verificar limites de concorrência
        user_active_jobs = len(self.active_jobs.get(user.id, []))
        if user_active_jobs >= user.limits.max_concurrent_vosk:
            raise HTTPException(
                status_code=429,
                detail={
                    "error": "concurrent_limit_exceeded",
                    "current_jobs": user_active_jobs,
                    "max_concurrent": user.limits.max_concurrent_vosk
                }
            )
        
        # Verificar limite diário
        daily_usage = await self._get_daily_usage(user.id)
        if daily_usage >= user.limits.max_daily_vosk:
            raise HTTPException(
                status_code=429,
                detail={
                    "error": "daily_limit_exceeded",
                    "daily_used": daily_usage,
                    "daily_limit": user.limits.max_daily_vosk
                }
            )
        
        # Adicionar à fila
        queue_item = QueueItem(
            priority=user.limits.queue_priority,
            timestamp=time.time(),
            user_id=user.id,
            job=job
        )
        
        await self.queues[user.limits.queue_priority].put(queue_item)
        
        # Calcular posição e tempo estimado
        position = await self._calculate_queue_position(user.limits.queue_priority)
        estimated_wait = await self._estimate_wait_time(position)
        
        return QueueResponse(
            job_id=job.id,
            status="queued",
            queue_position=position,
            estimated_wait_minutes=estimated_wait,
            message=f"Job adicionado à fila de prioridade {user.limits.queue_priority}"
        )
    
    async def process_queues(self):
        """Background task que processa as filas"""
        while True:
            # Verificar slots disponíveis
            if len(self.active_jobs) < self.max_concurrent:
                
                # Processar por prioridade (1 > 2 > 3)
                job_item = None
                for priority in [1, 2, 3]:
                    if not self.queues[priority].empty():
                        job_item = await self.queues[priority].get()
                        break
                
                if job_item:
                    # Iniciar processamento
                    task = asyncio.create_task(
                        self._process_transcription_job(job_item)
                    )
                    
                    # Registrar job ativo
                    if job_item.user_id not in self.active_jobs:
                        self.active_jobs[job_item.user_id] = []
                    self.active_jobs[job_item.user_id].append(job_item.job.id)
                    
                    # Cleanup quando completar
                    task.add_done_callback(
                        lambda t, uid=job_item.user_id, jid=job_item.job.id: 
                        self._cleanup_job(uid, jid)
                    )
            
            await asyncio.sleep(1)  # Check a cada segundo
    
    async def _process_transcription_job(self, queue_item: QueueItem):
        """Processar job de transcrição"""
        start_time = time.time()
        
        try:
            # Aqui seria chamado o serviço de transcrição
            # Por exemplo: await vosk_service.transcribe(queue_item.job)
            
            # Simular processamento por enquanto
            await asyncio.sleep(10)  # Simula processamento
            
            processing_time = time.time() - start_time
            self.processing_times.append(processing_time)
            
            # Manter apenas últimos 100 tempos
            if len(self.processing_times) > 100:
                self.processing_times = self.processing_times[-100:]
                
        except Exception as e:
            print(f"Erro no processamento: {e}")
        
    def _cleanup_job(self, user_id: str, job_id: str):
        """Remove job da lista de ativos"""
        if user_id in self.active_jobs:
            if job_id in self.active_jobs[user_id]:
                self.active_jobs[user_id].remove(job_id)
            if not self.active_jobs[user_id]:
                del self.active_jobs[user_id]
    
    async def _get_daily_usage(self, user_id: str) -> int:
        """Obter uso diário do usuário"""
        from datetime import date
        today = date.today().isoformat()
        key = f"daily_usage:vosk:{user_id}:{today}"
        usage = await self.redis_client.get(key)
        return int(usage) if usage else 0
    
    async def _calculate_queue_position(self, user_priority: int) -> int:
        """Calcular posição na fila"""
        position = 0
        for priority in range(1, user_priority + 1):
            position += self.queues[priority].qsize()
        return position
    
    async def _estimate_wait_time(self, position: int) -> int:
        """Estimar tempo de espera em minutos"""
        if position == 0:
            return 0
        
        avg_time = sum(self.processing_times[-10:]) / len(self.processing_times[-10:]) if self.processing_times else 120
        available_slots = max(1, self.max_concurrent - len(self.active_jobs))
        
        estimated_seconds = (position / available_slots) * avg_time
        return int(estimated_seconds / 60)

# Instância global
queue_manager = QueueManager()
```

### **FASE 6: Endpoints da API** ⏱️ 4-5h

#### **6.1 Endpoints de Autenticação**

```python
# app/routers/v1/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.models.user import UserCreate, UserLogin, Token, User
from app.services.auth_service import AuthService
from app.core.security import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=dict)
async def register(user_data: UserCreate):
    """Registrar novo usuário"""
    auth_service = AuthService()
    user = await auth_service.create_user(user_data)
    return {
        "message": "Usuário criado com sucesso",
        "user_id": user.id,
        "user_type": user.user_type
    }

@router.post("/token", response_model=Token)
async def login(login_data: UserLogin):
    """Login e obtenção de tokens JWT"""
    auth_service = AuthService()
    return await auth_service.authenticate_user(login_data)

@router.post("/refresh", response_model=dict)
async def refresh_token(refresh_token: str):
    """Renovar access token"""
    # Implementar renovação de token
    pass

@router.get("/me", response_model=dict)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Obter informações do usuário atual"""
    return {
        "user_id": current_user.id,
        "username": current_user.username,
        "user_type": current_user.user_type,
        "permissions": current_user.permissions,
        "limits": current_user.limits
    }
```

#### **6.2 Endpoints do Vosk**

```python
# app/routers/v1/vosk.py
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from app.models.user import User
from app.core.security import get_current_user, require_permission
from app.core.queue_manager import queue_manager
from app.services.vosk_service import VoskService

router = APIRouter(prefix="/vosk", tags=["Vosk Transcription"])

@router.post("/transcribe")
async def transcribe_vosk(
    video_file: UploadFile = File(...),
    client_name: str = "",
    return_markdown: bool = False,
    current_user: User = Depends(require_permission("transcribe:vosk"))
):
    """Transcrição usando Vosk (gratuita)"""
    
    # Validações de arquivo
    if video_file.content_type not in ["video/mp4", "video/quicktime"]:
        raise HTTPException(400, "Tipo de arquivo não suportado")
    
    if video_file.size > current_user.limits.max_file_size_mb * 1024 * 1024:
        raise HTTPException(413, "Arquivo muito grande")
    
    # Criar job de transcrição
    job = TranscriptionJob(
        file_name=video_file.filename,
        client_name=client_name,
        user_id=current_user.id,
        method="vosk",
        file_size_mb=video_file.size / (1024 * 1024)
    )
    
    # Adicionar à fila
    queue_response = await queue_manager.enqueue_job(current_user, job)
    
    return {
        "job_id": job.id,
        "status": queue_response.status,
        "queue_position": queue_response.queue_position,
        "estimated_wait_minutes": queue_response.estimated_wait_minutes,
        "message": queue_response.message
    }

@router.get("/queue/status")
async def get_queue_status(current_user: User = Depends(get_current_user)):
    """Status da fila de processamento"""
    return {
        "queue_sizes": {
            "high_priority": queue_manager.queues[1].qsize(),
            "medium_priority": queue_manager.queues[2].qsize(),
            "low_priority": queue_manager.queues[3].qsize()
        },
        "active_jobs": len(queue_manager.active_jobs),
        "max_concurrent": queue_manager.max_concurrent,
        "user_active_jobs": len(queue_manager.active_jobs.get(current_user.id, []))
    }
```

### **FASE 7: App Principal** ⏱️ 1-2h

#### **7.1 FastAPI App**

```python
# app/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import asyncio
import uvicorn

from app.config import settings
from app.routers.v1 import auth, vosk, openai, health
from app.core.queue_manager import queue_manager
from app.exceptions import CustomHTTPException

# Criar app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API para transcrição de vídeos usando Vosk e OpenAI",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(vosk.router, prefix="/api/v1")
app.include_router(openai.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")

# Exception handlers
@app.exception_handler(CustomHTTPException)
async def custom_exception_handler(request: Request, exc: CustomHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

# Eventos de startup/shutdown
@app.on_event("startup")
async def startup_event():
    """Inicializar serviços"""
    # Iniciar queue processor
    asyncio.create_task(queue_manager.process_queues())
    print(f"🚀 {settings.app_name} v{settings.app_version} iniciado!")

@app.on_event("shutdown")
async def shutdown_event():
    """Finalizar serviços"""
    print("⏹️ Finalizando serviços...")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "docs": "/docs"
    }

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug
    )
```

## 🚀 Comandos de Execução

### **Desenvolvimento Local**

```bash
# 1. Instalar dependências
pip install -r requirements_api.txt

# 2. Configurar ambiente
cp .env.example .env
# Editar .env com suas configurações

# 3. Iniciar Redis (se não usar Docker)
redis-server

# 4. Iniciar API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 5. Acessar documentação
# http://localhost:8000/docs
```

### **Produção com Docker**

```bash
# 1. Build e start
docker-compose up --build -d

# 2. Verificar logs
docker-compose logs -f api

# 3. Acessar API
# http://localhost:8000

# 4. Monitoramento (Flower)
# http://localhost:5555
```

### **Testes**

```bash
# Executar testes
pytest tests/ -v

# Teste com cobertura
pytest tests/ --cov=app --cov-report=html

# Teste específico
pytest tests/test_auth.py::test_create_user -v
```

## 📊 Checklist de Implementação

### **✅ FASE 1: Preparação** (2-3h)
- [ ] Estrutura de diretórios criada
- [ ] Dependências configuradas
- [ ] Docker configurado
- [ ] Environment configurado

### **✅ FASE 2: Modelos** (2-3h)
- [ ] Configurações (config.py)
- [ ] Modelos base (base.py)
- [ ] Modelos de usuário (user.py)
- [ ] Modelos de transcrição

### **✅ FASE 3: Autenticação** (3-4h)
- [ ] Sistema JWT (auth.py)
- [ ] Serviço de autenticação
- [ ] Middleware de segurança
- [ ] Tipos de usuário configurados

### **✅ FASE 4: Serviços Core** (4-5h)
- [ ] Auth Service implementado
- [ ] Queue Manager implementado
- [ ] Rate Limiting implementado
- [ ] Background tasks configuradas

### **✅ FASE 5: Sistema de Filas** (3-4h)
- [ ] Filas por prioridade
- [ ] Controle de concorrência
- [ ] Verificação de limites
- [ ] Estimativa de tempo

### **✅ FASE 6: Endpoints** (4-5h)
- [ ] Endpoints de autenticação
- [ ] Endpoints do Vosk
- [ ] Endpoints do OpenAI
- [ ] Health checks

### **✅ FASE 7: App Principal** (1-2h)
- [ ] FastAPI app configurada
- [ ] Middlewares configurados
- [ ] Exception handlers
- [ ] Documentação automática

## 🎯 Próximos Passos Após Implementação

### **Funcionalidades Avançadas**
1. **Monitoramento** - Prometheus + Grafana
2. **Logs Estruturados** - ELK Stack
3. **Backup Automático** - Configurações e dados
4. **CI/CD Pipeline** - GitHub Actions
5. **Testes E2E** - Conjunto completo de testes

### **Otimizações**
1. **Cache** - Redis para resultados frequentes
2. **CDN** - Para arquivos estáticos
3. **Load Balancing** - Múltiplas instâncias
4. **Database** - Migração para PostgreSQL
5. **Message Queue** - RabbitMQ ou Apache Kafka

### **Segurança Adicional**
1. **Rate Limiting** - Por IP e usuário
2. **WAF** - Web Application Firewall
3. **SSL/TLS** - Certificados automáticos
4. **Audit Logs** - Rastreamento detalhado
5. **Backup Encryption** - Dados criptografados

---

## 📝 Conclusão

Este documento orquestrador fornece um roadmap completo para implementar a API de transcrição de vídeos. Seguindo estas instruções passo a passo, você terá uma API moderna, segura e escalável.

**Tempo Total Estimado: 20-25 horas**

**Próximo Passo: Começar pela FASE 1 - Preparação e Estrutura Base**

🚀 **Pronto para implementar? Let's code!**

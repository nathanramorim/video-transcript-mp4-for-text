# 🔄 Especificação de Endpoints - Zero Persistência

## 📋 Resumo Executivo

Todos os endpoints da API seguem o princípio de **Zero Persistência**, onde:
- ✅ Arquivos são processados temporariamente
- ✅ Transcrições retornam diretamente no body JSON
- ✅ Links de markdown são opcionais e temporários (5min)
- ✅ Nenhum dado é persistido após processamento

## 🛣️ Endpoints Detalhados

### **🔐 POST /api/v1/auth/token**

Autenticação JWT para acesso à API

#### Request
```json
{
  "username": "user@example.com",
  "password": "senha_segura"
}
```

#### Response (200 OK)
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user_id": "uuid-v4",
  "user_type": "free",
  "permissions": ["transcribe:vosk"],
  "limits": {
    "daily_vosk": 10,
    "concurrent_jobs": 1,
    "max_file_size_mb": 100
  }
}
```

---

### **🔄 POST /api/v1/auth/refresh**

Renovação de token JWT

#### Request
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Response (200 OK)
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "expires_in": 3600
}
```

---

### **🚦 GET /api/v1/user/stats**

Estatísticas de uso do usuário autenticado

#### Headers
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

#### Response (200 OK)
```json
{
  "user_id": "uuid-v4",
  "user_type": "free",
  "usage": {
    "daily_vosk": 3,
    "daily_vosk_limit": 10,
    "monthly_openai": 0,
    "monthly_openai_limit": 5
  },
  "current_jobs": {
    "active": 0,
    "queued": 0,
    "max_concurrent": 1
  },
  "queue_status": {
    "vosk_queue_size": 5,
    "estimated_wait_minutes": 12
  }
}
```

---

### **🎵 POST /api/v1/vosk/transcribe**

Transcrição offline usando Vosk (gratuita, privada)

#### Request
```json
{
  "video_file": "file_upload",
  "client_name": "NOME_CLIENTE",
  "return_markdown": false,  // opcional, default: false
  "language": "pt-br"        // opcional, default: pt-br
}
```

#### Headers
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

#### Response (200 OK)
```json
{
  "transcription_id": "uuid-v4",
  "client_name": "NOME_CLIENTE", 
  "method": "vosk",
  "duration_seconds": 245.8,
  "transcription_text": "Texto completo da transcrição...",
  "processing_time_seconds": 12.3,
  "chunks_processed": 3,
  "queue_info": {
    "was_queued": true,
    "wait_time_seconds": 45,
    "queue_position": 2
  },
  "markdown_download_url": null, // ou URL temporária se solicitado
  "temp_files_cleaned": true,
  "created_at": "2025-08-02T22:30:00Z"
}
```

#### Response (429 Too Many Requests)
```json
{
  "error": "rate_limit_exceeded",
  "message": "Limite diário de transcrições atingido",
  "limits": {
    "daily_used": 10,
    "daily_limit": 10,
    "resets_at": "2025-08-03T00:00:00Z"
  }
}
```

#### Response (429 Too Many Requests - Concurrent)
```json
{
  "error": "concurrent_limit_exceeded", 
  "message": "Limite de jobs simultâneos atingido",
  "current_jobs": 1,
  "max_concurrent": 1,
  "queue_info": {
    "position": 3,
    "estimated_wait_minutes": 8
  }
}
```

#### Comportamento Interno
```text
1. Upload MP4 → Temp storage com session ID
2. Extract audio → Remove MP4 imediatamente  
3. Chunk audio → Remove WAV original
4. Process chunks → Remove cada chunk após processamento
5. Merge results → Remove arquivos restantes
6. Return JSON → Cleanup final garantido
7. Optional markdown → Auto-expire em 5min
```

---

### **🤖 POST /api/v1/openai/transcribe**

Transcrição online usando OpenAI (paga, alta precisão)

#### Request
```json
{
  "video_file": "file_upload",
  "client_name": "NOME_CLIENTE",
  "custom_prompt": "Instruções específicas...", // opcional
  "return_markdown": false,  // opcional, default: false
  "max_seconds": 900,        // opcional, default: 900
  "overlap_seconds": 15      // opcional, default: 15
}
```

#### Response (200 OK)
```json
{
  "transcription_id": "uuid-v4",
  "client_name": "NOME_CLIENTE",
  "method": "openai", 
  "duration_seconds": 1200.5,
  "transcription_text": "Texto completo da transcrição...",
  "processing_time_seconds": 45.2,
  "chunks_processed": 2,
  "estimated_cost_usd": 0.072,
  "estimated_cost_brl": 0.396,
  "markdown_download_url": null, // ou URL temporária se solicitado
  "temp_files_cleaned": true,
  "created_at": "2025-08-02T22:30:00Z"
}
```

---

### **💰 POST /api/v1/openai/estimate-cost**

Estimativa de custo antes da transcrição

#### Request
```json
{
  "video_file": "file_upload"
}
```

#### Response (200 OK)
```json
{
  "duration_minutes": 20.1,
  "estimated_cost_usd": 0.1206,
  "estimated_cost_brl": 0.6633,
  "parts_needed": 2,
  "max_seconds_per_part": 900,
  "overlap_seconds": 15,
  "temp_file_cleaned": true, // arquivo foi removido após análise
  "analysis_time_seconds": 2.1
}
```

---

### **📥 GET /api/v1/download/markdown/{token}**

Download temporário de arquivo markdown (opcional)

#### Response (200 OK)
```markdown
# Transcrição de Reunião - NOME_CLIENTE

**Arquivo de origem:** video.mp4
**Método:** vosk
**Duração:** 4m 5s
**Data:** 2025-08-02 22:30:00

## Transcrição

Conteúdo completo da transcrição...
```

#### Headers
```
Content-Type: text/markdown
Content-Disposition: attachment; filename="transcricao-NOME_CLIENTE.md"
X-Expires-At: 2025-08-02T22:35:00Z  // 5 minutos após geração
```

#### Comportamento
- ⏰ Link expira em 5 minutos
- 🗑️ Arquivo removido automaticamente após expiração
- 🔄 Apenas 1 download permitido por token
- ❌ 404 após expiração ou download

---

### **❤️ GET /api/v1/health**

Verificação de saúde do sistema

#### Response (200 OK)
```json
{
  "status": "healthy",
  "timestamp": "2025-08-02T22:30:00Z",
  "services": {
    "vosk_model": {
      "status": "available",
      "model_path": "/app/model",
      "language": "pt-br"
    },
    "openai_api": {
      "status": "available", 
      "api_key_configured": true,
      "last_check": "2025-08-02T22:29:00Z"
    },
    "storage": {
      "status": "healthy",
      "temp_dir_size_mb": 0,  // sempre próximo de 0 devido à limpeza
      "free_space_gb": 45.2
    },
    "cleanup_service": {
      "status": "active",
      "last_cleanup": "2025-08-02T22:28:00Z",
      "files_cleaned_today": 156,
      "orphaned_files": 0
    }
  },
  "version": "1.0.0"
}
```

---

### **📊 GET /api/v1/stats**

Estatísticas do sistema (sem dados sensíveis)

#### Response (200 OK)
```json
{
  "period": "last_24h",
  "transcriptions": {
    "total": 47,
    "vosk": 31,
    "openai": 16,
    "avg_duration_seconds": 456.2,
    "avg_processing_time_seconds": 23.1
  },
  "cleanup": {
    "files_processed": 423,
    "files_cleaned": 423,  // deve ser sempre igual
    "cleanup_efficiency": 100.0,
    "avg_cleanup_time_ms": 12.3
  },
  "errors": {
    "total": 2,
    "file_format": 1,
    "openai_api": 1,
    "cleanup_failures": 0  // deve ser sempre 0
  },
  "storage": {
    "peak_usage_mb": 1.2,   // máximo de storage temporário usado
    "current_usage_mb": 0.0, // sempre próximo de 0
    "files_orphaned": 0      // deve ser sempre 0
  }
}
```

## 🔒 Validações e Segurança

### **Validação de Upload**
```python
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
MAX_DURATION = 7200  # 2 horas
ALLOWED_TYPES = ["video/mp4", "video/quicktime"]

def validate_upload(file: UploadFile):
    # Verificações críticas antes de aceitar arquivo
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(413, "Arquivo muito grande")
    
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(415, "Tipo de arquivo não suportado")
    
    # Scan básico de segurança
    if not is_safe_file(file):
        raise HTTPException(400, "Arquivo rejeitado por segurança")
```

### **Rate Limiting**
```python
# Por IP:
- 10 uploads por hora
- 5 transcrições simultâneas máximo
- 1GB total de uploads por dia

# Global:
- 100 transcrições por hora
- Proteção DDoS automática
```

### **Auditoria (Sem dados sensíveis)**
```python
# Logs de auditoria incluem apenas:
- Timestamp da operação
- Tamanho do arquivo (não conteúdo)
- Duração do processamento  
- Método usado (Vosk/OpenAI)
- Status de limpeza (sucesso/falha)
- IP hash (para rate limiting)

# NÃO inclui:
- Nome do arquivo original
- Conteúdo da transcrição
- Dados pessoais
- Client_name específico
```

## 🧹 Garantias de Limpeza

### **Context Managers**
```python
@contextmanager
def temp_audio_processor(video_file: UploadFile):
    temp_files = []
    try:
        # Processa arquivo
        yield temp_files
    finally:
        # SEMPRE limpa, mesmo com erro
        cleanup_service.immediate_cleanup(temp_files)
```

### **Background Cleanup Jobs**
```python
# Job executado a cada hora
@scheduler.scheduled_job("interval", hours=1)
def orphan_cleanup():
    removed = cleanup_service.remove_orphaned_files()
    logger.info(f"Cleanup job: {removed} orphaned files removed")

# Job de emergência executado diariamente  
@scheduler.scheduled_job("cron", hour=2)
def emergency_cleanup():
    cleanup_service.emergency_full_cleanup()
    logger.info("Emergency cleanup completed")
```

### **Monitoring e Alertas**
```python
# Alerta se temp folder > 100MB
# Alerta se cleanup falhar 3 vezes consecutivas
# Alerta se arquivos órfãos > 0 por mais de 1 hora
# Dashboard em tempo real de uso de storage
```

---

## 🎯 Resumo dos Benefícios

### **Para o Usuário**
- ✅ **Privacidade máxima** - Nenhum arquivo fica armazenado
- ✅ **Resposta imediata** - Transcrição retorna no body da API
- ✅ **Flexibilidade** - Escolha entre Vosk (grátis) ou OpenAI (premium)
- ✅ **Transparência** - Estimativa de custo antes de processar

### **Para o Sistema**  
- ✅ **Segurança** - Zero persistência elimina vazamentos
- ✅ **Performance** - Limpeza automática mantém sistema ágil
- ✅ **Escalabilidade** - Sem acúmulo de dados desnecessários
- ✅ **Compliance** - Atende LGPD e outras regulamentações

### **Para Operação**
- ✅ **Monitoramento** - Métricas em tempo real de limpeza
- ✅ **Auditoria** - Logs completos sem dados sensíveis
- ✅ **Manutenção** - Sistema auto-sustentável
- ✅ **Custo** - Redução de storage e backup

---

*Esta especificação garante que a API seja segura, eficiente e respeitosa à privacidade dos usuários, seguindo as melhores práticas de desenvolvimento moderno.*

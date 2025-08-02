# 🎨 Diagrama Visual da Arquitetura

## 🏗️ Visão Geral em Camadas

```text
┌─────────────────────────────────────────────────────────────────┐
│                    🌐 CLIENT LAYER                              │
│  📱 Mobile App   🖥️ Web Browser   🔧 API Client   📊 Dashboard │
└─────────────────────────────────────────────────────────────────┘
                                   │
                           📡 HTTP/REST API
                                   │
┌─────────────────────────────────────────────────────────────────┐
│                   🛣️ PRESENTATION LAYER                        │
│                        (FastAPI Routers)                       │
│                                                                 │
│  📤 /upload    🎵 /audio    🗣️ /vosk    🤖 /openai    ❤️ /health │
│     │              │           │           │              │     │
│     └──────────────┼───────────┼───────────┼──────────────┘     │
└─────────────────────────────────────────────────────────────────┘
                                   │
                           🔄 Dependency Injection
                                   │
┌─────────────────────────────────────────────────────────────────┐
│                   🧠 BUSINESS LOGIC LAYER                       │
│                         (Services)                             │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────┐ │
│  │ 🎯 Manager  │  │ 🎵 Audio    │  │ 🗣️ Vosk     │  │ 🤖 OpenAI│ │
│  │ Service     │  │ Service     │  │ Service     │  │ Service │ │
│  │             │  │             │  │             │  │         │ │
│  │ • Orchestr  │  │ • Extract   │  │ • Load Model│  │ • API   │ │
│  │ • Validate  │  │ • Convert   │  │ • Transcribe│  │ • Chunk │ │
│  │ • Route     │  │ • Metadata  │  │ • Split WAV │  │ • Cost  │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────┘ │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │ 📁 File     │  │ 📝 Output   │  │ ⚡ Background│              │
│  │ Service     │  │ Service     │  │ Tasks       │              │
│  │             │  │             │  │             │              │
│  │ • Storage   │  │ • Markdown  │  │ • Async     │              │
│  │ • Cleanup   │  │ • Format    │  │ • Queue     │              │
│  │ • Security  │  │ • Save      │  │ • Status    │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘
                                   │
                           🔌 Interfaces & Adapters
                                   │
┌─────────────────────────────────────────────────────────────────┐
│                 🏗️ INFRASTRUCTURE LAYER                        │
│                     (External Systems)                         │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────┐ │
│  │ 💾 Storage  │  │ 🔧 FFmpeg   │  │ 🤖 OpenAI   │  │ 📝 Vosk │ │
│  │ System      │  │ Converter   │  │ API         │  │ Model   │ │
│  │             │  │             │  │             │  │         │ │
│  │ • Temp      │  │ • MP4→WAV   │  │ • Whisper   │  │ • Local │ │
│  │ • Upload    │  │ • Normalize │  │ • Tokens    │  │ • Offline│ │
│  │ • Output    │  │ • Metadata  │  │ • Billing   │  │ • Free  │ │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

🔄 FLUXO DE DADOS PRINCIPAL

```text
📱 CLIENT REQUEST (with JWT)
     │
     ▼
� JWT VALIDATION 
     │ • Verify token signature
     │ • Check permissions
     │ • Validate rate limits
     ▼
�🛣️ ROUTER (Validation & Auth)
     │
     ▼
🚦 QUEUE MANAGER
     │ • Check concurrent limits
     │ • Check daily limits  
     │ • Add to priority queue
     ▼
🎯 TRANSCRIPTION MANAGER
     │ • Wait for processing slot
     │ • Track active jobs
     ├─────────────────────────────┐
     ▼                             ▼
🎵 AUDIO SERVICE              📁 FILE SERVICE
│   • Upload MP4               │   • Temp storage
│   • Extract audio            │   • Security check
│   • 🗑️ Remove MP4            │   • Track files
     │                             │
     ▼                             ▼
🔧 FFMPEG PROCESSING          💾 STORAGE SYSTEM
     │                             │
     ▼                             │
🔀 METHOD SELECTION               │
     │                             │
     ├─────────────┬───────────────┼─────────────┐
     ▼             ▼               ▼             ▼
🗣️ VOSK        🤖 OPENAI      ⚡ BACKGROUND  📊 STATUS
SERVICE        SERVICE        TASKS         TRACKING
│              │              │             │
│ • Offline    │ • Online     │ • Async     │ • Progress
│ • FREE       │ • PREMIUM    │ • Queue     │ • Position
│ • Queue      │ • Rate limit │ • Monitor   │ • ETA
     │             │              │             │
     └─────────────┼──────────────┼─────────────┘
                   ▼              ▼
             🧹 CLEANUP SERVICE    📡 RESPONSE
             │   • 🗑️ Remove WAV   │   • Text in body
             │   • 🗑️ Remove chunks│   • Queue info
             │   • 🗑️ Remove temp  │   • Usage stats
                   │                
                   ▼                
             ✨ ZERO PERSISTENCE   
```

## 🏛️ Arquitetura por Responsabilidade

### 🎯 Core Components

```text
┌─────────────────────────────────────────────────────────────┐
│                   TRANSCRIPTION MANAGER                    │
│                      (Orchestrator)                        │
│                                                             │
│  📋 Responsibilities:                                       │
│  ├─ Route requests to appropriate service                  │
│  ├─ Manage workflow state                                  │
│  ├─ Handle cross-service communication                     │
│  ├─ Error handling and recovery                            │
│  └─ Resource management                                     │
│                                                             │
│  🔌 Interfaces:                                             │
│  ├─ TranscriptionServiceInterface                          │
│  ├─ AudioServiceInterface                                  │
│  ├─ FileServiceInterface                                   │
│  └─ OutputServiceInterface                                 │
└─────────────────────────────────────────────────────────────┘
```

### 🎵 Audio Processing Pipeline

```text
INPUT: MP4 File
     │
     ▼
┌─────────────────┐
│   VALIDATION    │ ◄─── • File type check
│                 │      • Size limits
│                 │      • Security scan
└─────────────────┘
     │
     ▼
┌─────────────────┐
│   EXTRACTION    │ ◄─── • FFmpeg conversion
│                 │      • Format: WAV 16kHz mono
│                 │      • Metadata extraction
│                 │      • 🗑️ REMOVE MP4 immediately
└─────────────────┘
     │
     ▼
┌─────────────────┐
│   ANALYSIS      │ ◄─── • Duration calculation
│                 │      • Quality assessment
│                 │      • Chunking strategy
└─────────────────┘
     │
     ▼
┌─────────────────┐
│   TRANSCRIPTION │ ◄─── • Process audio
│                 │      • Generate text
│                 │      • 🗑️ REMOVE WAV & chunks
└─────────────────┘
     │
     ▼
┌─────────────────┐
│   RESPONSE      │ ◄─── • Return text in body
│                 │      • Optional markdown link
│                 │      • 🗑️ CLEANUP all temp files
└─────────────────┘
     │
     ▼
OUTPUT: ✨ Zero Persistence ✨
```

### 🗣️ Transcription Services

```text
              TRANSCRIPTION REQUEST
                       │
                       ▼
              ┌─────────────────┐
              │ METHOD SELECTOR │
              └─────────────────┘
                       │
            ┌──────────┴──────────┐
            ▼                     ▼
   ┌─────────────────┐   ┌─────────────────┐
   │  VOSK SERVICE   │   │ OPENAI SERVICE  │
   │                 │   │                 │
   │ 🗣️ Features:    │   │ 🤖 Features:    │
   │ • Offline       │   │ • Online        │
   │ • Free          │   │ • Paid          │
   │ • Portuguese    │   │ • Multi-lang    │
   │ • Local model   │   │ • Cloud API     │
   │ • No limits     │   │ • Rate limits   │
   │ • Private       │   │ • High accuracy │
   │                 │   │                 │
   │ 📊 Process:     │   │ 📊 Process:     │
   │ 1. Load model   │   │ 1. Chunk audio  │
   │ 2. Stream audio │   │ 2. API calls    │
   │ 3. Real-time    │   │ 3. Merge results│
   │ 4. Local result │   │ 4. Cost tracking│
   └─────────────────┘   └─────────────────┘
            │                     │
            └──────────┬──────────┘
                       ▼
              ┌─────────────────┐
              │ RESULT MERGER   │ ◄─── • Combine chunks
              │                 │      • Remove overlaps
              │                 │      • Quality check
              └─────────────────┘
                       │
                       ▼
              FINAL TRANSCRIPTION
```

## 🔐 Security & Validation Flow

```text
📤 FILE UPLOAD
     │
     ▼
┌─────────────────┐
│ SECURITY GATES  │
│                 │
│ 🔍 Checks:      │
│ ├─ File type    │
│ ├─ File size    │
│ ├─ Virus scan   │
│ ├─ Content type │
│ └─ Rate limits  │
└─────────────────┘
     │
     ▼ ✅ PASS
┌─────────────────┐
│ SANITIZATION    │
│                 │
│ 🧹 Actions:     │
│ ├─ Name cleanup │
│ ├─ Path safe    │
│ ├─ Metadata     │
│ └─ Temp storage │
└─────────────────┘
     │
     ▼ ✅ CLEAN
┌─────────────────┐
│ VALIDATION      │
│                 │
│ ✅ Validates:   │
│ ├─ Audio format │
│ ├─ Duration     │
│ ├─ Quality      │
│ └─ Integrity    │
└─────────────────┘
     │
     ▼ ✅ VALID
🎵 PROCESSING PIPELINE
```

## 🚦 Sistema de Filas e Controle de Concorrência

### **Arquitetura de Filas Multi-Prioridade**

```text
📱 USER REQUESTS (with JWT tokens)
     │
     ▼
🔐 JWT VALIDATION & RATE LIMITING
     │ • Validate token
     │ • Check user type (free/premium/admin)
     │ • Verify daily/concurrent limits
     ▼
🚦 QUEUE MANAGER
     │
     ┌─────────┬─────────┬─────────┐
     ▼         ▼         ▼         ▼
┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐
│ ADMIN   │ │PREMIUM  │ │  FREE   │ │   ACTIVE    │
│ QUEUE   │ │ QUEUE   │ │ QUEUE   │ │    JOBS     │
│ (P1)    │ │ (P2)    │ │ (P3)    │ │             │
│         │ │         │ │         │ │ user1: [j1] │
│ • High  │ │ • Medium│ │ • Low   │ │ user2: [j2] │
│   prio  │ │   prio  │ │   prio  │ │ user3: [j3] │
│ • No    │ │ • 100MB │ │ • 100MB │ │             │
│   limits│ │   limit │ │   limit │ │ Max: 3 jobs │
│ • 10    │ │ • 3     │ │ • 1     │ │ concurrent  │
│   simul │ │   simul │ │   simul │ │             │
└─────────┘ └─────────┘ └─────────┘ └─────────────┘
     │         │         │               │
     └─────────┼─────────┼───────────────┘
               ▼         ▼
         🔄 QUEUE PROCESSOR
         │ 1. Check available slots (max 3)
         │ 2. Process P1 first, then P2, then P3
         │ 3. Respect user concurrent limits
         │ 4. Update active jobs tracking
         ▼
    🗣️ VOSK PROCESSING SLOTS
    ┌─────────┬─────────┬─────────┐
    │ SLOT 1  │ SLOT 2  │ SLOT 3  │
    │ Active  │ Active  │ Free    │
    │ Admin   │ Premium │ ---     │
    │ Job A   │ Job B   │         │
    └─────────┴─────────┴─────────┘
```

### **Fluxo de Decisão de Fila**

```text
NEW TRANSCRIPTION REQUEST
     │
     ▼
🔍 USER TYPE CHECK
     │
     ├─ ADMIN ──────────► 🏆 HIGH PRIORITY QUEUE (P1)
     │                     │ • No limits
     │                     │ • Process immediately
     │                     │ • Max 10 concurrent
     │
     ├─ PREMIUM ────────► 🥈 MEDIUM PRIORITY QUEUE (P2)  
     │                     │ • 50/day, 1000/month
     │                     │ • Max 3 concurrent
     │                     │ • Process after admin
     │
     └─ FREE ───────────► � LOW PRIORITY QUEUE (P3)
                           │ • 10/day, 100/month
                           │ • Max 1 concurrent  
                           │ • Process after premium
                           │
     ▼ ALL QUEUES
🎯 SLOT ALLOCATION
     │ Check: Current active jobs < 3 total slots?
     │ Check: User within concurrent limit?
     │ Check: User within daily limit?
     │
     ├─ YES ────────────► ⚡ START PROCESSING
     │                     │ • Assign to available slot
     │                     │ • Add to active jobs
     │                     │ • Send "processing" status
     │
     └─ NO ─────────────► ⏳ QUEUE POSITION
                           │ • Calculate wait time
                           │ • Return queue position
                           │ • Send "queued" status
```

### **Estados do Job de Transcrição**

```text
📤 SUBMITTED
│ • File uploaded
│ • Initial validation
│ • JWT verified
▼
🔍 VALIDATED  
│ • File size OK
│ • Duration OK
│ • User limits OK
▼
⏳ QUEUED
│ • Added to priority queue
│ • Position: #N
│ • ETA: X minutes
▼
⚡ PROCESSING
│ • Slot assigned
│ • Audio extraction
│ • Vosk transcription
│ • Progress: X%
▼
�🧹 CLEANUP
│ • Remove temp files
│ • Free processing slot
│ • Update usage counters
▼
✅ COMPLETED
│ • Result in response
│ • Usage updated
│ • Slot available
```

### **Controle de Rate Limiting**

```text
📊 RATE LIMIT CHECKS (Redis-based)

Daily Limits:
┌────────────────────────────────────┐
│ Key: rate_limit:daily:vosk:user123:2025-08-02
│ Value: 7                          │ 
│ TTL: 86400s (expires at midnight) │
│ Limit: 10 (for free users)        │
│ Status: 7/10 ✅ (OK)              │
└────────────────────────────────────┘

Concurrent Limits:
┌────────────────────────────────────┐
│ Active Jobs: {                     │
│   "user123": ["job1"],            │
│   "user456": ["job2", "job3"]     │
│ }                                  │
│ User123 concurrent: 1/1 ✅ (OK)   │  
│ User456 concurrent: 2/3 ✅ (OK)   │
└────────────────────────────────────┘

Queue Positions:
┌────────────────────────────────────┐
│ High Priority Queue: []            │
│ Medium Priority Queue: [job4]      │
│ Low Priority Queue: [job5, job6]   │
│                                    │
│ job5 position: 2                   │
│ job6 position: 3                   │
│ Estimated wait: 8 minutes          │
└────────────────────────────────────┘
```

### **Algoritmo de Fair Usage**

```text
🎯 FAIR USAGE ALGORITHM

For each new request:

1️⃣ CHECK USER TYPE
   ├─ Free: Apply strict limits
   ├─ Premium: Apply medium limits  
   └─ Admin: Apply minimal limits

2️⃣ CHECK RECENT USAGE
   ├─ High recent usage? → Add delay
   ├─ Consistent max usage? → Flag suspicious
   └─ Normal usage? → Proceed

3️⃣ CHECK FILE CHARACTERISTICS
   ├─ Large file + Free user? → Lower priority
   ├─ Peak hours + Free user? → Add to queue
   └─ Normal conditions? → Process normally

4️⃣ DYNAMIC ADJUSTMENTS
   ├─ System under load? → Reduce slots
   ├─ Low usage period? → Increase slots
   └─ Abuse detected? → Throttle user

5️⃣ PRIORITY CALCULATION
   Final Priority = Base Priority + Usage Factor + Time Factor
   
   Where:
   • Base Priority: 1(admin), 2(premium), 3(free)
   • Usage Factor: +1 if heavy usage, +0 if normal
   • Time Factor: +1 if peak hours, +0 if off-peak
```

### **Fluxo de Limpeza Obrigatória**

```text
📤 UPLOAD MP4 (temp1.mp4)
     │ ⏰ Tracked by CleanupService
     ▼
🎵 EXTRACT AUDIO (temp1.wav)
     │ 🗑️ REMOVE temp1.mp4 ← IMMEDIATE
     ▼
🔀 CHUNK AUDIO (temp1_part1.wav, temp1_part2.wav...)
     │ 🗑️ REMOVE temp1.wav ← IMMEDIATE  
     ▼
🗣️ TRANSCRIBE CHUNKS (processing...)
     │ 🗑️ REMOVE temp1_partN.wav ← AFTER EACH CHUNK
     ▼
📝 MERGE RESULTS (final_transcript.txt)
     │ 🗑️ REMOVE all remaining temp files ← IMMEDIATE
     ▼
📡 RETURN RESPONSE
     │ • Text in JSON body
     │ • Optional markdown link (expires 5min)
     ▼
✨ ZERO PERSISTENCE ACHIEVED ✨
```

### **Garantias de Limpeza**

```text
┌─────────────────────────────────────────────────────────────┐
│                  CLEANUP SAFETY NET                        │
│                                                             │
│  🔄 LEVEL 1: Context Managers                              │
│  ├─ try/finally blocks guarantee cleanup                   │
│  └─ Even on exceptions, files are removed                  │
│                                                             │
│  ⏰ LEVEL 2: Scheduled Jobs                                │
│  ├─ Hourly orphan file cleanup                             │
│  └─ Daily emergency full cleanup                           │
│                                                             │
│  � LEVEL 3: Disk Monitoring                               │
│  ├─ Alert if temp folder > 1GB                             │
│  └─ Emergency cleanup if disk > 90%                        │
│                                                             │
│  📋 LEVEL 4: Audit Logs                                    │
│  ├─ Log every file creation/deletion                       │
│  └─ Daily report of cleanup operations                     │
└─────────────────────────────────────────────────────────────┘
```

### **Timeline de Limpeza**

```text
T+0s    : MP4 uploaded to /temp/session_id/
T+5s    : WAV extracted, MP4 deleted
T+10s   : WAV chunked, original WAV deleted
T+30s   : Chunk 1 transcribed, chunk1.wav deleted
T+45s   : Chunk 2 transcribed, chunk2.wav deleted
T+60s   : Final transcript ready, all remaining files deleted
T+300s  : Optional markdown link expires and file deleted
T+3600s : Hourly orphan cleanup (safety net)
T+86400s: Daily emergency cleanup (safety net)
```

```text
┌─────────────────┐    1:N    ┌─────────────────┐
│   AudioFile     │ ────────► │ TranscriptionJob│
│                 │           │                 │
│ • id            │           │ • id            │
│ • filename      │           │ • audio_id (FK) │
│ • duration      │           │ • method        │
│ • file_path     │           │ • status        │
│ • metadata      │           │ • progress      │
│ • created_at    │           │ • result        │
└─────────────────┘           │ • created_at    │
                              │ • completed_at  │
                              └─────────────────┘
         │                             │
         │                             │
         ▼                             ▼
┌─────────────────┐           ┌─────────────────┐
│   AudioChunk    │           │ TranscriptOutput│
│                 │           │                 │
│ • audio_id (FK) │           │ • job_id (FK)   │
│ • chunk_index   │           │ • output_path   │
│ • start_time    │           │ • format        │
│ • end_time      │           │ • client_name   │
│ • file_path     │           │ • created_at    │
└─────────────────┘           └─────────────────┘
```

## ⚡ Performance & Scaling Strategy

```text
🚀 SCALING LAYERS

┌─────────────────────────────────────────────────────────────┐
│                    LOAD BALANCER                           │
│                   (nginx/traefik)                          │
└─────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            ▼                 ▼                 ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   API INSTANCE  │ │   API INSTANCE  │ │   API INSTANCE  │
│        #1       │ │        #2       │ │        #3       │
└─────────────────┘ └─────────────────┘ └─────────────────┘
            │                 │                 │
            └─────────────────┼─────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SHARED RESOURCES                        │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │    REDIS    │  │   MESSAGE   │  │   SHARED    │        │
│  │   CACHE     │  │   QUEUE     │  │  STORAGE    │        │
│  │             │  │  (Celery)   │  │   (S3/NFS)  │        │
│  │ • Sessions  │  │ • BG Tasks  │  │ • Files     │        │
│  │ • Status    │  │ • Progress  │  │ • Models    │        │
│  │ • Cache     │  │ • Results   │  │ • Outputs   │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 State Management

```text
REQUEST LIFECYCLE STATES

📤 UPLOAD
│ State: UPLOADING
│ Progress: 0-10%
▼
🔍 VALIDATION  
│ State: VALIDATING
│ Progress: 10-15%
▼
🎵 EXTRACTION
│ State: EXTRACTING
│ Progress: 15-30%
▼
🔀 QUEUED
│ State: QUEUED
│ Progress: 30%
▼
🗣️ TRANSCRIBING
│ State: PROCESSING
│ Progress: 30-90%
│ ├─ Chunk 1/N: 30-40%
│ ├─ Chunk 2/N: 40-50%
│ └─ Chunk N/N: 80-90%
▼
📝 FORMATTING
│ State: FORMATTING
│ Progress: 90-95%
▼
💾 SAVING
│ State: SAVING
│ Progress: 95-100%
▼
✅ COMPLETED
│ State: COMPLETED
│ Progress: 100%
```

---

*Este diagrama visual complementa o documento de arquitetura principal e serve como referência rápida para entender os fluxos e relacionamentos do sistema.*

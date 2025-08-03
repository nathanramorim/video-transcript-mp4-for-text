# 📺 Video Transcript API

## 🚀 Como executar a API


### 1. Pré-requisitos

- **Python 3.11 instalado**
    - No macOS, instale com:
      ```bash
      brew install python@3.11
      ```
- **pip instalado** (vem junto com Python)
- (Opcional) Docker e Docker Compose

---

### 2. Preparação do ambiente Python

**Crie e ative o ambiente virtual:**

```bash
# Crie o ambiente virtual (apenas uma vez)
python3.11 -m venv app/venv

# Ative o ambiente virtual (sempre antes de rodar ou instalar pacotes)
source app/venv/bin/activate
```

**Dica:** Após ativar, o comando `pip` deve funcionar normalmente. Se não funcionar, use:
```bash
python3.11 -m pip install -r requirements_api.txt
```

**Alias para facilitar:**
Se quiser digitar só `pip` sempre, adicione ao final do seu `~/.zshrc`:
```bash
alias pip="python3.11 -m pip"
```
Depois rode:
```bash
source ~/.zshrc
```

---

### 3. Instalação das dependências

```bash
pip install -r requirements_api.txt
```

---

### 4. Configuração do ambiente

- Edite o arquivo `.env` conforme necessário (baseado em `.env.example`).

---

### 5. Executando a API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Acesse a documentação interativa: [http://localhost:8000/docs](http://localhost:8000/docs)
- Endpoint raiz: [http://localhost:8000/](http://localhost:8000/)

---

### 6. Endpoint de transcrição Vosk

**POST /api/v1/vosk/transcribe**

Envia um vídeo (mp4 ou mov) e retorna a transcrição do áudio.

**Resposta:**
```json
{
  "job_id": "...",
  "status": "completed",
  "result": "texto transcrito...",
  "exec_time_seconds": 12.34
}
```
O campo `exec_time_seconds` mostra o tempo total de processamento da transcrição.

---

### 7. Usando Docker (opcional)

```bash
sudo docker-compose up --build -d
sudo docker-compose logs -f api
```

---

### 8. Estrutura de diretórios

...existing code...

### 2. Preparação do ambiente

```bash
# Crie o ambiente virtual (se ainda não existir)
python3.11 -m venv app/venv

# Ative o ambiente virtual
source app/venv/bin/activate

# Instale as dependências
pip install -r requirements_api.txt
```

### 3. Configuração do ambiente

- Edite o arquivo `.env` conforme necessário (baseado em `.env.example`).

### 4. Executando a API

```bash
# Na raiz do projeto
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Acesse a documentação interativa: [http://localhost:8000/docs](http://localhost:8000/docs)
- Endpoint raiz: [http://localhost:8000/](http://localhost:8000/)

### 5. Usando Docker (opcional)

```bash
# Build e start
sudo docker-compose up --build -d

# Logs
sudo docker-compose logs -f api
```

### 6. Estrutura de diretórios

```
transcript-video/
├── app/
│   ├── main.py
│   ├── ...
├── requirements_api.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── README_API.md
```

### 7. Principais comandos

- Ativar ambiente virtual:
  ```bash
  source app/venv/bin/activate
  ```
- Instalar dependências:
  ```bash
  pip install -r requirements_api.txt
  ```
- Rodar API:
  ```bash
  uvicorn app.main:app --reload
  ```

---

## 📢 Observações
- O projeto original CLI está preservado em `legacy-transcription/`.
- Este README é exclusivo para a API.
- Para dúvidas ou problemas, consulte a documentação na pasta `feature-instructions/`.

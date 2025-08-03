# 📺 Video Transcript API

## 🚀 Como executar a API

### 1. Pré-requisitos
- Python 3.11 instalado
- pip instalado
- (Opcional) Docker e Docker Compose

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

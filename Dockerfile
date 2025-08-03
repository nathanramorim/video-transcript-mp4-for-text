FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    redis-server \
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

#!/bin/bash

# Script para corrigir e preparar o ambiente legacy para funcionar após reorganização

echo "🔧 Corrigindo ambiente legacy após reorganização..."

cd "$(dirname "$0")"
LEGACY_DIR="$(pwd)"
ROOT_DIR="$(dirname "$LEGACY_DIR")"

echo "📁 Diretórios detectados:"
echo "   Legacy: $LEGACY_DIR"
echo "   Root: $ROOT_DIR"

# 1. Criar link simbólico para o modelo (evita duplicar arquivos grandes)
echo ""
echo "🤖 Configurando acesso ao modelo Vosk..."
if [ -d "$ROOT_DIR/model" ]; then
    if [ ! -L "$LEGACY_DIR/model" ]; then
        ln -s "$ROOT_DIR/model" "$LEGACY_DIR/model"
        echo "   ✅ Link simbólico criado: legacy-transcription/model -> ../model"
    else
        echo "   ✅ Link simbólico já existe"
    fi
else
    echo "   ❌ Modelo não encontrado em $ROOT_DIR/model"
    echo "   💡 Baixe o modelo português em: https://alphacephei.com/vosk/models"
fi

# 2. Criar link simbólico para .env (para manter configurações centralizadas)
echo ""
echo "⚙️ Configurando acesso às variáveis de ambiente..."
if [ -f "$ROOT_DIR/.env" ]; then
    if [ ! -L "$LEGACY_DIR/.env" ]; then
        ln -s "$ROOT_DIR/.env" "$LEGACY_DIR/.env"
        echo "   ✅ Link simbólico criado: legacy-transcription/.env -> ../.env"
    else
        echo "   ✅ Link simbólico já existe"
    fi
else
    echo "   ⚠️ Arquivo .env não encontrado no diretório raiz"
    echo "   💡 Crie um .env no diretório raiz ou use apenas Vosk (offline)"
fi

# 3. Verificar se venv existe e está ativo
echo ""
echo "🐍 Verificando ambiente Python..."
if [ -d "$ROOT_DIR/venv" ]; then
    echo "   ✅ Virtual environment encontrado em $ROOT_DIR/venv"
    if [[ "$VIRTUAL_ENV" == *"transcript-video"* ]]; then
        echo "   ✅ Virtual environment ativo"
    else
        echo "   ⚠️ Virtual environment não está ativo"
        echo "   💡 Execute: source $ROOT_DIR/venv/bin/activate"
    fi
else
    echo "   ❌ Virtual environment não encontrado"
    echo "   💡 Crie um venv: python3 -m venv $ROOT_DIR/venv"
fi

# 4. Verificar dependências
echo ""
echo "📦 Verificando dependências..."
if python3 -c "import vosk, openai, moviepy" 2>/dev/null; then
    echo "   ✅ Todas as dependências estão instaladas"
else
    echo "   ❌ Algumas dependências estão faltando"
    echo "   💡 Instale com: pip install -r requirements.txt"
fi

# 5. Teste rápido
echo ""
echo "🧪 Teste rápido do script..."
if python3 -c "
import sys
sys.path.insert(0, '.')
try:
    from pathlib import Path
    BASE_DIR = Path('$LEGACY_DIR')
    INPUT_DIR = BASE_DIR / 'input'
    OUTPUT_DIR = BASE_DIR / 'output' 
    MODEL_DIR = BASE_DIR / 'model'
    print(f'   📂 Input: {INPUT_DIR.exists()} - {INPUT_DIR}')
    print(f'   📂 Output: {OUTPUT_DIR.exists()} - {OUTPUT_DIR}')
    print(f'   📂 Model: {MODEL_DIR.exists()} - {MODEL_DIR}')
    if MODEL_DIR.exists():
        print(f'   🤖 Modelo: {len(list(MODEL_DIR.glob(\"*\")))} arquivos')
except Exception as e:
    print(f'   ❌ Erro: {e}')
"; then
    echo "   ✅ Estrutura de diretórios OK"
else
    echo "   ❌ Problemas na estrutura"
fi

echo ""
echo "🎯 Resumo do Status:"
echo "   📁 Diretórios: $([ -d input ] && echo "✅" || echo "❌") input  $([ -d output ] && echo "✅" || echo "❌") output  $([ -L model ] && echo "✅" || echo "❌") model"
echo "   ⚙️ Configuração: $([ -L .env ] && echo "✅" || echo "❌") .env"
echo "   🐍 Python: $(python3 --version 2>/dev/null | cut -d' ' -f2 || echo "❌ não encontrado")"
echo "   📦 Dependências: $(python3 -c "import vosk,openai,moviepy" 2>/dev/null && echo "✅" || echo "❌")"

echo ""
if [ -L model ] && [ -d input ] && [ -d output ]; then
    echo "🚀 Pronto! Agora você pode executar:"
    echo "   cd $LEGACY_DIR"
    echo "   source $ROOT_DIR/venv/bin/activate  # se necessário"
    echo "   python3 main.py"
else
    echo "❌ Ainda há problemas que precisam ser resolvidos."
    echo "   Siga as instruções acima marcadas com 💡"
fi

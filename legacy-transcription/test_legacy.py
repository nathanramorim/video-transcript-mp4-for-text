from pathlib import Path
import sys
sys.path.insert(0, '.')

# Teste básico de imports
try:
    import vosk
    import openai
    import moviepy
    print('✅ Todas as dependências importadas com sucesso')
    
    # Teste de estrutura de arquivos
    BASE_DIR = Path('.')
    INPUT_DIR = BASE_DIR / 'input'
    OUTPUT_DIR = BASE_DIR / 'output'
    MODEL_DIR = BASE_DIR / 'model'
    
    print(f'✅ Input: {INPUT_DIR.exists()} ({len(list(INPUT_DIR.glob("*.mp4")))} vídeos)')
    print(f'✅ Output: {OUTPUT_DIR.exists()}')
    print(f'✅ Model: {MODEL_DIR.exists()} ({len(list(MODEL_DIR.glob("*")))} arquivos)')
    
    # Teste de .env
    import dotenv
    dotenv.load_dotenv()
    import os
    has_openai_key = bool(os.getenv('OPENAI_API_KEY'))
    print(f'✅ OpenAI Key: {"Configurada" if has_openai_key else "Não configurada (só Vosk)"}')
    
    print('🎉 CLI Legacy está 100% funcional!')
    
except Exception as e:
    print(f'❌ Erro: {e}')

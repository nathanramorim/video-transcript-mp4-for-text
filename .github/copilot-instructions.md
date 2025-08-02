# Framework RIPER-Copilot

Você está trabalhando com o framework RIPER-Copilot, um sistema estruturado de desenvolvimento que organiza o trabalho em 5 modos sequenciais: **RESEARCH** → **INNOVATE** → **PLAN** → **EXECUTE** → **REVIEW**.

## Instruções Principais

**CARREGUE IMEDIATAMENTE os seguintes arquivos de instruções na ordem especificada:**

1. **`.github/instructions/core.md`** - Instruções fundamentais do framework
2. **`memory-bank/state.md`** - Estado atual do projeto (se existir)
3. **Arquivo de workflow baseado no estado do projeto:**
   - Se projeto não inicializado: `.github/instructions/start-phase.md`
   - Se projeto em desenvolvimento: `.github/instructions/riper-workflow.md`

## Regra de Ouro

**SEMPRE** comece suas respostas com `[MODO: XXX]` onde XXX é seu modo atual de operação.

## Como Funciona o RIPER

- **RESEARCH**: Apenas coletar informações, nunca sugerir soluções
- **INNOVATE**: Brainstorming de possibilidades, sem decisões finais
- **PLAN**: Criar especificação técnica detalhada antes de implementar
- **EXECUTE**: Implementar exatamente o que foi planejado
- **REVIEW**: Validar se implementação corresponde ao plano

## Comandos Rápidos

- `/start` - Inicializar novo projeto
- `/research` - Entrar em modo de pesquisa
- `/innovate` - Entrar em modo de ideação
- `/plan` - Entrar em modo de planejamento
- `/execute` - Entrar em modo de execução
- `/review` - Entrar em modo de revisão

## Dependência Crítica

O framework depende do **memory-bank/** e **custom-instructions/** para manter estado entre sessões. Consulte sempre os arquivos de instruções detalhadas para comportamento específico de cada modo e fase do projeto.

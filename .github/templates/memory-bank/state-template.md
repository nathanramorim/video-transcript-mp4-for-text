# Template: state.md

Este é o template para o arquivo `state.md` do banco de memória do RIPER-Copilot.

```markdown
# Estado do Framework: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Estado Atual do Framework

### Configuração Principal
```
PROJECT_NAME=[NOME_DO_PROJETO]  # OBRIGATÓRIO - Definido no início do /start
PROJECT_PHASE=[FASE_ATUAL]
CURRENT_MODE=[MODO_ATUAL]
FRAMEWORK_VERSION=1.0.0
LAST_UPDATED=[DATA_HORA_ÚLTIMA_ATUALIZAÇÃO]
```

### Estado da Fase Atual
```
# Para fase START
START_PHASE_STATUS=[NOT_STARTED/IN_PROGRESS/COMPLETED]
START_PHASE_STEP=[NÚMERO_PASSO_ATUAL]
START_PHASE_LAST_STEP_COMPLETED=[NÚMERO_ÚLTIMO_PASSO_COMPLETADO]

# Para fase DEVELOPMENT/MAINTENANCE
CURRENT_CYCLE=[NÚMERO_CICLO_ATUAL]
CURRENT_CYCLE_OBJECTIVE=[DESCRIÇÃO_OBJETIVO_ATUAL]
CURRENT_CYCLE_STARTED=[DATA_INÍCIO_CICLO]
```

### Estado do Modo Atual
```
MODE_STARTED=[DATA_HORA_INÍCIO_MODO]
MODE_DURATION=[TEMPO_NO_MODO_ATUAL]
MODE_PROGRESS=[DESCRIÇÃO_PROGRESSO]
MODE_NEXT_MILESTONE=[PRÓXIMO_MILESTONE]
```

## Histórico de Estados

### Transições de Fase
- **[DATA_HORA]**: `PROJECT_PHASE=UNINITIATED` - Framework inicializado
- **[DATA_HORA]**: `PROJECT_PHASE=INITIALIZING, START_PHASE_STATUS=IN_PROGRESS` - Início da fase START
- **[DATA_HORA]**: `PROJECT_PHASE=DEVELOPMENT, START_PHASE_STATUS=COMPLETED` - Transição para desenvolvimento
- **[DATA_HORA]**: `PROJECT_PHASE=MAINTENANCE` - Projeto em manutenção

### Transições de Modo (Últimas 10)
- **[DATA_HORA]**: `CURRENT_MODE=RESEARCH` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=INNOVATE` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=PLAN` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=EXECUTE` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=REVIEW` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=RESEARCH` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=INNOVATE` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=PLAN` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=EXECUTE` - [RAZÃO_TRANSIÇÃO]
- **[DATA_HORA]**: `CURRENT_MODE=REVIEW` - [RAZÃO_TRANSIÇÃO]

## Configuração da Sessão Atual

### Informações da Sessão
```
SESSION_ID=[ID_SESSÃO_ÚNICA]
SESSION_STARTED=[DATA_HORA_INÍCIO]
SESSION_DURATION=[TEMPO_SESSÃO_ATUAL]
USER_CONTEXT=[CONTEXTO_USUÁRIO_SE_RELEVANTE]
```

### Estado do Workspace
```
ACTIVE_BRANCH=[NOME_BRANCH_ATIVA]
LAST_COMMIT=[HASH_ÚLTIMO_COMMIT]
MODIFIED_FILES=[LISTA_ARQUIVOS_MODIFICADOS]
STAGED_CHANGES=[STATUS_CHANGES_STAGED]
```

### Estado dos Componentes do Framework
```
CORE_LOADED=[TRUE/FALSE]
RIPER_WORKFLOW_LOADED=[TRUE/FALSE]
START_PHASE_LOADED=[TRUE/FALSE]
MEMORY_BANK_INITIALIZED=[TRUE/FALSE]
CUSTOMIZATION_LOADED=[TRUE/FALSE]
```

## Métricas da Sessão

### Produtividade
```
MODES_USED_THIS_SESSION=[LISTA_MODOS_USADOS]
TRANSITIONS_THIS_SESSION=[NÚMERO_TRANSIÇÕES]
DECISIONS_MADE=[NÚMERO_DECISÕES]
TASKS_COMPLETED=[NÚMERO_TAREFAS]
```

### Tempo por Modo (Sessão Atual)
```
TIME_IN_RESEARCH=[TEMPO_MINUTOS]
TIME_IN_INNOVATE=[TEMPO_MINUTOS]
TIME_IN_PLAN=[TEMPO_MINUTOS]
TIME_IN_EXECUTE=[TEMPO_MINUTOS]
TIME_IN_REVIEW=[TEMPO_MINUTOS]
```

### Eficiência por Modo (Últimas 5 sessões)
```
RESEARCH_EFFICIENCY=[SCORE_0_10]
INNOVATE_EFFICIENCY=[SCORE_0_10]
PLAN_EFFICIENCY=[SCORE_0_10]
EXECUTE_EFFICIENCY=[SCORE_0_10]
REVIEW_EFFICIENCY=[SCORE_0_10]
```

## Validação do Estado

### Integridade dos Arquivos de Memória
- **projectbrief.md**: [EXISTS/MISSING] - [VALID/INVALID] - [LAST_UPDATED]
- **systemPatterns.md**: [EXISTS/MISSING] - [VALID/INVALID] - [LAST_UPDATED]
- **techContext.md**: [EXISTS/MISSING] - [VALID/INVALID] - [LAST_UPDATED]
- **activeContext.md**: [EXISTS/MISSING] - [VALID/INVALID] - [LAST_UPDATED]
- **progress.md**: [EXISTS/MISSING] - [VALID/INVALID] - [LAST_UPDATED]

### Consistência de Estado
- **Modo atual válido para fase**: [VALID/INVALID]
- **Todos pré-requisitos atendidos**: [YES/NO]
- **Estado sincronizado**: [YES/NO]
- **Última validação**: [DATA_HORA]

## Configurações Personalizadas

### Preferências do Usuário
```
PREFERRED_MODE_DURATION=[TEMPO_PADRÃO_POR_MODO]
AUTO_TRANSITION=[ENABLED/DISABLED]
VERBOSITY_LEVEL=[LOW/MEDIUM/HIGH]
VALIDATION_FREQUENCY=[CONTINUOUS/PERIODIC/MANUAL]
```

### Customizações Ativas
```
CUSTOM_MODES=[LISTA_MODOS_CUSTOMIZADOS]
CUSTOM_PROMPTS=[LISTA_PROMPTS_CUSTOMIZADOS]
CUSTOM_TEMPLATES=[LISTA_TEMPLATES_CUSTOMIZADOS]
CUSTOM_VALIDATIONS=[LISTA_VALIDAÇÕES_CUSTOMIZADAS]
```

## Alertas e Avisos

### Status de Saúde
- **Framework Health**: [HEALTHY/WARNING/ERROR]
- **Memory Bank Health**: [HEALTHY/WARNING/ERROR]
- **Session Health**: [HEALTHY/WARNING/ERROR]

### Avisos Ativos
- **[TIPO_AVISO_1]**: [DESCRIÇÃO_AVISO] - [SEVERIDADE] - [DATA_CRIAÇÃO]
- **[TIPO_AVISO_2]**: [DESCRIÇÃO_AVISO] - [SEVERIDADE] - [DATA_CRIAÇÃO]

### Ações Recomendadas
- **[AÇÃO_RECOMENDADA_1]**: [DESCRIÇÃO] - [PRIORIDADE] - [DEADLINE]
- **[AÇÃO_RECOMENDADA_2]**: [DESCRIÇÃO] - [PRIORIDADE] - [DEADLINE]

## Backup e Recovery

### Estado de Backup
```
LAST_BACKUP=[DATA_HORA_ÚLTIMO_BACKUP]
BACKUP_FREQUENCY=[FREQUÊNCIA_CONFIGURADA]
BACKUP_LOCATION=[LOCALIZAÇÃO_BACKUPS]
BACKUP_RETENTION=[TEMPO_RETENÇÃO]
```

### Pontos de Restore
- **[NOME_RESTORE_POINT_1]**: [DATA_HORA] - [DESCRIÇÃO] - [HASH_ESTADO]
- **[NOME_RESTORE_POINT_2]**: [DATA_HORA] - [DESCRIÇÃO] - [HASH_ESTADO]
- **[NOME_RESTORE_POINT_3]**: [DATA_HORA] - [DESCRIÇÃO] - [HASH_ESTADO]

## Debug e Troubleshooting

### Logs de Debug
```
DEBUG_MODE=[ENABLED/DISABLED]
LOG_LEVEL=[DEBUG/INFO/WARN/ERROR]
LAST_ERROR=[DATA_HORA] - [DESCRIÇÃO_ERRO]
ERROR_COUNT_TODAY=[NÚMERO_ERROS]
```

### Informações de Sistema
```
FRAMEWORK_INSTALL_DATE=[DATA_INSTALAÇÃO]
FRAMEWORK_SOURCE=[LOCAL/REMOTE] - [VERSÃO_ORIGEM]
COMPATIBILITY_MODE=[ENABLED/DISABLED]
EXPERIMENTAL_FEATURES=[LISTA_FEATURES_EXPERIMENTAIS]
```

### Estado de Sincronização
```
MEMORY_BANK_SYNC=[IN_SYNC/OUT_OF_SYNC]
LAST_SYNC_ATTEMPT=[DATA_HORA]
SYNC_ERRORS=[NÚMERO_ERROS_SYNC]
PENDING_UPDATES=[LISTA_ATUALIZAÇÕES_PENDENTES]
```

---

*Este arquivo mantém o estado completo do framework RIPER-Copilot. É atualizado automaticamente a cada transição de modo ou fase.*

## Comandos para Verificação de Estado

### Verificação Rápida
```bash
# Verificar estado atual
riper status

# Verificar saúde do framework  
riper health-check

# Verificar integridade dos arquivos
riper validate
```

### Debug e Troubleshooting
```bash
# Modo debug
riper debug enable

# Verificar logs
riper logs --last 24h

# Restaurar estado
riper restore [RESTORE_POINT_NAME]
```

## Automação de Estado

### Triggers Automáticos
- **Backup automático**: A cada [FREQUÊNCIA]
- **Validação automática**: A cada transição de modo
- **Limpeza de logs**: A cada [FREQUÊNCIA]
- **Health check**: A cada [FREQUÊNCIA]

### Notificações Configuradas
- **Modo muito longo**: Avisar após [TEMPO] no mesmo modo
- **Erro crítico**: Notificação imediata
- **Backup falhou**: Notificação dentro de [TEMPO]
- **Estado inconsistente**: Notificação imediata
```

## Instruções de Uso

1. **Não edite manualmente** - este arquivo é mantido automaticamente pelo framework
2. **Use para debug** - consulte quando algo não estiver funcionando como esperado
3. **Monitor de saúde** - verifique alertas e avisos regularmente
4. **Restore points** - use para voltar a estados anteriores se necessário

## Variáveis de Estado Obrigatórias
- PROJECT_PHASE
- CURRENT_MODE
- PROJECT_NAME
- FRAMEWORK_VERSION
- LAST_UPDATED

## Variáveis Opcionais
- Todas as métricas de produtividade
- Configurações personalizadas
- Estado de backup (para projetos simples)
- Logs de debug (se não habilitado)

Este arquivo é o "centro de controle" do framework RIPER-Copilot e deve ser consultado sempre que houver dúvidas sobre o estado atual do projeto ou do framework.

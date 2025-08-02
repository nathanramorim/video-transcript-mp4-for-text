# Template: techContext.md

Este é o template para o arquivo `techContext.md` do banco de memória do RIPER-Copilot.

```markdown
# Contexto Técnico: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Stack de Tecnologia

### Frontend
- **Framework principal**: [FRAMEWORK] v[VERSÃO] - [Justificativa da escolha]
- **Linguagem**: [LINGUAGEM] - [Versão/padrão usado]
- **Bibliotecas principais**:
  - [BIBLIOTECA_1]: v[VERSÃO] - [Propósito]
  - [BIBLIOTECA_2]: v[VERSÃO] - [Propósito]
  - [BIBLIOTECA_3]: v[VERSÃO] - [Propósito]
- **Ferramentas de build**: [FERRAMENTA] v[VERSÃO]
- **Package manager**: [MANAGER] v[VERSÃO]

### Backend
- **Framework principal**: [FRAMEWORK] v[VERSÃO] - [Justificativa da escolha]
- **Linguagem**: [LINGUAGEM] - [Versão usado]
- **Runtime**: [RUNTIME] v[VERSÃO]
- **Bibliotecas principais**:
  - [BIBLIOTECA_1]: v[VERSÃO] - [Propósito]
  - [BIBLIOTECA_2]: v[VERSÃO] - [Propósito]
  - [BIBLIOTECA_3]: v[VERSÃO] - [Propósito]

### Base de Dados
- **Banco principal**: [BANCO] v[VERSÃO] - [Justificativa]
- **ORM/ODM**: [ORM] v[VERSÃO] - [Se aplicável]
- **Banco para cache**: [BANCO_CACHE] v[VERSÃO] - [Se aplicável]
- **Banco para sessões**: [BANCO_SESSAO] v[VERSÃO] - [Se aplicável]

### Infraestrutura
- **Cloud Provider**: [PROVIDER] - [Região principal]
- **Containerização**: [TECNOLOGIA] v[VERSÃO]
- **Orchestração**: [ORQUESTRADOR] v[VERSÃO] - [Se aplicável]
- **Web Server**: [SERVIDOR] v[VERSÃO]
- **Proxy/Load Balancer**: [PROXY] v[VERSÃO] - [Se aplicável]

## Configuração do Ambiente de Desenvolvimento

### Pré-requisitos
```bash
# Versões necessárias
[LINGUAGEM]: [VERSÃO_MÍNIMA]+
[RUNTIME]: [VERSÃO_MÍNIMA]+
[BANCO_DADOS]: [VERSÃO_MÍNIMA]+
[FERRAMENTA_1]: [VERSÃO_MÍNIMA]+
```

### Instalação Local
```bash
# 1. Clonar repositório
git clone [URL_REPOSITORIO]
cd [NOME_PROJETO]

# 2. Instalar dependências
[COMANDO_INSTALACAO_DEPS]

# 3. Configurar banco de dados
[COMANDOS_SETUP_BD]

# 4. Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com configurações locais

# 5. Executar migrações (se aplicável)
[COMANDO_MIGRATIONS]

# 6. Iniciar desenvolvimento
[COMANDO_DEV]
```

### Configurações de Ambiente
- **Arquivo de configuração**: [NOME_ARQUIVO] 
- **Localização**: [CAMINHO_ARQUIVO]
- **Variáveis obrigatórias**:
  ```
  [VAR_1]=[DESCRIÇÃO_E_EXEMPLO]
  [VAR_2]=[DESCRIÇÃO_E_EXEMPLO]
  [VAR_3]=[DESCRIÇÃO_E_EXEMPLO]
  ```
- **Variáveis opcionais**:
  ```
  [VAR_OPCIONAL_1]=[DESCRIÇÃO_E_VALOR_PADRÃO]
  [VAR_OPCIONAL_2]=[DESCRIÇÃO_E_VALOR_PADRÃO]
  ```

## Dependências Detalhadas

### Dependências de Produção
```json
{
  "[DEPENDENCIA_1]": "[VERSÃO]",
  "[DEPENDENCIA_2]": "[VERSÃO]",
  "[DEPENDENCIA_3]": "[VERSÃO]"
}
```

#### [DEPENDENCIA_1] v[VERSÃO]
- **Propósito**: [Para que é usada]
- **Alternativas consideradas**: [Outras opções avaliadas]
- **Criticidade**: [Alta/Média/Baixa]
- **Licença**: [TIPO_LICENÇA]
- **Última atualização**: [DATA_ÚLTIMA_ATUALIZAÇÃO]
- **Vulnerabilidades conhecidas**: [Nenhuma/Lista]

#### [DEPENDENCIA_2] v[VERSÃO]
- **Propósito**: [Para que é usada]
- **Alternativas consideradas**: [Outras opções avaliadas]
- **Criticidade**: [Alta/Média/Baixa]
- **Licença**: [TIPO_LICENÇA]
- **Última atualização**: [DATA_ÚLTIMA_ATUALIZAÇÃO]
- **Vulnerabilidades conhecidas**: [Nenhuma/Lista]

### Dependências de Desenvolvimento
```json
{
  "[DEP_DEV_1]": "[VERSÃO]",
  "[DEP_DEV_2]": "[VERSÃO]",
  "[DEP_DEV_3]": "[VERSÃO]"
}
```

## Restrições Técnicas

### Limitações de Performance
- **Latência máxima aceitável**: [VALOR] ms para [OPERAÇÃO]
- **Throughput mínimo**: [VALOR] requests/segundo
- **Uso de memória**: Máximo [VALOR] MB em produção
- **Tamanho de payload**: Máximo [VALOR] KB por request

### Limitações de Compatibilidade
- **Browsers suportados**: [LISTA_BROWSERS_E_VERSÕES]
- **Dispositivos móveis**: [SUPORTE_MÓVEL]
- **Acessibilidade**: [PADRÕES_A11Y_SEGUIDOS]
- **Internacionalização**: [IDIOMAS_SUPORTADOS]

### Limitações de Infraestrutura
- **Regiões disponíveis**: [LISTA_REGIÕES]
- **Limites de storage**: [VALOR_LÍMITE]
- **Limites de banda**: [VALOR_LÍMITE]
- **Número máximo de instâncias**: [VALOR_LÍMITE]

## Build e Deployment

### Processo de Build
```bash
# Build para desenvolvimento
[COMANDO_BUILD_DEV]

# Build para produção
[COMANDO_BUILD_PROD]

# Build para testes
[COMANDO_BUILD_TEST]
```

### Pipeline de CI/CD
- **Ferramenta**: [FERRAMENTA_CI_CD]
- **Trigger**: [QUANDO_EXECUTA] (push, PR, schedule, etc.)
- **Stages**:
  1. **Lint & Format**: [COMANDO_LINT]
  2. **Test**: [COMANDO_TEST]
  3. **Build**: [COMANDO_BUILD]
  4. **Security Scan**: [COMANDO_SECURITY]
  5. **Deploy**: [COMANDO_DEPLOY]

### Ambientes de Deployment
#### Desenvolvimento
- **URL**: [URL_DEV]
- **Branch**: [BRANCH_DEV]
- **Deploy automático**: [SIM/NÃO]
- **Configurações específicas**: [CONFIGS_DEV]

#### Staging
- **URL**: [URL_STAGING]
- **Branch**: [BRANCH_STAGING]
- **Deploy automático**: [SIM/NÃO]
- **Configurações específicas**: [CONFIGS_STAGING]

#### Produção
- **URL**: [URL_PROD]
- **Branch**: [BRANCH_PROD]
- **Deploy automático**: [SIM/NÃO]
- **Configurações específicas**: [CONFIGS_PROD]
- **Processo de aprovação**: [PROCESSO_APROVAÇÃO]

## Estratégia de Testes

### Testes Unitários
- **Framework**: [FRAMEWORK_TEST] v[VERSÃO]
- **Coverage mínimo**: [PORCENTAGEM]%
- **Comando**: `[COMANDO_UNIT_TEST]`
- **Localização**: [PASTA_TESTES_UNITÁRIOS]
- **Convenções**: [CONVENÇÕES_NOMENCLATURA]

### Testes de Integração
- **Framework**: [FRAMEWORK_INTEGRATION] v[VERSÃO]
- **Banco de teste**: [BANCO_TEST]
- **Comando**: `[COMANDO_INTEGRATION_TEST]`
- **Localização**: [PASTA_TESTES_INTEGRAÇÃO]

### Testes End-to-End
- **Framework**: [FRAMEWORK_E2E] v[VERSÃO]
- **Browser**: [BROWSER_E2E]
- **Comando**: `[COMANDO_E2E_TEST]`
- **Localização**: [PASTA_TESTES_E2E]

### Testes de Performance
- **Ferramenta**: [FERRAMENTA_PERF] v[VERSÃO]
- **Métricas monitoradas**: [LISTA_MÉTRICAS]
- **Thresholds**: [VALORES_LIMITE]

## Monitoramento e Observabilidade

### Logging
- **Framework**: [FRAMEWORK_LOG] v[VERSÃO]
- **Nível padrão**: [NÍVEL_LOG]
- **Formato**: [FORMATO_LOG]
- **Destino**: [ONDE_LOGS_SÃO_ENVIADOS]

### Métricas
- **Ferramenta**: [FERRAMENTA_MÉTRICAS] v[VERSÃO]
- **Métricas de negócio**: [LISTA_MÉTRICAS_NEGÓCIO]
- **Métricas técnicas**: [LISTA_MÉTRICAS_TÉCNICAS]
- **Dashboards**: [LINKS_DASHBOARDS]

### APM (Application Performance Monitoring)
- **Ferramenta**: [FERRAMENTA_APM] v[VERSÃO]
- **Instrumentação**: [NÍVEL_INSTRUMENTAÇÃO]
- **Alertas configurados**: [LISTA_ALERTAS]

## Segurança

### Autenticação e Autorização
- **Método de autenticação**: [JWT/Session/OAuth/etc.]
- **Provider de identidade**: [PROVIDER_IDENTIDADE]
- **Expiração de sessão**: [TEMPO_EXPIRAÇÃO]
- **Refresh tokens**: [SIM/NÃO]

### Criptografia
- **Dados em trânsito**: [TLS_VERSION]
- **Dados em repouso**: [ALGORITMO_CRIPTOGRAFIA]
- **Hashing de senhas**: [ALGORITMO_HASH]

### Validação e Sanitização
- **Validação de input**: [BIBLIOTECA_VALIDAÇÃO]
- **Sanitização**: [MÉTODO_SANITIZAÇÃO]
- **Rate limiting**: [CONFIGURAÇÃO_RATE_LIMIT]

## Configurações de Qualidade

### Linting e Formatação
- **Linter**: [LINTER] v[VERSÃO]
- **Formatter**: [FORMATTER] v[VERSÃO]
- **Configuração**: [ARQUIVO_CONFIG]
- **Pre-commit hooks**: [SIM/NÃO] - [LISTA_HOOKS]

### Code Quality
- **Ferramenta de análise**: [FERRAMENTA] v[VERSÃO]
- **Métricas monitoradas**: [MÉTRICAS_QUALIDADE]
- **Thresholds**: [VALORES_LIMITE_QUALIDADE]

## Backup e Disaster Recovery

### Estratégia de Backup
- **Frequência**: [FREQUÊNCIA_BACKUP]
- **Retenção**: [TEMPO_RETENÇÃO]
- **Localização**: [ONDE_BACKUPS_FICAM]
- **Teste de restore**: [FREQUÊNCIA_TESTE]

### Disaster Recovery
- **RTO (Recovery Time Objective)**: [TEMPO_MÁXIMO_RECOVERY]
- **RPO (Recovery Point Objective)**: [PERDA_MÁXIMA_DADOS]
- **Processo de failover**: [DESCRIÇÃO_PROCESSO]

## Troubleshooting

### Problemas Comuns
#### [PROBLEMA_1]
- **Sintomas**: [DESCRIÇÃO_SINTOMAS]
- **Causa provável**: [CAUSA_PROVÁVEL]
- **Solução**: [PASSOS_SOLUÇÃO]

#### [PROBLEMA_2]
- **Sintomas**: [DESCRIÇÃO_SINTOMAS]
- **Causa provável**: [CAUSA_PROVÁVEL]
- **Solução**: [PASSOS_SOLUÇÃO]

### Comandos Úteis para Debug
```bash
# Verificar logs
[COMANDO_LOGS]

# Verificar status do sistema
[COMANDO_STATUS]

# Reiniciar serviços
[COMANDO_RESTART]

# Conectar ao banco de dados
[COMANDO_DB_CONNECT]
```

## Atualizações e Manutenção

### Política de Atualizações
- **Dependências críticas**: [POLÍTICA_CRÍTICAS]
- **Dependências não-críticas**: [POLÍTICA_NÃO_CRÍTICAS]
- **Framework principal**: [POLÍTICA_FRAMEWORK]

### Cronograma de Manutenção
- **Security patches**: [FREQUÊNCIA_SECURITY]
- **Dependency updates**: [FREQUÊNCIA_DEPS]
- **Framework upgrades**: [FREQUÊNCIA_FRAMEWORK]

---

*Este documento descreve o contexto técnico completo do projeto. Deve ser atualizado sempre que tecnologias, dependências ou configurações mudarem.*

## Histórico de Revisões
- **v1.0** ([DATA]): Versão inicial - [AUTOR]
- **v1.1** ([DATA]): [Descrição das mudanças] - [AUTOR]
```

## Instruções de Preenchimento

1. **Seja específico com versões** - sempre inclua números de versão
2. **Documente comandos reais** - use comandos que realmente funcionam
3. **Inclua justificativas** - explique por que tecnologias foram escolhidas
4. **Mantenha atualizado** - especialmente versões e configurações
5. **Teste as instruções** - garanta que setup funciona para novos desenvolvedores

## Campos Obrigatórios
- Stack de Tecnologia completo
- Configuração do Ambiente de Desenvolvimento
- Dependências principais com versões
- Processo de Build básico
- Estratégia de Testes

## Campos Opcionais
- Todas as seções de monitoramento (se não aplicável)
- Disaster Recovery (para projetos simples)
- APM (se não usado)
- Testes de Performance (se não necessários)

Este template garante que toda informação técnica necessária para desenvolver, deployar e manter o projeto esteja documentada de forma acessível.

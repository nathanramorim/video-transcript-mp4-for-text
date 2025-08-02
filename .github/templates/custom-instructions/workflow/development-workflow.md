description: MUST BE APPLIED WHEN working on development workflow, version control, CI/CD, and development process improvements. Covers workflow-specific patterns including Git practices, build processes, and deployment strategies.
applyTo: "**/.github/**/*,**/.gitlab-ci.yml,**/Jenkinsfile,**/azure-pipelines.yml,**/bitbucket-pipelines.yml,**/buildspec.yml,**/Dockerfile,**/docker-compose.yml,**/Makefile,**/.gitignore,**/.gitattributes,**/scripts/**/*"
alwaysApply: false

# Development Workflow Guidelines: [NOME_DO_PROJETO]

## Development Philosophy
<development_philosophy>
**Methodology**: [METODOLOGIA_DESENVOLVIMENTO_DETECTADA]
**Git Strategy**: [ESTRATEGIA_GIT_DETECTADA]
**CI/CD Platform**: [PLATAFORMA_CI_CD_DETECTADA]

### Core Values
- Collaboration and knowledge sharing
- Continuous learning and improvement
- Quality-first development approach
- Sustainable development practices
- Automated and reliable processes

### Team Practices
- Code review culture: [CULTURA_CODE_REVIEW_DETECTADA]
- Pair programming: [PAIR_PROGRAMMING_DETECTADO]
- Test-driven development: [TDD_DETECTADO]
- Documentation standards: [PADROES_DOCUMENTACAO_DETECTADOS]

[FILOSOFIA_DESENVOLVIMENTO_BASEADA_PROJECTBRIEF]
</development_philosophy>

## Version Control Workflow
<git_workflow>
**Branching Strategy**: [ESTRATEGIA_BRANCH_DETECTADA]
**Merge Strategy**: [ESTRATEGIA_MERGE_DETECTADA]

### Branch Structure
```bash
# [ESTRUTURA_BRANCHES_DETECTADA]
main/master          # Production-ready code
develop             # Integration branch
feature/*           # Feature development
hotfix/*            # Production fixes
release/*           # Release preparation
```

### Commit Message Format
```bash
# [FORMATO_COMMIT_DETECTADO]
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types
- **feat**: New feature implementation
- **fix**: Bug fixes
- **docs**: Documentation changes
- **style**: Code style changes
- **refactor**: Code refactoring
- **test**: Test additions or modifications
- **chore**: Build process or auxiliary tool changes

### Branch Naming Conventions
```bash
# [CONVENCOES_BRANCH_DETECTADAS]
feature/AUTH-123-add-user-authentication
bugfix/FIX-456-resolve-login-issue
hotfix/URGENT-789-security-patch
release/v1.2.0
```

### Pull Request Process
```markdown
# [PROCESSO_PR_DETECTADO]
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No merge conflicts
```
</git_workflow>

## Development Environment
<development_environment>
### Environment Setup
```bash
# [SETUP_AMBIENTE_DETECTADO]
```

### Required Tools
- **IDE/Editor**: [EDITOR_DETECTADO]
- **Language Runtime**: [RUNTIME_DETECTADO]
- **Package Manager**: [GERENCIADOR_PACOTES_DETECTADO]
- **Database**: [DATABASE_DESENVOLVIMENTO_DETECTADO]
- **Build Tools**: [FERRAMENTAS_BUILD_DETECTADAS]

### Environment Configuration
```[LINGUAGEM_DETECTADA]
// [CONFIGURACAO_AMBIENTE_DETECTADA]
```

### Local Development Guidelines
- Use consistent development environment: [AMBIENTE_CONSISTENTE]
- Environment variable management: [GERENCIAMENTO_ENV_VARS]
- Local database setup: [SETUP_DB_LOCAL]
- Hot reloading configuration: [CONFIG_HOT_RELOAD]

### Docker Development
```dockerfile
# [DOCKER_DEV_DETECTADO]
```

### Development Services
- Local API server: [SERVIDOR_API_LOCAL]
- Database services: [SERVICOS_DB_DETECTADOS]
- Mock services: [SERVICOS_MOCK_DETECTADOS]
- Development proxy: [PROXY_DESENVOLVIMENTO]
</development_environment>

## Build and Deployment
<build_deployment>
### Build Process
```bash
# [PROCESSO_BUILD_DETECTADO]
```

### Build Configuration
```[LINGUAGEM_DETECTADA]
// [CONFIGURACAO_BUILD_DETECTADA]
```

### Build Stages
1. **Dependencies**: [INSTALACAO_DEPENDENCIAS]
2. **Compilation**: [PROCESSO_COMPILACAO]
3. **Testing**: [EXECUCAO_TESTES]
4. **Linting**: [VERIFICACAO_LINT]
5. **Packaging**: [EMPACOTAMENTO]
6. **Deployment**: [PROCESSO_DEPLOYMENT]

### Environment-Specific Builds
- **Development**: [BUILD_DESENVOLVIMENTO]
- **Staging**: [BUILD_STAGING]
- **Production**: [BUILD_PRODUCAO]

### Artifact Management
- Build artifacts: [ARTEFATOS_BUILD_DETECTADOS]
- Version tagging: [TAGGEAMENTO_VERSAO]
- Artifact storage: [ARMAZENAMENTO_ARTEFATOS]
- Release notes: [NOTAS_RELEASE_DETECTADAS]

### Deployment Strategies
```yaml
# [ESTRATEGIAS_DEPLOYMENT_DETECTADAS]
```

### Deployment Environments
- **Development**: [AMBIENTE_DEV_DETECTADO]
- **Staging**: [AMBIENTE_STAGING_DETECTADO]
- **Production**: [AMBIENTE_PROD_DETECTADO]
- **Preview/Review**: [AMBIENTE_PREVIEW_DETECTADO]
</build_deployment>

## Continuous Integration
<continuous_integration>
**CI Platform**: [PLATAFORMA_CI_DETECTADA]

### CI Pipeline Configuration
```yaml
# [CONFIGURACAO_PIPELINE_CI_DETECTADA]
```

### Pipeline Stages
1. **Checkout**: Source code retrieval
2. **Setup**: Environment and dependency setup
3. **Lint**: Code style and quality checks
4. **Test**: Automated test execution
5. **Build**: Application build process
6. **Security**: Security vulnerability scanning
7. **Package**: Artifact creation and storage

### Test Automation
- **Unit Tests**: [TESTES_UNITARIOS_CI]
- **Integration Tests**: [TESTES_INTEGRACAO_CI]
- **E2E Tests**: [TESTES_E2E_CI]
- **Performance Tests**: [TESTES_PERFORMANCE_CI]

### Quality Gates
```[LINGUAGEM_DETECTADA]
// [QUALITY_GATES_DETECTADOS]
```

### CI Best Practices
- Fast feedback loops: [FEEDBACK_RAPIDO]
- Parallel execution: [EXECUCAO_PARALELA_CI]
- Fail fast strategy: [ESTRATEGIA_FAIL_FAST]
- Build caching: [CACHE_BUILD_DETECTADO]

### Notification Strategy
- Build status notifications: [NOTIFICACOES_BUILD]
- Failure alerts: [ALERTAS_FALHA_DETECTADOS]
- Success confirmations: [CONFIRMACOES_SUCESSO]
- Team communication: [COMUNICACAO_EQUIPE_CI]
</continuous_integration>

## Code Quality and Standards
<code_quality>
### Code Style Guidelines
```[LINGUAGEM_DETECTADA]
// [DIRETRIZES_ESTILO_CODIGO_DETECTADAS]
```

### Linting Configuration
```[LINGUAGEM_DETECTADA]
// [CONFIGURACAO_LINTING_DETECTADA]
```

### Code Formatting
- **Formatter**: [FORMATADOR_DETECTADO]
- **Rules**: [REGRAS_FORMATACAO_DETECTADAS]
- **IDE Integration**: [INTEGRACAO_IDE_FORMATACAO]
- **Pre-commit hooks**: [HOOKS_PRE_COMMIT_DETECTADOS]

### Static Analysis
- **Tools**: [FERRAMENTAS_ANALISE_ESTATICA]
- **Rules**: [REGRAS_ANALISE_DETECTADAS]
- **Thresholds**: [THRESHOLDS_QUALIDADE_DETECTADOS]
- **Reports**: [RELATORIOS_QUALIDADE_DETECTADOS]

### Code Review Standards
```markdown
# [PADROES_CODE_REVIEW_DETECTADOS]
```

### Review Checklist
- [ ] Code follows project conventions
- [ ] Business logic is correct
- [ ] Error handling is appropriate
- [ ] Tests are comprehensive
- [ ] Documentation is updated
- [ ] Performance considerations addressed
- [ ] Security implications reviewed
- [ ] No code duplication introduced
</code_quality>

## Testing Strategy
<testing_strategy>
### Testing Pyramid
```[LINGUAGEM_DETECTADA]
// [ESTRATEGIA_PIRAMIDE_TESTES_DETECTADA]
```

### Test Categories
- **Unit Tests**: [CATEGORIA_UNIT_TESTS]
- **Integration Tests**: [CATEGORIA_INTEGRATION_TESTS]
- **Contract Tests**: [CATEGORIA_CONTRACT_TESTS]
- **E2E Tests**: [CATEGORIA_E2E_TESTS]

### Test Execution Strategy
- **Local Testing**: [EXECUCAO_LOCAL_TESTES]
- **CI Testing**: [EXECUCAO_CI_TESTES]
- **Pre-deployment Testing**: [TESTES_PRE_DEPLOYMENT]
- **Smoke Testing**: [TESTES_SMOKE_DETECTADOS]

### Test Data Management
```[LINGUAGEM_DETECTADA]
// [GERENCIAMENTO_DADOS_TESTE_DETECTADO]
```

### Performance Testing
- **Load Testing**: [TESTES_CARGA_DETECTADOS]
- **Stress Testing**: [TESTES_STRESS_DETECTADOS]
- **Performance Budgets**: [ORCAMENTOS_PERFORMANCE]
- **Monitoring**: [MONITORAMENTO_PERFORMANCE_TESTES]
</testing_strategy>

## Release Management
<release_management>
### Release Strategy
**Release Cycle**: [CICLO_RELEASE_DETECTADO]
**Versioning**: [VERSIONAMENTO_DETECTADO]

### Release Types
- **Major Releases**: [RELEASES_MAJOR_DETECTADAS]
- **Minor Releases**: [RELEASES_MINOR_DETECTADAS]
- **Patch Releases**: [RELEASES_PATCH_DETECTADAS]
- **Hotfix Releases**: [RELEASES_HOTFIX_DETECTADAS]

### Release Process
```bash
# [PROCESSO_RELEASE_DETECTADO]
```

### Release Planning
1. **Feature Freeze**: [FEATURE_FREEZE_DETECTADO]
2. **Testing Phase**: [FASE_TESTES_RELEASE]
3. **Release Candidate**: [RELEASE_CANDIDATE_PROCESSO]
4. **Production Deployment**: [DEPLOYMENT_PRODUCAO]
5. **Post-Release Monitoring**: [MONITORAMENTO_POS_RELEASE]

### Release Documentation
- **Release Notes**: [NOTAS_RELEASE_DETECTADAS]
- **Migration Guides**: [GUIAS_MIGRACAO_DETECTADOS]
- **API Documentation**: [DOCUMENTACAO_API_RELEASE]
- **User Documentation**: [DOCUMENTACAO_USUARIO_RELEASE]

### Rollback Strategy
```bash
# [ESTRATEGIA_ROLLBACK_DETECTADA]
```

### Release Monitoring
- **Deployment metrics**: [METRICAS_DEPLOYMENT]
- **Application health**: [SAUDE_APLICACAO_RELEASE]
- **User feedback**: [FEEDBACK_USUARIO_RELEASE]
- **Error monitoring**: [MONITORAMENTO_ERROS_RELEASE]
</release_management>

## Collaboration and Communication
<collaboration>
### Team Communication
- **Daily standups**: [STANDUPS_DETECTADOS]
- **Sprint planning**: [PLANEJAMENTO_SPRINT]
- **Retrospectives**: [RETROSPECTIVAS_DETECTADAS]
- **Code reviews**: [REVISOES_CODIGO_COLABORACAO]

### Documentation Practices
```markdown
# [PRATICAS_DOCUMENTACAO_DETECTADAS]
```

### Knowledge Sharing
- **Technical documentation**: [DOC_TECNICA_DETECTADA]
- **Architecture decisions**: [DECISOES_ARQUITETURA_DOC]
- **Best practices**: [MELHORES_PRATICAS_DOC]
- **Troubleshooting guides**: [GUIAS_TROUBLESHOOTING]

### Onboarding Process
1. **Environment setup**: [SETUP_ONBOARDING]
2. **Codebase overview**: [OVERVIEW_CODEBASE]
3. **Development workflow**: [WORKFLOW_ONBOARDING]
4. **First contribution**: [PRIMEIRA_CONTRIBUICAO]

### Mentoring and Growth
- **Code review mentoring**: [MENTORING_CODE_REVIEW]
- **Pair programming**: [PAIR_PROGRAMMING_MENTORING]
- **Technical discussions**: [DISCUSSOES_TECNICAS]
- **Learning resources**: [RECURSOS_APRENDIZADO]
</collaboration>

## Monitoring and Observability
<monitoring_observability>
### Application Monitoring
```[LINGUAGEM_DETECTADA]
// [MONITORAMENTO_APLICACAO_DETECTADO]
```

### Logging Strategy
- **Log levels**: [NIVEIS_LOG_DETECTADOS]
- **Log aggregation**: [AGREGACAO_LOGS_DETECTADA]
- **Log analysis**: [ANALISE_LOGS_DETECTADA]
- **Log retention**: [RETENCAO_LOGS_DETECTADA]

### Metrics Collection
```[LINGUAGEM_DETECTADA]
// [COLETA_METRICAS_DETECTADA]
```

### Alerting Strategy
- **Critical alerts**: [ALERTAS_CRITICOS_DETECTADOS]
- **Warning alerts**: [ALERTAS_WARNING_DETECTADOS]
- **Notification channels**: [CANAIS_NOTIFICACAO_DETECTADOS]
- **Escalation procedures**: [PROCEDIMENTOS_ESCALACAO]

### Performance Monitoring
- **Response time monitoring**: [MONITOR_TEMPO_RESPOSTA]
- **Resource utilization**: [MONITOR_RECURSOS]
- **Error rate tracking**: [RASTREAMENTO_TAXA_ERRO]
- **User experience monitoring**: [MONITOR_EXPERIENCIA_USUARIO]
</monitoring_observability>

---
*Development workflow guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
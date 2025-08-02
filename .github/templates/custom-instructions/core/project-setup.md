description: MUST BE APPLIED WHEN setting up new project components, configuring environments, or managing project dependencies. Covers project setup patterns including environment configuration, build setup, and project scaffolding.
applyTo: "**/package.json,**/pom.xml,**/build.gradle,**/requirements.txt,**/pyproject.toml,**/*.csproj,**/Dockerfile,**/docker-compose.yml,**/README.md,**/LICENSE,**/.env*,**/config/**/*"
alwaysApply: false

# Project Setup Guidelines: [NOME_DO_PROJETO]

## Project Overview
<project_overview>
[CONTEXTO_GERAL_BASEADO_PROJECTBRIEF]

### Project Purpose
- Main objectives and goals
- Target audience and use cases
- Key features and functionality
- Technology stack and architecture decisions
- Project scope and boundaries
</project_overview>

## Environment Setup

### Prerequisites
<prerequisites>
**Detected Prerequisites:**
- [LINGUAGEM_DETECTADA] [VERSAO_DETECTADA]
- [DEPENDENCIAS_SISTEMA_DETECTADAS]
- [FERRAMENTAS_DESENVOLVIMENTO_DETECTADAS]

### System Requirements
- Operating system compatibility
- Memory and storage requirements
- Network and connectivity needs
- Required accounts and access permissions
</prerequisites>

### Installation Guide
<installation_guide>
**Automated Setup:**
```bash
# [COMANDOS_SETUP_DETECTADOS]
```

**Manual Setup Steps:**
1. Install [LINGUAGEM_DETECTADA] [VERSAO_DETECTADA]
2. Install package manager: [GERENCIADOR_PACOTES]
3. Clone repository and navigate to project
4. Install dependencies: [COMANDO_INSTALL_DEPS]
5. Configure environment variables
6. Run initial setup: [COMANDO_SETUP_INICIAL]
7. Verify installation: [COMANDO_VERIFICACAO]
</installation_guide>

## Configuration Management

### Environment Variables
<environment_variables>
**Required Environment Variables:**
```env
# [VARIAVEIS_AMBIENTE_DETECTADAS]
```

**Environment-Specific Configuration:**
- Development: `.env.development`
- Testing: `.env.test`
- Production: `.env.production`
</environment_variables>

### Configuration Files
<configuration_files>
**Key Configuration Files:**
- [ARQUIVOS_CONFIG_DETECTADOS]

**Configuration Patterns:**
- Use environment-specific configuration
- Validate configuration on startup
- Document all configuration options
- Use secure defaults
- Version configuration changes
</configuration_files>

## Build and Deployment

### Build Process
<build_process>
**Build Commands:**
```bash
# Development build
[COMANDO_BUILD_DEV]

# Production build
[COMANDO_BUILD_PROD]

# Test build
[COMANDO_BUILD_TEST]
```

**Build Configuration:**
- Build tool: [FERRAMENTA_BUILD_DETECTADA]
- Build scripts: [SCRIPTS_BUILD_DETECTADOS]
- Asset management: [ESTRATEGIA_ASSETS]
- Optimization settings: [CONFIGURACOES_OTIMIZACAO]
</build_process>

### Deployment Strategy
<deployment_strategy>
**Deployment Environments:**
- Development: [ESTRATEGIA_DEV]
- Staging: [ESTRATEGIA_STAGING]
- Production: [ESTRATEGIA_PROD]

**Deployment Tools:**
- Container: [CONTAINER_DETECTADO]
- Orchestration: [ORQUESTRACAO_DETECTADA]
- CI/CD: [PIPELINE_DETECTADO]
</deployment_strategy>

## Development Workflow

### Version Control
<version_control>
**Git Configuration:**
- Branching strategy: [ESTRATEGIA_BRANCH]
- Commit conventions: [CONVENCOES_COMMIT]
- PR/MR process: [PROCESSO_PR]

**Repository Structure:**
- Main branches: [BRANCHES_PRINCIPAIS]
- Development workflow: [WORKFLOW_DESENVOLVIMENTO]
- Release process: [PROCESSO_RELEASE]
</version_control>

### Development Tools
<development_tools>
**Required Tools:**
- IDE/Editor: [EDITOR_RECOMENDADO]
- Debugging tools: [FERRAMENTAS_DEBUG]
- Testing tools: [FERRAMENTAS_TESTE]
- Code quality: [FERRAMENTAS_QUALIDADE]

**Tool Configuration:**
- Linting: [CONFIG_LINTING]
- Formatting: [CONFIG_FORMATACAO]
- Type checking: [CONFIG_TIPOS]
</development_tools>

## Testing Setup

### Test Framework Configuration
<test_framework>
**Testing Stack:**
- Unit tests: [FRAMEWORK_TESTE_UNITARIO]
- Integration tests: [FRAMEWORK_TESTE_INTEGRACAO]
- E2E tests: [FRAMEWORK_TESTE_E2E]

**Test Commands:**
```bash
# Run all tests
[COMANDO_TESTE_ALL]

# Run unit tests
[COMANDO_TESTE_UNIT]

# Run integration tests
[COMANDO_TESTE_INTEGRATION]

# Run with coverage
[COMANDO_TESTE_COVERAGE]
```
</test_framework>

### Test Environment Setup
<test_environment>
**Test Database:**
- Test DB setup: [SETUP_DB_TESTE]
- Test data management: [GERENCIAMENTO_DADOS_TESTE]
- Test cleanup: [LIMPEZA_TESTE]

**Mock Configuration:**
- External services: [MOCKS_SERVICOS_EXTERNOS]
- API mocking: [MOCKS_API]
- Test doubles: [TEST_DOUBLES]
</test_environment>

## Maintenance Procedures

### Regular Maintenance
<maintenance_procedures>
**Dependency Management:**
- Update schedule: [CRONOGRAMA_UPDATES]
- Security patches: [PROCESSO_SECURITY_PATCHES]
- Version compatibility: [ESTRATEGIA_COMPATIBILIDADE]

**Performance Monitoring:**
- Monitoring tools: [FERRAMENTAS_MONITORING]
- Performance metrics: [METRICAS_PERFORMANCE]
- Alerting setup: [CONFIGURACAO_ALERTAS]
</maintenance_procedures>

### Documentation Standards
<documentation_standards>
**Documentation Requirements:**
- Code documentation: [PADROES_DOC_CODIGO]
- API documentation: [PADROES_DOC_API]
- User documentation: [PADROES_DOC_USUARIO]

**Documentation Tools:**
- Documentation generator: [FERRAMENTA_DOC]
- Documentation hosting: [HOSTING_DOC]
- Documentation maintenance: [MANUTENCAO_DOC]
</documentation_standards>

---
*Project setup guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
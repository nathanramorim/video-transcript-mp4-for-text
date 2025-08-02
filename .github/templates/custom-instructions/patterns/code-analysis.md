description: MUST BE APPLIED WHEN performing code analysis, refactoring, or quality assessment. Covers code analysis patterns including static analysis, quality metrics, technical debt management, and code review optimization.
applyTo: "**/*.js,**/*.ts,**/*.jsx,**/*.tsx,**/*.py,**/*.java,**/*.cs,**/*.cpp,**/*.c,**/*.h,**/*.go,**/*.rb,**/*.php,**/*.swift,**/*.kt,**/src/**/*,**/lib/**/*,**/test/**/*,**/tests/**/*,**/*test*,**/*spec*"
alwaysApply: false

# Code Analysis Guidelines: [NOME_DO_PROJETO]

## Analysis Philosophy
**Project**: [NOME_DO_PROJETO]
**Primary Language**: [LINGUAGEM_DETECTADA]
**Analysis Tools**: [FERRAMENTAS_ANALISE_DETECTADAS]

[FILOSOFIA_ANALISE_BASEADA_PROJECTBRIEF]

## Static Analysis Standards

### Code Quality Metrics
**Detected from project configuration:**
- **Complexity Threshold**: [COMPLEXIDADE_MAXIMA_DETECTADA]
- **Coverage Target**: [COBERTURA_TESTES_DETECTADA]
- **Duplication Limit**: [LIMITE_DUPLICACAO_DETECTADO]
- **Maintainability Index**: [INDICE_MANTIBILIDADE_DETECTADO]

### Analysis Tools Configuration
**Tools in use:**
- **Linting**: [LINTER_DETECTADO] (configuração: [ARQUIVO_CONFIG_LINTER])
- **Security Scanning**: [SCANNER_SEGURANCA_DETECTADO]
- **Performance Analysis**: [FERRAMENTA_PERFORMANCE_DETECTADA]
- **Dependency Analysis**: [FERRAMENTA_DEPENDENCIAS_DETECTADA]

### Quality Gates
[QUALITY_GATES_CONFIGURADOS]

## Code Review Analysis

### Review Standards
- **Minimum Reviewers**: [NUMERO_REVIEWERS_REQUERIDO]
- **Review Checklist**: [CHECKLIST_REVIEW_DETECTADO]
- **Approval Requirements**: [REQUISITOS_APROVACAO_DETECTADOS]

### Review Focus Areas
- **Architecture Compliance**: [PADROES_ARQUITETURA_REVIEW]
- **Security Checks**: [VERIFICACOES_SEGURANCA_REVIEW]
- **Performance Impact**: [ANALISE_PERFORMANCE_REVIEW]
- **Test Coverage**: [REQUISITOS_COBERTURA_REVIEW]

## Technical Debt Management

### Debt Identification
**Patterns to identify:**
- [PADROES_DEBT_DETECTADOS]
- [ANTIPADROES_DEBT_ESPECIFICOS]
- [METRICAS_DEBT_MONITORADAS]

### Debt Resolution Strategy
**Priority levels:**
- **Critical**: [CRITERIOS_DEBT_CRITICA]
- **High**: [CRITERIOS_DEBT_ALTA]
- **Medium**: [CRITERIOS_DEBT_MEDIA]
- **Low**: [CRITERIOS_DEBT_BAIXA]

## Refactoring Guidelines

### Refactoring Triggers
**When to refactor:**
- [TRIGGER_REFACTORING_1]
- [TRIGGER_REFACTORING_2]
- [TRIGGER_REFACTORING_3]

### Refactoring Patterns
**Preferred refactoring approaches:**
- [PADRAO_REFACTORING_1]: [CONTEXTO_USO]
- [PADRAO_REFACTORING_2]: [CONTEXTO_USO]
- [PADRAO_REFACTORING_3]: [CONTEXTO_USO]

### Safety Measures
**Required before refactoring:**
- [MEDIDA_SEGURANCA_1]
- [MEDIDA_SEGURANCA_2]
- [MEDIDA_SEGURANCA_3]

## Performance Analysis

### Performance Metrics
**Key metrics to monitor:**
- [METRICA_PERFORMANCE_1]: [THRESHOLD_ACEITAVEL]
- [METRICA_PERFORMANCE_2]: [THRESHOLD_ACEITAVEL]
- [METRICA_PERFORMANCE_3]: [THRESHOLD_ACEITAVEL]

### Performance Patterns
**Optimization patterns:**
- [PADRAO_OTIMIZACAO_1]: [CONTEXTO_APLICACAO]
- [PADRAO_OTIMIZACAO_2]: [CONTEXTO_APLICACAO]
- [PADRAO_OTIMIZACAO_3]: [CONTEXTO_APLICACAO]

## Code Organization Analysis

### Structure Assessment
**Evaluate:**
- [CRITERIO_ESTRUTURA_1]
- [CRITERIO_ESTRUTURA_2]
- [CRITERIO_ESTRUTURA_3]

### Modularity Guidelines
**Modularization principles:**
- [PRINCIPIO_MODULARIDADE_1]
- [PRINCIPIO_MODULARIDADE_2]
- [PRINCIPIO_MODULARIDADE_3]

## Anti-patterns to Avoid
**Project-specific anti-patterns:**
- [ANTIPADRAO_ESPECIFICO_1]: [DESCRICAO_PROBLEMA]
- [ANTIPADRAO_ESPECIFICO_2]: [DESCRICAO_PROBLEMA]
- [ANTIPADRAO_ESPECIFICO_3]: [DESCRICAO_PROBLEMA]

## Examples from Codebase
**Real examples of good patterns:**
```[LINGUAGEM_DETECTADA]
[EXEMPLO_BOA_PRATICA_1_EXTRAIDO]
```

**Examples to avoid:**
```[LINGUAGEM_DETECTADA]
[EXEMPLO_ANTIPADRAO_1_EXTRAIDO]
```

## Integration with CI/CD
**Analysis integration points:**
- [INTEGRACAO_CI_1]: [CONFIGURACAO]
- [INTEGRACAO_CI_2]: [CONFIGURACAO]
- [INTEGRACAO_CI_3]: [CONFIGURACAO]

## Monitoring and Reporting
**Analysis reporting:**
- [RELATORIO_ANALISE_1]: [FREQUENCIA]
- [RELATORIO_ANALISE_2]: [FREQUENCIA]
- [RELATORIO_ANALISE_3]: [FREQUENCIA]

---

**Generated from**: `.github/templates/custom-instructions/patterns/code-analysis.md`
**Last Updated**: [DATA_GERACAO]
**Applies to**: Code analysis, refactoring, quality assessment, and technical debt management 
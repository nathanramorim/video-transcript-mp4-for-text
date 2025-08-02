description: MUST BE APPLIED WHEN working on test code including unit tests, integration tests, test utilities, and testing infrastructure. Covers testing-specific patterns including test organization, mocking strategies, and test data management.
applyTo: "**/test/**/*,**/tests/**/*,**/__tests__/**/*,**/*.test.*,**/*.spec.*,**/cypress/**/*,**/e2e/**/*,**/fixtures/**/*,**/mocks/**/*,**/factories/**/*,**/test-utils/**/*"
alwaysApply: false

# Testing Guidelines: [NOME_DO_PROJETO]

## Testing Philosophy
<testing_philosophy>
**Testing Framework**: [FRAMEWORK_TESTE_DETECTADO]
**Test Runner**: [TEST_RUNNER_DETECTADO]
**Assertion Library**: [BIBLIOTECA_ASSERTION_DETECTADA]

### Testing Principles
- Test pyramid approach (Unit > Integration > E2E)
- Test-driven development (TDD) when appropriate
- Behavior-driven development (BDD) for complex scenarios
- Fast feedback loops and reliable tests
- Maintainable and readable test code

### Quality Standards
- Test coverage target: [COBERTURA_ALVO_DETECTADA]%
- Test execution time: [TEMPO_EXECUCAO_ALVO]
- Test reliability: [CONFIABILIDADE_TESTES]%
- Code quality in tests: [QUALIDADE_CODIGO_TESTE]

[FILOSOFIA_TESTE_BASEADA_PROJECTBRIEF]
</testing_philosophy>

## Test Organization
<test_organization>
**Directory Structure**: [ESTRUTURA_TESTE_DETECTADA]

### Test File Organization
```
[ORGANIZACAO_ARQUIVOS_TESTE_DETECTADA]
```

### Naming Conventions
- Test files: [CONVENCAO_ARQUIVOS_TESTE]
- Test classes: [CONVENCAO_CLASSES_TESTE]
- Test methods: [CONVENCAO_METODOS_TESTE]
- Test data: [CONVENCAO_DADOS_TESTE]

### Test Categories
- Unit tests: [CATEGORIA_UNIT_DETECTADA]
- Integration tests: [CATEGORIA_INTEGRATION_DETECTADA]
- E2E tests: [CATEGORIA_E2E_DETECTADA]
- Performance tests: [CATEGORIA_PERFORMANCE_DETECTADA]

### Test Grouping Strategy
- Group by feature: [AGRUPAMENTO_FEATURE_DETECTADO]
- Group by component: [AGRUPAMENTO_COMPONENTE_DETECTADO]
- Group by layer: [AGRUPAMENTO_CAMADA_DETECTADO]
- Test suites: [SUITES_TESTE_DETECTADAS]
</test_organization>

## Unit Testing
<unit_testing>
### Unit Test Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_UNITARIO_DETECTADO]
```

### Test Method Patterns
- **Arrange-Act-Assert (AAA)**: Standard pattern for test structure
- **Given-When-Then**: BDD-style test organization
- **Setup-Exercise-Verify**: Alternative test structure
- **One assertion per test**: Keep tests focused and clear

### Test Naming Conventions
```[LINGUAGEM_DETECTADA]
// [CONVENCOES_NOMES_TESTE_DETECTADAS]
```

### Parameterized Tests
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_PARAMETRIZADO_DETECTADO]
```

### Test Data Builders
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_BUILDER_DADOS_DETECTADO]
```
</unit_testing>

## Mocking and Stubbing
<mocking_stubbing>
**Mocking Framework**: [FRAMEWORK_MOCK_DETECTADO]

### Mocking Strategies
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_MOCK_DETECTADO]
```

### When to Use Mocks vs Stubs
- **Mocks**: Verify behavior and interactions
- **Stubs**: Provide controlled responses
- **Fakes**: In-memory implementations
- **Spies**: Monitor calls to real objects

### Dependency Injection in Tests
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_DI_TESTE_DETECTADO]
```

### Mock Management
- Mock lifecycle: [CICLO_VIDA_MOCK_DETECTADO]
- Mock verification: [VERIFICACAO_MOCK_DETECTADA]
- Mock reset strategies: [RESET_MOCK_DETECTADO]
- Shared mocks: [MOCKS_COMPARTILHADOS_DETECTADOS]

### External Service Mocking
- API mocking: [MOCK_API_DETECTADO]
- Database mocking: [MOCK_DATABASE_DETECTADO]
- File system mocking: [MOCK_FILESYSTEM_DETECTADO]
- Time mocking: [MOCK_TIME_DETECTADO]
</mocking_stubbing>

## Test Data Management
<test_data_management>
### Test Data Strategies
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_DADOS_TESTE_DETECTADO]
```

### Fixture Management
- Static fixtures: [FIXTURES_ESTATICAS_DETECTADAS]
- Dynamic fixtures: [FIXTURES_DINAMICAS_DETECTADAS]
- Fixture sharing: [COMPARTILHAMENTO_FIXTURES]
- Fixture cleanup: [LIMPEZA_FIXTURES_DETECTADA]

### Factory Patterns
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_FACTORY_DETECTADO]
```

### Test Database Management
- Test database setup: [SETUP_DB_TESTE_DETECTADO]
- Data seeding: [SEEDING_DADOS_DETECTADO]
- Transaction rollback: [ROLLBACK_TRANSACAO_TESTE]
- Database isolation: [ISOLAMENTO_DB_TESTE]

### Data Generation
- Random data generation: [GERACAO_DADOS_RANDOM]
- Realistic test data: [DADOS_REALISTAS_TESTE]
- Edge case data: [DADOS_EDGE_CASES]
- Large dataset testing: [TESTE_DATASETS_GRANDES]
</test_data_management>

## Integration Testing
<integration_testing>
### Integration Test Strategy
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_INTEGRACAO_DETECTADO]
```

### Component Integration
- Service integration: [INTEGRACAO_SERVICOS_DETECTADA]
- API integration: [INTEGRACAO_API_DETECTADA]
- Database integration: [INTEGRACAO_DB_DETECTADA]
- Message queue integration: [INTEGRACAO_QUEUE_DETECTADA]

### Test Environment Setup
- Test containers: [CONTAINERS_TESTE_DETECTADOS]
- Environment configuration: [CONFIG_AMBIENTE_TESTE]
- External service setup: [SETUP_SERVICOS_EXTERNOS]
- Resource management: [GERENCIAMENTO_RECURSOS_TESTE]

### Contract Testing
- API contract testing: [TESTE_CONTRATO_API]
- Schema validation: [VALIDACAO_SCHEMA_TESTE]
- Consumer-driven contracts: [CONTRATOS_CONSUMER_DRIVEN]
- Provider testing: [TESTE_PROVIDER_DETECTADO]
</integration_testing>

## End-to-End Testing
<e2e_testing>
**E2E Framework**: [FRAMEWORK_E2E_DETECTADO]

### E2E Test Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_E2E_DETECTADO]
```

### User Journey Testing
- Critical path testing: [TESTE_CAMINHO_CRITICO]
- User flow validation: [VALIDACAO_FLUXO_USUARIO]
- Cross-browser testing: [TESTE_CROSS_BROWSER]
- Mobile testing: [TESTE_MOBILE_DETECTADO]

### Page Object Pattern
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_PAGE_OBJECT_DETECTADO]
```

### Test Data for E2E
- Test user management: [GERENCIAMENTO_USUARIOS_TESTE]
- Test environment data: [DADOS_AMBIENTE_TESTE]
- Data cleanup strategies: [LIMPEZA_DADOS_E2E]
- Isolated test runs: [EXECUCAO_ISOLADA_E2E]

### Visual Testing
- Screenshot testing: [TESTE_SCREENSHOT_DETECTADO]
- Visual regression: [REGRESSAO_VISUAL_DETECTADA]
- Responsive testing: [TESTE_RESPONSIVO_DETECTADO]
- Accessibility testing: [TESTE_ACESSIBILIDADE_DETECTADO]
</e2e_testing>

## Performance Testing
<performance_testing>
### Performance Test Types
- Load testing: [TESTE_CARGA_DETECTADO]
- Stress testing: [TESTE_STRESS_DETECTADO]
- Spike testing: [TESTE_SPIKE_DETECTADO]
- Volume testing: [TESTE_VOLUME_DETECTADO]

### Performance Metrics
```[LINGUAGEM_DETECTADA]
// [METRICAS_PERFORMANCE_DETECTADAS]
```

### Benchmarking
- Baseline establishment: [BASELINE_PERFORMANCE]
- Performance regression detection: [DETECCAO_REGRESSAO_PERF]
- Continuous performance monitoring: [MONITORAMENTO_CONTINUO_PERF]
- Performance budgets: [ORCAMENTOS_PERFORMANCE]
</performance_testing>

## Test Automation
<test_automation>
### CI/CD Integration
```yaml
# [INTEGRACAO_CI_CD_TESTE_DETECTADA]
```

### Test Execution Strategies
- Parallel test execution: [EXECUCAO_PARALELA_DETECTADA]
- Test sharding: [SHARDING_TESTE_DETECTADO]
- Selective test execution: [EXECUCAO_SELETIVA_TESTE]
- Test prioritization: [PRIORIZACAO_TESTE_DETECTADA]

### Test Reporting
- Test result reporting: [RELATORIO_RESULTADO_TESTE]
- Coverage reporting: [RELATORIO_COBERTURA_DETECTADO]
- Failure analysis: [ANALISE_FALHAS_TESTE]
- Trend analysis: [ANALISE_TENDENCIAS_TESTE]

### Test Infrastructure
- Test environment management: [GERENCIAMENTO_AMBIENTE_TESTE]
- Test data pipeline: [PIPELINE_DADOS_TESTE]
- Test artifact management: [GERENCIAMENTO_ARTEFATOS_TESTE]
- Test monitoring: [MONITORAMENTO_TESTE_DETECTADO]
</test_automation>

## Test Quality and Maintenance
<test_quality>
### Test Code Quality
- Test readability: [LEGIBILIDADE_TESTE_DETECTADA]
- Test maintainability: [MANUTIBILIDADE_TESTE_DETECTADA]
- Test reliability: [CONFIABILIDADE_TESTE_DETECTADA]
- Test performance: [PERFORMANCE_TESTE_DETECTADA]

### Test Refactoring
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_REFATORACAO_TESTE_DETECTADO]
```

### Test Debt Management
- Test code reviews: [REVISAO_CODIGO_TESTE]
- Test refactoring strategies: [ESTRATEGIAS_REFATORACAO_TESTE]
- Flaky test management: [GERENCIAMENTO_TESTES_FLAKY]
- Test deprecation: [DEPRECACAO_TESTE_DETECTADA]

### Test Documentation
- Test case documentation: [DOCUMENTACAO_CASOS_TESTE]
- Test strategy documentation: [DOCUMENTACAO_ESTRATEGIA_TESTE]
- Test environment documentation: [DOCUMENTACAO_AMBIENTE_TESTE]
- Troubleshooting guides: [GUIAS_TROUBLESHOOTING_TESTE]
</test_quality>

## Security Testing
<security_testing>
### Security Test Types
- Authentication testing: [TESTE_AUTENTICACAO_DETECTADO]
- Authorization testing: [TESTE_AUTORIZACAO_DETECTADO]
- Input validation testing: [TESTE_VALIDACAO_INPUT]
- SQL injection testing: [TESTE_SQL_INJECTION]

### Security Test Patterns
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_SEGURANCA_DETECTADO]
```

### Penetration Testing
- Automated security scans: [SCANS_SEGURANCA_AUTOMATIZADOS]
- Vulnerability assessment: [AVALIACAO_VULNERABILIDADES]
- Security regression testing: [TESTE_REGRESSAO_SEGURANCA]
- Compliance testing: [TESTE_COMPLIANCE_DETECTADO]
</security_testing>

---
*Testing guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
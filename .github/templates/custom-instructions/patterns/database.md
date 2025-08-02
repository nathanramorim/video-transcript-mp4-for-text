description: MUST BE APPLIED WHEN working on database code including models, schemas, migrations, queries, and data access patterns. Covers database-specific patterns including ORM usage, query optimization, and data modeling.
applyTo: "**/models/**/*,**/entities/**/*,**/schemas/**/*,**/migrations/**/*,**/seeds/**/*,**/repositories/**/*,**/*Model.*,**/*Entity.*,**/*Schema.*,**/*Migration.*,**/*Repository.*,**/database/**/*,**/db/**/*,**/*.sql"
alwaysApply: false

# Database Development Guidelines: [NOME_DO_PROJETO]

## Database Philosophy
<database_philosophy>
**Database**: [DATABASE_DETECTADO]
**ORM/ODM**: [ORM_DETECTADO]
**Migration Tool**: [FERRAMENTA_MIGRACAO_DETECTADA]

### Core Principles
- Data integrity and consistency
- Performance and scalability
- Security and access control
- Maintainable schema evolution
- Efficient query patterns

[FILOSOFIA_DATABASE_BASEADA_PROJECTBRIEF]
</database_philosophy>

## Database Design
<schema_design>
**Schema Pattern**: [PADRAO_SCHEMA_DETECTADO]
**Naming Convention**: [CONVENCAO_NOMES_DB_DETECTADA]

### Table Design Principles
```sql
-- [EXEMPLO_TABELA_DETECTADO]
```

### Normalization Standards
- Use appropriate normalization level (typically 3NF)
- Denormalize only when performance requires it
- Document denormalization decisions
- Maintain referential integrity
- Use constraints effectively

### Relationship Modeling
- Foreign key relationships: [RELACIONAMENTOS_FK_DETECTADOS]
- Many-to-many relationships: [RELACIONAMENTOS_M2M_DETECTADOS]
- Self-referencing relationships: [RELACIONAMENTOS_SELF_REF_DETECTADOS]
- Cascade rules: [REGRAS_CASCADE_DETECTADAS]

### Data Types and Constraints
```sql
-- [TIPOS_DADOS_CONSTRAINTS_DETECTADOS]
```
</schema_design>

## Data Modeling
<data_modeling>
**Modeling Approach**: [ABORDAGEM_MODELAGEM_DETECTADA]

### Entity Definitions
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_ENTIDADE_DETECTADO]
```

### Domain-Driven Design
- Aggregate roots: [AGGREGATE_ROOTS_DETECTADOS]
- Value objects: [VALUE_OBJECTS_DETECTADOS]
- Domain entities: [DOMAIN_ENTITIES_DETECTADAS]
- Repository patterns: [PADROES_REPOSITORY_DETECTADOS]

### Data Validation Rules
- Model-level validation: [VALIDACAO_MODEL_DETECTADA]
- Database constraints: [CONSTRAINTS_DB_DETECTADAS]
- Business rule validation: [VALIDACAO_REGRAS_NEGOCIO_DB]
- Data type validation: [VALIDACAO_TIPOS_DETECTADA]

### Data Lifecycle Management
- Soft deletes: [SOFT_DELETES_DETECTADOS]
- Audit trails: [AUDIT_TRAILS_DETECTADOS]
- Data archiving: [ARQUIVAMENTO_DETECTADO]
- Data retention policies: [POLITICAS_RETENCAO_DETECTADAS]
</data_modeling>

## Query Optimization
<query_optimization>
### Indexing Strategy
```sql
-- [ESTRATEGIA_INDICES_DETECTADA]
CREATE INDEX [NOME_INDICE] ON [TABELA] ([COLUNAS]);
```

### Index Types and Usage
- Primary indexes: [INDICES_PRIMARIOS_DETECTADOS]
- Composite indexes: [INDICES_COMPOSTOS_DETECTADOS]
- Partial indexes: [INDICES_PARCIAIS_DETECTADOS]
- Covering indexes: [INDICES_COVERING_DETECTADOS]

### Query Performance Patterns
```sql
-- [EXEMPLOS_QUERIES_OTIMIZADAS_DETECTADAS]
```

### Query Analysis
- Execution plan analysis: [ANALISE_PLANO_EXECUCAO]
- Performance monitoring: [MONITORAMENTO_PERFORMANCE_DB]
- Query optimization techniques: [TECNICAS_OTIMIZACAO_QUERY]
- N+1 query prevention: [PREVENCAO_N_PLUS_1]

### Pagination Strategies
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_PAGINACAO_DETECTADO]
```
</query_optimization>

## Migration and Versioning
<schema_migration>
**Migration Framework**: [FRAMEWORK_MIGRACAO_DETECTADO]

### Migration Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_MIGRACAO_DETECTADO]
```

### Migration Best Practices
- Atomic migrations: [MIGRACOES_ATOMICAS_DETECTADAS]
- Rollback strategies: [ESTRATEGIAS_ROLLBACK_DETECTADAS]
- Data migration patterns: [PADROES_MIGRACAO_DADOS]
- Schema versioning: [VERSIONAMENTO_SCHEMA_DETECTADO]

### Environment-Specific Migrations
- Development migrations: [MIGRACOES_DEV_DETECTADAS]
- Testing migrations: [MIGRACOES_TEST_DETECTADAS]
- Production migrations: [MIGRACOES_PROD_DETECTADAS]
- Migration validation: [VALIDACAO_MIGRACOES_DETECTADA]

### Data Seeding
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_SEED_DETECTADO]
```
</schema_migration>

## ORM/ODM Patterns
<orm_patterns>
**ORM Framework**: [FRAMEWORK_ORM_DETECTADO]
**Query Builder**: [QUERY_BUILDER_DETECTADO]

### Model Definitions
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_MODEL_ORM_DETECTADO]
```

### Relationship Mappings
- One-to-one: [MAPEAMENTO_1_TO_1_DETECTADO]
- One-to-many: [MAPEAMENTO_1_TO_MANY_DETECTADO]
- Many-to-many: [MAPEAMENTO_MANY_TO_MANY_DETECTADO]
- Polymorphic relationships: [RELACIONAMENTOS_POLIMORFICOS]

### Query Patterns
```[LINGUAGEM_DETECTADA]
// [EXEMPLOS_QUERIES_ORM_DETECTADOS]
```

### Lazy vs Eager Loading
- Lazy loading strategies: [LAZY_LOADING_DETECTADO]
- Eager loading patterns: [EAGER_LOADING_DETECTADO]
- Join strategies: [ESTRATEGIAS_JOIN_DETECTADAS]
- Performance considerations: [CONSIDERACOES_PERFORMANCE_ORM]

### Transaction Management
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TRANSACAO_DETECTADO]
```
</orm_patterns>

## Database Security
<database_security>
### Access Control
- User roles and permissions: [ROLES_PERMISSOES_DB_DETECTADAS]
- Connection security: [SEGURANCA_CONEXAO_DETECTADA]
- Authentication methods: [METODOS_AUTH_DB_DETECTADOS]
- Authorization patterns: [PADROES_AUTHZ_DB_DETECTADOS]

### Data Protection
```sql
-- [EXEMPLO_PROTECAO_DADOS_DETECTADO]
```

### SQL Injection Prevention
- Parameterized queries: [QUERIES_PARAMETRIZADAS_DETECTADAS]
- Input sanitization: [SANITIZACAO_INPUT_DETECTADA]
- ORM protection: [PROTECAO_ORM_DETECTADA]
- Query validation: [VALIDACAO_QUERY_DETECTADA]

### Encryption and Masking
- Data encryption at rest: [ENCRIPTACAO_REST_DETECTADA]
- Data encryption in transit: [ENCRIPTACAO_TRANSIT_DETECTADA]
- Sensitive data masking: [MASCARAMENTO_DADOS_DETECTADO]
- Key management: [GERENCIAMENTO_CHAVES_DETECTADO]
</database_security>

## Performance Monitoring
<performance_monitoring>
### Database Metrics
- Query performance: [METRICAS_PERFORMANCE_QUERY]
- Connection pool monitoring: [MONITORAMENTO_POOL_CONEXAO]
- Resource utilization: [UTILIZACAO_RECURSOS_DB]
- Lock monitoring: [MONITORAMENTO_LOCKS]

### Monitoring Tools
```[LINGUAGEM_DETECTADA]
// [FERRAMENTAS_MONITORAMENTO_DETECTADAS]
```

### Performance Alerts
- Slow query detection: [DETECCAO_QUERY_LENTA]
- Resource exhaustion alerts: [ALERTAS_RECURSOS_ESGOTADOS]
- Deadlock detection: [DETECCAO_DEADLOCK]
- Connection limit monitoring: [MONITORAMENTO_LIMITE_CONEXAO]
</performance_monitoring>

## Testing Patterns
<testing_patterns>
### Database Testing Strategy
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_DATABASE_DETECTADO]
```

### Test Data Management
- Test fixtures: [FIXTURES_TESTE_DETECTADAS]
- Data builders: [BUILDERS_DADOS_DETECTADOS]
- Factory patterns: [PADROES_FACTORY_DETECTADOS]
- Test data cleanup: [LIMPEZA_DADOS_TESTE]

### Integration Testing
- Database integration tests: [TESTES_INTEGRACAO_DB]
- Transaction testing: [TESTES_TRANSACAO]
- Migration testing: [TESTES_MIGRACAO]
- Performance testing: [TESTES_PERFORMANCE_DB]

### Mock Strategies
- Database mocking: [MOCK_DATABASE_DETECTADO]
- Repository mocking: [MOCK_REPOSITORY_DETECTADO]
- In-memory databases: [DB_IN_MEMORY_DETECTADAS]
</testing_patterns>

## Backup and Recovery
<backup_recovery>
### Backup Strategies
- Automated backups: [BACKUPS_AUTOMATIZADOS_DETECTADOS]
- Incremental backups: [BACKUPS_INCREMENTAIS]
- Point-in-time recovery: [RECUPERACAO_POINT_IN_TIME]
- Cross-region replication: [REPLICACAO_CROSS_REGION]

### Disaster Recovery
- Recovery procedures: [PROCEDIMENTOS_RECUPERACAO]
- Data validation post-recovery: [VALIDACAO_POS_RECUPERACAO]
- Business continuity planning: [PLANEJAMENTO_CONTINUIDADE_NEGOCIO]
- Recovery testing: [TESTES_RECUPERACAO]
</backup_recovery>

## Environment Management
<environment_management>
### Database Configuration
```[LINGUAGEM_DETECTADA]
// [CONFIGURACAO_DATABASE_DETECTADA]
```

### Environment-Specific Settings
- Development configuration: [CONFIG_DEV_DB]
- Testing configuration: [CONFIG_TEST_DB]
- Production configuration: [CONFIG_PROD_DB]
- Connection pooling: [CONFIG_POOL_CONEXAO]

### Deployment Procedures
- Schema deployment: [DEPLOY_SCHEMA_DETECTADO]
- Data migration deployment: [DEPLOY_MIGRACAO_DADOS]
- Rollback procedures: [PROCEDIMENTOS_ROLLBACK_DB]
- Validation scripts: [SCRIPTS_VALIDACAO_DETECTADOS]
</environment_management>

---
*Database development guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
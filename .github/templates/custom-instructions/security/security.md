description: MUST BE APPLIED WHEN working on security-related code including authentication, authorization, data protection, and security implementations. Covers security-specific patterns including secure coding practices, vulnerability prevention, and compliance requirements.
applyTo: "**/auth/**/*,**/security/**/*,**/middleware/auth*,**/middleware/security*,**/guards/**/*,**/policies/**/*,**/validators/**/*,**/encryption/**/*,**/*Auth*,**/*Security*,**/*Guard*,**/*Policy*,**/*Validator*"
alwaysApply: false

# Security Guidelines: [NOME_DO_PROJETO]

## Security Philosophy
<security_philosophy>
**Security Framework**: [FRAMEWORK_SEGURANCA_DETECTADO]
**Authentication Method**: [METODO_AUTENTICACAO_DETECTADO]
**Authorization Strategy**: [ESTRATEGIA_AUTORIZACAO_DETECTADA]

### Security Principles
- Security by design and default
- Defense in depth strategy
- Principle of least privilege
- Fail securely and safely
- Keep security simple and usable

### Compliance Requirements
- Data protection: [PROTECAO_DADOS_DETECTADA]
- Industry standards: [PADROES_INDUSTRIA_DETECTADOS]
- Regulatory compliance: [COMPLIANCE_REGULATORIO_DETECTADO]
- Security frameworks: [FRAMEWORKS_SEGURANCA_DETECTADOS]

[FILOSOFIA_SEGURANCA_BASEADA_PROJECTBRIEF]
</security_philosophy>

## Authentication and Authorization
<auth_patterns>
### Authentication Implementation
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_AUTENTICACAO_DETECTADO]
```

### Authentication Methods
- **JWT Tokens**: [IMPLEMENTACAO_JWT_DETECTADA]
- **Session-based**: [IMPLEMENTACAO_SESSION_DETECTADA]
- **OAuth/OIDC**: [IMPLEMENTACAO_OAUTH_DETECTADA]
- **Multi-factor**: [IMPLEMENTACAO_MFA_DETECTADA]

### Token Management
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_GERENCIAMENTO_TOKEN_DETECTADO]
```

### Token Security Practices
- Token expiration: [EXPIRACAO_TOKEN_DETECTADA]
- Token refresh strategy: [ESTRATEGIA_REFRESH_TOKEN]
- Token storage: [ARMAZENAMENTO_TOKEN_DETECTADO]
- Token revocation: [REVOGACAO_TOKEN_DETECTADA]

### Authorization Patterns
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_AUTORIZACAO_DETECTADO]
```

### Role-Based Access Control (RBAC)
- Role definitions: [DEFINICOES_ROLES_DETECTADAS]
- Permission mapping: [MAPEAMENTO_PERMISSOES_DETECTADO]
- Role inheritance: [HERANCA_ROLES_DETECTADA]
- Dynamic permissions: [PERMISSOES_DINAMICAS_DETECTADAS]

### Attribute-Based Access Control (ABAC)
- Attribute definitions: [DEFINICOES_ATRIBUTOS_DETECTADAS]
- Policy engine: [ENGINE_POLITICAS_DETECTADO]
- Context evaluation: [AVALIACAO_CONTEXTO_DETECTADA]
- Rule-based decisions: [DECISOES_BASEADAS_REGRAS]
</auth_patterns>

## Data Protection
<data_protection>
### Encryption Strategies
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_ENCRIPTACAO_DETECTADO]
```

### Encryption at Rest
- Database encryption: [ENCRIPTACAO_DB_DETECTADA]
- File encryption: [ENCRIPTACAO_ARQUIVO_DETECTADA]
- Backup encryption: [ENCRIPTACAO_BACKUP_DETECTADA]
- Key management: [GERENCIAMENTO_CHAVES_DETECTADO]

### Encryption in Transit
- HTTPS/TLS: [IMPLEMENTACAO_TLS_DETECTADA]
- API encryption: [ENCRIPTACAO_API_DETECTADA]
- Message encryption: [ENCRIPTACAO_MENSAGEM_DETECTADA]
- Certificate management: [GERENCIAMENTO_CERTIFICADOS]

### Data Masking and Anonymization
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_MASCARAMENTO_DETECTADO]
```

### Sensitive Data Handling
- PII protection: [PROTECAO_PII_DETECTADA]
- Data classification: [CLASSIFICACAO_DADOS_DETECTADA]
- Data retention: [RETENCAO_DADOS_DETECTADA]
- Data disposal: [DESCARTE_DADOS_DETECTADO]

### Privacy Protection
- GDPR compliance: [COMPLIANCE_GDPR_DETECTADO]
- CCPA compliance: [COMPLIANCE_CCPA_DETECTADO]
- Consent management: [GERENCIAMENTO_CONSENTIMENTO]
- Data subject rights: [DIREITOS_TITULAR_DADOS]
</data_protection>

## Input Validation and Sanitization
<input_validation>
### Input Validation Patterns
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_VALIDACAO_INPUT_DETECTADO]
```

### Validation Strategies
- Server-side validation: [VALIDACAO_SERVER_SIDE_DETECTADA]
- Client-side validation: [VALIDACAO_CLIENT_SIDE_DETECTADA]
- Schema validation: [VALIDACAO_SCHEMA_DETECTADA]
- Type validation: [VALIDACAO_TIPO_DETECTADA]

### Sanitization Techniques
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_SANITIZACAO_DETECTADO]
```

### Common Validation Rules
- Email validation: [VALIDACAO_EMAIL_DETECTADA]
- Phone validation: [VALIDACAO_TELEFONE_DETECTADA]
- Password strength: [VALIDACAO_SENHA_DETECTADA]
- File upload validation: [VALIDACAO_UPLOAD_DETECTADA]

### Output Encoding
- HTML encoding: [CODIFICACAO_HTML_DETECTADA]
- URL encoding: [CODIFICACAO_URL_DETECTADA]
- JSON encoding: [CODIFICACAO_JSON_DETECTADA]
- SQL parameter binding: [BINDING_PARAMETROS_SQL]
</input_validation>

## Vulnerability Prevention
<vulnerability_prevention>
### SQL Injection Prevention
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_PREVENCAO_SQL_INJECTION_DETECTADO]
```

### XSS Prevention
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_PREVENCAO_XSS_DETECTADO]
```

### CSRF Protection
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_PROTECAO_CSRF_DETECTADO]
```

### Common Vulnerabilities (OWASP Top 10)
- Injection attacks: [PREVENCAO_INJECTION_DETECTADA]
- Broken authentication: [PREVENCAO_AUTH_QUEBRADA]
- Sensitive data exposure: [PREVENCAO_EXPOSICAO_DADOS]
- XML external entities: [PREVENCAO_XXE_DETECTADA]
- Security misconfigurations: [PREVENCAO_MISCONFIG_DETECTADA]

### Security Headers
```http
# [HEADERS_SEGURANCA_DETECTADOS]
Content-Security-Policy: [CSP_POLICY_DETECTADA]
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000
```

### Rate Limiting and DDoS Protection
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_RATE_LIMITING_DETECTADO]
```
</vulnerability_prevention>

## Secure Communication
<secure_communication>
### API Security
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_SEGURANCA_API_DETECTADO]
```

### API Authentication
- API key management: [GERENCIAMENTO_API_KEYS]
- Bearer token authentication: [AUTH_BEARER_TOKEN]
- Certificate-based authentication: [AUTH_CERTIFICADO]
- Mutual TLS (mTLS): [IMPLEMENTACAO_MTLS]

### API Security Best Practices
- Request signing: [ASSINATURA_REQUEST_DETECTADA]
- Timestamp validation: [VALIDACAO_TIMESTAMP_DETECTADA]
- Nonce usage: [USO_NONCE_DETECTADO]
- Rate limiting per endpoint: [RATE_LIMIT_ENDPOINT]

### Secure File Handling
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_MANIPULACAO_ARQUIVO_SEGURA]
```

### File Upload Security
- File type validation: [VALIDACAO_TIPO_ARQUIVO]
- File size limits: [LIMITES_TAMANHO_ARQUIVO]
- Virus scanning: [SCANNER_VIRUS_DETECTADO]
- Secure storage: [ARMAZENAMENTO_SEGURO_ARQUIVO]
</secure_communication>

## Security Monitoring and Logging
<security_monitoring>
### Security Event Logging
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_LOG_SEGURANCA_DETECTADO]
```

### Audit Trail Implementation
- User action logging: [LOG_ACOES_USUARIO_DETECTADO]
- System event logging: [LOG_EVENTOS_SISTEMA_DETECTADO]
- Security incident logging: [LOG_INCIDENTES_SEGURANCA]
- Access logging: [LOG_ACESSO_DETECTADO]

### Intrusion Detection
- Anomaly detection: [DETECCAO_ANOMALIA_DETECTADA]
- Failed login monitoring: [MONITOR_LOGIN_FALHADO]
- Suspicious activity detection: [DETECCAO_ATIVIDADE_SUSPEITA]
- Real-time alerting: [ALERTAS_TEMPO_REAL]

### Security Metrics
```[LINGUAGEM_DETECTADA]
// [METRICAS_SEGURANCA_DETECTADAS]
```

### SIEM Integration
- Log aggregation: [AGREGACAO_LOGS_DETECTADA]
- Event correlation: [CORRELACAO_EVENTOS_DETECTADA]
- Threat intelligence: [INTELIGENCIA_AMEACAS]
- Incident response: [RESPOSTA_INCIDENTES_DETECTADA]
</security_monitoring>

## Compliance and Governance
<compliance_governance>
### Regulatory Compliance
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_COMPLIANCE_DETECTADO]
```

### Data Protection Regulations
- GDPR requirements: [REQUISITOS_GDPR_DETECTADOS]
- CCPA requirements: [REQUISITOS_CCPA_DETECTADOS]
- HIPAA compliance: [COMPLIANCE_HIPAA_DETECTADO]
- PCI DSS compliance: [COMPLIANCE_PCI_DSS_DETECTADO]

### Security Frameworks
- ISO 27001: [FRAMEWORK_ISO27001_DETECTADO]
- NIST Cybersecurity Framework: [FRAMEWORK_NIST_DETECTADO]
- CIS Controls: [CONTROLES_CIS_DETECTADOS]
- OWASP guidelines: [DIRETRIZES_OWASP_DETECTADAS]

### Security Policies
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_POLITICA_SEGURANCA_DETECTADO]
```

### Risk Management
- Risk assessment: [AVALIACAO_RISCO_DETECTADA]
- Threat modeling: [MODELAGEM_AMEACAS_DETECTADA]
- Vulnerability management: [GERENCIAMENTO_VULNERABILIDADES]
- Security training: [TREINAMENTO_SEGURANCA_DETECTADO]
</compliance_governance>

## Incident Response
<incident_response>
### Incident Response Plan
```[LINGUAGEM_DETECTADA]
// [PLANO_RESPOSTA_INCIDENTE_DETECTADO]
```

### Incident Classification
- Security incidents: [CLASSIFICACAO_INCIDENTES_SEGURANCA]
- Data breaches: [CLASSIFICACAO_BREACH_DADOS]
- System compromises: [CLASSIFICACAO_COMPROMISSO_SISTEMA]
- Service disruptions: [CLASSIFICACAO_INTERRUPCAO_SERVICO]

### Response Procedures
- Incident detection: [DETECCAO_INCIDENTES_DETECTADA]
- Incident containment: [CONTENCAO_INCIDENTES_DETECTADA]
- Evidence preservation: [PRESERVACAO_EVIDENCIAS]
- Recovery procedures: [PROCEDIMENTOS_RECUPERACAO]

### Communication Plan
- Internal notifications: [NOTIFICACOES_INTERNAS]
- Customer communications: [COMUNICACOES_CLIENTE]
- Regulatory reporting: [RELATORIO_REGULATORIO]
- Media relations: [RELACOES_MIDIA_DETECTADAS]

### Post-Incident Activities
- Lessons learned: [LICOES_APRENDIDAS_DETECTADAS]
- Process improvements: [MELHORIAS_PROCESSO]
- Security updates: [ATUALIZACOES_SEGURANCA]
- Training updates: [ATUALIZACOES_TREINAMENTO]
</incident_response>

## Security Testing
<security_testing>
### Security Test Types
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_SEGURANCA_DETECTADO]
```

### Penetration Testing
- Automated security scans: [SCANS_AUTOMATIZADOS_DETECTADOS]
- Manual penetration testing: [PENTEST_MANUAL_DETECTADO]
- Vulnerability assessments: [AVALIACOES_VULNERABILIDADE]
- Red team exercises: [EXERCICIOS_RED_TEAM]

### Security Code Review
- Static analysis: [ANALISE_ESTATICA_SEGURANCA]
- Dynamic analysis: [ANALISE_DINAMICA_SEGURANCA]
- Interactive analysis: [ANALISE_INTERATIVA_SEGURANCA]
- Dependency scanning: [SCAN_DEPENDENCIAS_DETECTADO]

### Continuous Security Testing
- DevSecOps integration: [INTEGRACAO_DEVSECOPS]
- Security in CI/CD: [SEGURANCA_CI_CD_DETECTADA]
- Automated vulnerability scanning: [SCAN_VULN_AUTOMATIZADO]
- Security regression testing: [TESTE_REGRESSAO_SEGURANCA]
</security_testing>

---
*Security guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
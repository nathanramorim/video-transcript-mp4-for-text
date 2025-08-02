description: MUST BE APPLIED WHEN working on code review processes, pull requests, review standards, and review documentation. Covers code review-specific patterns including review checklists, feedback guidelines, and review automation.
applyTo: "**/.github/pull_request_template.md,**/.github/PULL_REQUEST_TEMPLATE.md,**/CONTRIBUTING.md,**/CODE_OF_CONDUCT.md,**/.github/ISSUE_TEMPLATE/**/*,**/review-checklist.md,**/code-review-guidelines.md"
alwaysApply: false

# Code Review Guidelines: [NOME_DO_PROJETO]

## Review Philosophy
<review_philosophy>
**Review Process**: [PROCESSO_REVIEW_DETECTADO]
**Review Tools**: [FERRAMENTAS_REVIEW_DETECTADAS]
**Team Size**: [TAMANHO_EQUIPE_DETECTADO]

### Core Principles
- Constructive and respectful feedback
- Knowledge sharing and learning focus
- Code quality and maintainability improvement
- Collaborative problem-solving approach
- Continuous improvement mindset

### Review Objectives
- **Code Quality**: Ensure high standards of code quality
- **Knowledge Transfer**: Share domain and technical knowledge
- **Risk Mitigation**: Identify potential issues early
- **Standards Compliance**: Enforce coding standards and best practices
- **Mentoring**: Support team learning and growth

[FILOSOFIA_REVIEW_BASEADA_PROJECTBRIEF]
</review_philosophy>

## Review Process
<review_workflow>
### Review Workflow
```mermaid
# [WORKFLOW_REVIEW_DETECTADO]
graph LR
    A[Create PR] --> B[Self Review]
    B --> C[Request Reviewers]
    C --> D[Code Review]
    D --> E{Approved?}
    E -->|No| F[Address Feedback]
    F --> D
    E -->|Yes| G[Merge]
```

### Review Assignment
- **Required reviewers**: [REVISORES_OBRIGATORIOS_DETECTADOS]
- **Optional reviewers**: [REVISORES_OPCIONAIS_DETECTADOS]
- **Domain experts**: [ESPECIALISTAS_DOMINIO_DETECTADOS]
- **Code owners**: [CODE_OWNERS_DETECTADOS]

### Review Timeline
- **Initial review**: [TEMPO_REVIEW_INICIAL] hours
- **Feedback response**: [TEMPO_RESPOSTA_FEEDBACK] hours
- **Re-review**: [TEMPO_RE_REVIEW] hours
- **Escalation**: [TEMPO_ESCALACAO] hours

### Review States
- **Draft**: Work in progress, feedback welcome
- **Ready for Review**: Complete and ready for formal review
- **Changes Requested**: Feedback provided, changes needed
- **Approved**: Ready to merge
- **Merged**: Successfully integrated

### Review Automation
```yaml
# [AUTOMACAO_REVIEW_DETECTADA]
```
</review_workflow>

## Pre-Review Checklist
<pre_review_checklist>
### Author Self-Review
- [ ] **Functionality**: Code works as intended
- [ ] **Testing**: All tests pass locally
- [ ] **Style**: Code follows project style guidelines
- [ ] **Documentation**: Code is properly documented
- [ ] **Performance**: No obvious performance issues
- [ ] **Security**: No security vulnerabilities introduced

### PR Preparation
```markdown
# [TEMPLATE_PR_DETECTADO]
## Description
Brief description of the changes made

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests that you ran to verify your changes

## Screenshots (if applicable)
Add screenshots to help explain your changes

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### Code Quality Checks
```[LINGUAGEM_DETECTADA]
// [VERIFICACOES_QUALIDADE_PRE_REVIEW]
```

### Automated Checks
- **Linting**: [LINTING_AUTOMATIZADO_DETECTADO]
- **Testing**: [TESTES_AUTOMATIZADOS_DETECTADOS]
- **Security**: [VERIFICACOES_SEGURANCA_DETECTADAS]
- **Performance**: [VERIFICACOES_PERFORMANCE_DETECTADAS]
</pre_review_checklist>

## Review Standards
<review_standards>
### Code Structure and Organization
```[LINGUAGEM_DETECTADA]
// [PADROES_ESTRUTURA_CODIGO_DETECTADOS]
```

### Review Focus Areas
1. **Correctness**: Does the code do what it's supposed to do?
2. **Design**: Is the code well-designed and appropriate for your system?
3. **Functionality**: Does the code behave as the author likely intended?
4. **Complexity**: Could the code be simpler?
5. **Tests**: Does the code have correct and well-designed automated tests?
6. **Naming**: Are variables, functions, classes named clearly?
7. **Comments**: Are comments clear and useful?
8. **Style**: Does the code follow style guidelines?
9. **Documentation**: Is relevant documentation updated?

### Code Readability Standards
- **Clear naming**: [PADROES_NOMENCLATURA_DETECTADOS]
- **Appropriate comments**: [PADROES_COMENTARIOS_DETECTADOS]
- **Logical structure**: [PADROES_ESTRUTURA_LOGICA]
- **Consistent formatting**: [PADROES_FORMATACAO_DETECTADOS]

### Performance Review Criteria
```[LINGUAGEM_DETECTADA]
// [CRITERIOS_PERFORMANCE_REVIEW_DETECTADOS]
```

### Security Review Criteria
- **Input validation**: [VALIDACAO_INPUT_REVIEW]
- **Authentication/Authorization**: [AUTH_REVIEW_DETECTADO]
- **Data protection**: [PROTECAO_DADOS_REVIEW]
- **Secure communication**: [COMUNICACAO_SEGURA_REVIEW]

### Architecture Review
- **Design patterns**: [PADROES_DESIGN_REVIEW]
- **Separation of concerns**: [SEPARACAO_CONCERNS_REVIEW]
- **Dependency management**: [GERENCIAMENTO_DEPS_REVIEW]
- **Scalability considerations**: [ESCALABILIDADE_REVIEW]
</review_standards>

## Feedback Guidelines
<feedback_guidelines>
### Constructive Feedback Principles
```markdown
# [PRINCIPIOS_FEEDBACK_DETECTADOS]
```

### Feedback Categories
- **Must Fix**: Critical issues that must be addressed
- **Should Fix**: Important improvements that should be made
- **Consider**: Suggestions for improvement
- **Nit**: Minor style or preference issues
- **Question**: Clarification needed
- **Praise**: Positive feedback on good practices

### Feedback Format
```markdown
# [FORMATO_FEEDBACK_DETECTADO]
**Category**: [Must Fix/Should Fix/Consider/Nit/Question/Praise]
**Location**: [File:Line] or [General]
**Issue**: Brief description of the issue
**Suggestion**: Specific recommendation for improvement
**Rationale**: Why this change would be beneficial
```

### Example Feedback
```markdown
**Category**: Must Fix
**Location**: `src/auth/login.js:45`
**Issue**: Password is being logged in plain text
**Suggestion**: Remove the password from the log statement
**Rationale**: This creates a security vulnerability by exposing sensitive data

**Category**: Consider
**Location**: `src/utils/helpers.js:12-20`
**Issue**: This function is quite complex
**Suggestion**: Consider breaking this into smaller, more focused functions
**Rationale**: Would improve readability and testability
```

### Communication Best Practices
- **Be specific**: Point to exact lines and provide clear examples
- **Be constructive**: Focus on the code, not the person
- **Be educational**: Explain the reasoning behind suggestions
- **Be positive**: Acknowledge good practices and improvements
- **Be timely**: Provide feedback promptly
</feedback_guidelines>

## Review Types
<review_types>
### Feature Reviews
```[LINGUAGEM_DETECTADA]
// [REVIEW_FEATURES_DETECTADO]
```

### Feature Review Checklist
- [ ] **Requirements**: Does the implementation meet the requirements?
- [ ] **User Experience**: Is the user experience intuitive and smooth?
- [ ] **Edge Cases**: Are edge cases handled appropriately?
- [ ] **Error Handling**: Are errors handled gracefully?
- [ ] **Performance**: Does the feature perform well under expected load?
- [ ] **Accessibility**: Is the feature accessible to all users?

### Bug Fix Reviews
```[LINGUAGEM_DETECTADA]
// [REVIEW_BUGFIX_DETECTADO]
```

### Bug Fix Review Checklist
- [ ] **Root Cause**: Is the root cause identified and addressed?
- [ ] **Fix Scope**: Does the fix address only the specific issue?
- [ ] **Side Effects**: Are there any unintended side effects?
- [ ] **Testing**: Is there a test to prevent regression?
- [ ] **Documentation**: Is any affected documentation updated?

### Refactoring Reviews
```[LINGUAGEM_DETECTADA]
// [REVIEW_REFACTORING_DETECTADO]
```

### Refactoring Review Checklist
- [ ] **Behavior Preservation**: Does the refactored code maintain the same behavior?
- [ ] **Improvement**: Is the code actually improved (readability, performance, maintainability)?
- [ ] **Test Coverage**: Are all existing tests still passing?
- [ ] **Breaking Changes**: Are there any breaking changes introduced?
- [ ] **Documentation**: Is documentation updated to reflect changes?

### Security Reviews
```[LINGUAGEM_DETECTADA]
// [REVIEW_SECURITY_DETECTADO]
```

### Security Review Checklist
- [ ] **Input Validation**: All inputs are properly validated
- [ ] **Output Encoding**: All outputs are properly encoded
- [ ] **Authentication**: Authentication is properly implemented
- [ ] **Authorization**: Authorization checks are in place
- [ ] **Data Protection**: Sensitive data is properly protected
- [ ] **Error Handling**: Errors don't leak sensitive information
</review_types>

## Advanced Review Techniques
<advanced_review>
### Code Review Tools
```[LINGUAGEM_DETECTADA]
// [FERRAMENTAS_REVIEW_AVANCADAS_DETECTADAS]
```

### Static Analysis Integration
- **Linting results**: [RESULTADOS_LINTING_REVIEW]
- **Security scanning**: [SCANNING_SEGURANCA_REVIEW]
- **Dependency analysis**: [ANALISE_DEPS_REVIEW]
- **Code complexity**: [COMPLEXIDADE_CODIGO_REVIEW]

### Automated Review Checks
```yaml
# [CHECKS_AUTOMATIZADOS_REVIEW_DETECTADOS]
```

### Review Metrics
- **Review coverage**: [COBERTURA_REVIEW_DETECTADA]%
- **Average review time**: [TEMPO_MEDIO_REVIEW]
- **Defect detection rate**: [TAXA_DETECCAO_DEFEITOS]%
- **Review participation**: [PARTICIPACAO_REVIEW_DETECTADA]%

### Large Change Reviews
```[LINGUAGEM_DETECTADA]
// [REVIEW_MUDANCAS_GRANDES_DETECTADO]
```

### Review Strategies for Large Changes
- **Incremental review**: Review changes in smaller chunks
- **Architecture review**: Focus on high-level design first
- **Pair review**: Conduct review sessions with multiple reviewers
- **Split reviews**: Divide review among domain experts
</advanced_review>

## Review Documentation
<review_documentation>
### Review Decision Records
```markdown
# [TEMPLATE_DECISAO_REVIEW_DETECTADO]
## Review Decision: [TITLE]
**Date**: [DATE]
**Reviewers**: [REVIEWER_LIST]
**Author**: [AUTHOR]

### Summary
Brief summary of the change and review decision

### Key Discussion Points
- [POINT_1]
- [POINT_2]
- [POINT_3]

### Decision
[APPROVED/REJECTED/CONDITIONAL]

### Action Items
- [ ] [ACTION_1]
- [ ] [ACTION_2]

### Lessons Learned
- [LESSON_1]
- [LESSON_2]
```

### Review Analytics
```[LINGUAGEM_DETECTADA]
// [ANALYTICS_REVIEW_DETECTADAS]
```

### Knowledge Sharing
- **Review summaries**: [RESUMOS_REVIEW_DETECTADOS]
- **Best practices**: [MELHORES_PRATICAS_REVIEW]
- **Common issues**: [PROBLEMAS_COMUNS_REVIEW]
- **Learning resources**: [RECURSOS_APRENDIZADO_REVIEW]

### Review Process Improvement
- **Retrospectives**: [RETROSPECTIVAS_REVIEW_DETECTADAS]
- **Process metrics**: [METRICAS_PROCESSO_REVIEW]
- **Feedback collection**: [COLETA_FEEDBACK_REVIEW]
- **Continuous improvement**: [MELHORIA_CONTINUA_REVIEW]
</review_documentation>

## Conflict Resolution
<conflict_resolution>
### Disagreement Handling
```[LINGUAGEM_DETECTADA]
// [RESOLUCAO_CONFLITOS_REVIEW_DETECTADA]
```

### Escalation Process
1. **Direct discussion**: Author and reviewer discuss the issue
2. **Team discussion**: Bring the issue to the team for input
3. **Tech lead decision**: Tech lead makes the final decision
4. **Architecture review**: For architectural disagreements

### Common Conflicts
- **Style preferences**: [CONFLITOS_ESTILO_DETECTADOS]
- **Architecture decisions**: [CONFLITOS_ARQUITETURA_DETECTADOS]
- **Performance trade-offs**: [CONFLITOS_PERFORMANCE_DETECTADOS]
- **Security concerns**: [CONFLITOS_SEGURANCA_DETECTADOS]

### Resolution Guidelines
- **Focus on facts**: Base decisions on measurable criteria
- **Consider context**: Take project constraints into account
- **Document decisions**: Record the rationale for future reference
- **Learn together**: Use conflicts as learning opportunities
</conflict_resolution>

---
*Code review guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
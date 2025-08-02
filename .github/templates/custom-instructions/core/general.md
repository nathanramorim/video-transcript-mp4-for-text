description: MUST BE APPLIED WHEN working on any code within [NOME_DO_PROJETO]. Covers general development patterns including naming conventions, project structure, code organization, and project-specific standards.
applyTo: "**/*"
alwaysApply: false

# General Development Guidelines: [NOME_DO_PROJETO]

## Project Context
**Project**: [NOME_DO_PROJETO]
**Primary Language**: [LINGUAGEM_DETECTADA]
**Main Framework**: [FRAMEWORK_PRINCIPAL]
**Architecture**: [ARQUITETURA_IDENTIFICADA]

[CONTEXTO_GERAL_BASEADO_PROJECTBRIEF]

## Development Philosophy
[FILOSOFIA_BASEADA_SYSTEMPATTERNS_E_PROJECTBRIEF]

## Naming Conventions
**Detected from existing codebase:**
- **Classes**: [PADROES_CLASSES_DETECTADOS]
- **Methods/Functions**: [PADROES_METODOS_DETECTADOS]
- **Variables**: [PADROES_VARIAVEIS_DETECTADOS]
- **Files**: [PADROES_ARQUIVOS_DETECTADOS]
- **Constants**: [PADROES_CONSTANTES_DETECTADOS]

## Project Structure
[ESTRUTURA_DIRETORIO_ANALISADA]

## Code Organization Patterns
<code_organization>
[PADROES_ARQUITETURAIS_IDENTIFICADOS]

### File Organization
- Follow established directory structure patterns
- Group related functionality together
- Maintain clear separation of concerns
- Use consistent file naming conventions

### Import/Dependency Management
- Order imports alphabetically within groups
- Group external dependencies before internal ones
- Use relative imports for local modules
- Avoid circular dependencies
</code_organization>

## Technology Stack
- **Main Stack**: [STACK_DETECTADO]
- **Key Dependencies**: [DEPENDENCIAS_PRINCIPAIS]
- **Build Tools**: [FERRAMENTAS_BUILD]
- **Testing Framework**: [FRAMEWORK_TESTES]

## Code Examples - Well Structured
[EXEMPLOS_REAIS_EXTRAIDOS_CODEBASE]

## Antipatterns to Avoid
[ANTIPADROES_ESPECIFICOS_PROJETO]

### Common Antipatterns
- Avoid deep nesting (max 3-4 levels)
- Don't use unclear or abbreviated variable names
- Avoid large functions (keep under 50 lines when possible)
- Don't mix business logic with presentation logic
- Avoid hardcoded values - use configuration

## Quality Guidelines
- **Test Coverage**: [COBERTURA_ESPERADA]%
- **Documentation**: [PADRAO_DOCUMENTACAO]
- **Performance**: [CRITERIOS_PERFORMANCE]
- **Security**: [REQUISITOS_SEGURANCA_BASICOS]

## Error Handling
- Use consistent error handling patterns
- Provide meaningful error messages
- Log errors appropriately for debugging
- Handle edge cases gracefully
- Validate inputs at boundaries

## Performance Considerations
- Optimize for readability first, performance second
- Profile before optimizing
- Use appropriate data structures
- Minimize memory allocations in hot paths
- Cache expensive computations when appropriate

---
*General development guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
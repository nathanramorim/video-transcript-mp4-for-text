description: MUST BE APPLIED WHEN working on backend code including APIs, services, controllers, and server-side logic. Covers backend-specific patterns including API design, service layer, data access, and middleware.
applyTo: "**/controllers/**/*,**/services/**/*,**/repositories/**/*,**/middleware/**/*,**/api/**/*,**/routes/**/*,**/handlers/**/*,**/*Controller.*,**/*Service.*,**/*Repository.*,**/*Handler.*,**/views.py,**/urls.py,**/serializers.py"
alwaysApply: false

# Backend Development Guidelines: [NOME_DO_PROJETO]

## Backend Architecture
<backend_architecture>
**Architecture Pattern**: [ARQUITETURA_BACKEND_DETECTADA]
**Framework**: [FRAMEWORK_BACKEND_DETECTADO]

### Layered Architecture
- **Presentation Layer**: [CAMADA_APRESENTACAO_DETECTADA]
- **Business Logic Layer**: [CAMADA_NEGOCIO_DETECTADA]
- **Data Access Layer**: [CAMADA_DADOS_DETECTADA]
- **Infrastructure Layer**: [CAMADA_INFRAESTRUTURA_DETECTADA]

### Component Interaction Patterns
[PADROES_INTERACAO_COMPONENTES_DETECTADOS]
</backend_architecture>

## API Design and Standards
<api_design>
**API Style**: [ESTILO_API_DETECTADO] (REST/GraphQL/gRPC)
**Base URL Pattern**: [PADRAO_URL_BASE_DETECTADO]

### RESTful API Conventions
```http
# [EXEMPLOS_ENDPOINTS_DETECTADOS]
GET    /api/v1/[RECURSO]           # List resources
POST   /api/v1/[RECURSO]           # Create resource
GET    /api/v1/[RECURSO]/{id}      # Get specific resource
PUT    /api/v1/[RECURSO]/{id}      # Update resource
DELETE /api/v1/[RECURSO]/{id}      # Delete resource
```

### HTTP Method Usage
- **GET**: Read operations, no side effects
- **POST**: Create new resources
- **PUT**: Update entire resource
- **PATCH**: Partial updates
- **DELETE**: Remove resources

### Status Code Standards
- **200**: Success with body
- **201**: Created successfully
- **204**: Success without body
- **400**: Bad request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not found
- **500**: Internal server error

### Request/Response Formats
```json
// [FORMATO_REQUEST_RESPONSE_DETECTADO]
```

### API Versioning
- Strategy: [ESTRATEGIA_VERSIONAMENTO_DETECTADA]
- Header: `Accept: application/vnd.api+json;version=1`
- URL: `/api/v1/endpoint`
</api_design>

## Service Layer Patterns
<service_layer>
**Service Pattern**: [PADRAO_SERVICE_DETECTADO]

### Service Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_SERVICE_DETECTADO]
```

### Service Responsibilities
- Business logic implementation
- Orchestration between different components
- Transaction management
- Business rule validation
- External service integration

### Service Communication
- Inter-service communication: [COMUNICACAO_SERVICOS_DETECTADA]
- Event handling: [MANIPULACAO_EVENTOS_DETECTADA]
- Message queues: [FILAS_MENSAGEM_DETECTADAS]
</service_layer>

## Data Access Layer
<data_access_layer>
**ORM/ODM**: [ORM_DETECTADO]
**Database**: [DATABASE_DETECTADO]

### Repository Pattern
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_REPOSITORY_DETECTADO]
```

### Database Connection Management
- Connection pooling: [POOL_CONEXAO_DETECTADO]
- Transaction handling: [MANIPULACAO_TRANSACAO_DETECTADA]
- Connection string pattern: [PADRAO_CONNECTION_STRING]

### Query Optimization
- Use indexes effectively
- Avoid N+1 queries
- Implement pagination
- Use appropriate fetch strategies
- Monitor query performance

### Data Validation
- Input validation at controller level
- Business rule validation at service level
- Database constraint validation
- Type validation and sanitization
</data_access_layer>

## Error Handling and Validation
<error_handling>
### Exception Handling Strategy
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_ERROR_HANDLING_DETECTADO]
```

### Global Error Handling
- Centralized error handling middleware
- Consistent error response format
- Error logging and monitoring
- User-friendly error messages
- Security-aware error responses

### Input Validation
- Request validation: [VALIDACAO_REQUEST_DETECTADA]
- Schema validation: [VALIDACAO_SCHEMA_DETECTADA]
- Business rule validation: [VALIDACAO_REGRAS_NEGOCIO]

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```
</error_handling>

## Authentication and Authorization
<auth_patterns>
**Authentication Method**: [METODO_AUTENTICACAO_DETECTADO]
**Authorization Strategy**: [ESTRATEGIA_AUTORIZACAO_DETECTADA]

### Authentication Patterns
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_AUTENTICACAO_DETECTADO]
```

### JWT Token Handling
- Token generation and validation
- Refresh token strategy
- Token expiration handling
- Secure token storage

### Role-Based Access Control (RBAC)
- Role definition: [DEFINICAO_ROLES_DETECTADAS]
- Permission mapping: [MAPEAMENTO_PERMISSOES_DETECTADO]
- Access control middleware: [MIDDLEWARE_CONTROLE_ACESSO]
</auth_patterns>

## Middleware and Interceptors
<middleware_patterns>
**Middleware Stack**: [STACK_MIDDLEWARE_DETECTADO]

### Common Middleware
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_MIDDLEWARE_DETECTADO]
```

### Middleware Order
1. Security headers
2. CORS handling
3. Request logging
4. Authentication
5. Authorization
6. Rate limiting
7. Request validation
8. Business logic
9. Error handling
10. Response formatting
</middleware_patterns>

## Testing Patterns
<testing_patterns>
### Unit Testing
- Test service layer logic
- Mock external dependencies
- Test validation logic
- Cover edge cases

### Integration Testing
- Test API endpoints
- Test database operations
- Test external service integration
- Test middleware functionality

### Test Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_BACKEND_DETECTADO]
```
</testing_patterns>

## Performance Considerations
<performance>
### Caching Strategies
- Application-level caching: [CACHE_APP_DETECTADO]
- Database query caching: [CACHE_DB_DETECTADO]
- HTTP response caching: [CACHE_HTTP_DETECTADO]

### Async Processing
- Background jobs: [JOBS_BACKGROUND_DETECTADOS]
- Message queues: [FILAS_MENSAGEM_DETECTADAS]
- Event-driven architecture: [ARQUITETURA_EVENTOS_DETECTADA]

### Database Optimization
- Proper indexing strategy
- Query optimization
- Connection pooling
- Read replicas for scaling
</performance>

## Monitoring and Logging
<monitoring>
### Logging Strategy
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_LOGGING_DETECTADO]
```

### Metrics Collection
- Request/response metrics
- Database performance metrics
- Error rates and types
- Business metrics

### Health Checks
- Application health endpoints
- Database connectivity checks
- External service health
- Resource utilization monitoring
</monitoring>

---
*Backend development guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
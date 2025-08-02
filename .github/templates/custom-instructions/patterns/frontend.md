description: MUST BE APPLIED WHEN working on frontend code including components, views, UI logic, and client-side functionality. Covers frontend-specific patterns including component architecture, state management, styling, and user interactions.
applyTo: "**/components/**/*,**/pages/**/*,**/views/**/*,**/screens/**/*,**/hooks/**/*,**/store/**/*,**/styles/**/*,**/assets/**/*,**/*.component.*,**/*.vue,**/*.jsx,**/*.tsx,**/*.svelte,**/public/**/*,**/static/**/*"
alwaysApply: false

# Frontend Development Guidelines: [NOME_DO_PROJETO]

## Frontend Philosophy
<frontend_philosophy>
**Framework**: [FRAMEWORK_FRONTEND_DETECTADO]
**Architecture Pattern**: [ARQUITETURA_FRONTEND_DETECTADA]
**Build Tool**: [FERRAMENTA_BUILD_DETECTADA]

### Core Principles
- User experience first approach
- Performance and accessibility standards
- Component-based development
- Responsive and mobile-first design
- Maintainable and testable code

[FILOSOFIA_FRONTEND_BASEADA_PROJECTBRIEF]
</frontend_philosophy>

## UI/UX Standards
<design_system>
**Design System**: [DESIGN_SYSTEM_DETECTADO]
**CSS Framework**: [FRAMEWORK_CSS_DETECTADO]

### Color Scheme and Branding
```css
/* [ESQUEMA_CORES_DETECTADO] */
:root {
  --primary-color: [COR_PRIMARIA];
  --secondary-color: [COR_SECUNDARIA];
  --accent-color: [COR_DESTAQUE];
  --text-color: [COR_TEXTO];
  --background-color: [COR_FUNDO];
}
```

### Typography Standards
- Primary font: [FONTE_PRIMARIA_DETECTADA]
- Secondary font: [FONTE_SECUNDARIA_DETECTADA]
- Font scales: [ESCALA_FONTES_DETECTADA]
- Line height standards: [ALTURA_LINHA_PADRAO]

### Spacing and Layout
```css
/* [SISTEMA_ESPACAMENTO_DETECTADO] */
--spacing-xs: [ESPACAMENTO_XS];
--spacing-sm: [ESPACAMENTO_SM];
--spacing-md: [ESPACAMENTO_MD];
--spacing-lg: [ESPACAMENTO_LG];
--spacing-xl: [ESPACAMENTO_XL];
```

### Component Design Patterns
- Atomic design principles
- Consistent component API
- Reusable design tokens
- Accessibility-first approach
</design_system>

## Component Architecture
<component_organization>
**Component Pattern**: [PADRAO_COMPONENTE_DETECTADO]
**State Management**: [GERENCIAMENTO_ESTADO_DETECTADO]

### Component Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_COMPONENTE_DETECTADO]
```

### Component Hierarchy
```
[HIERARQUIA_COMPONENTES_DETECTADA]
```

### Naming Conventions
- Components: [CONVENCAO_NOMES_COMPONENTES]
- Props: [CONVENCAO_NOMES_PROPS]
- Events: [CONVENCAO_NOMES_EVENTOS]
- CSS classes: [CONVENCAO_NOMES_CSS]

### Component Types
- **Atoms**: Basic UI elements (buttons, inputs, labels)
- **Molecules**: Simple combinations of atoms
- **Organisms**: Complex components with business logic
- **Templates**: Page-level layouts
- **Pages**: Specific instances of templates

### Reusability Patterns
- Generic base components
- Composition over inheritance
- Render props/slots pattern
- Higher-order components
- Custom hooks pattern
</component_organization>

## State Management
<state_management>
**State Solution**: [SOLUCAO_ESTADO_DETECTADA]
**Pattern**: [PADRAO_ESTADO_DETECTADO]

### State Architecture
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_ESTADO_DETECTADO]
```

### State Organization
- Local component state: [ESTADO_LOCAL_DETECTADO]
- Global application state: [ESTADO_GLOBAL_DETECTADO]
- Server state management: [ESTADO_SERVIDOR_DETECTADO]
- URL state synchronization: [SINC_ESTADO_URL_DETECTADA]

### Data Flow Patterns
- Unidirectional data flow
- Event-driven updates
- Immutable state updates
- State normalization
- Optimistic updates

### State Persistence
- Local storage strategy: [ESTRATEGIA_LOCAL_STORAGE]
- Session storage usage: [USO_SESSION_STORAGE]
- State hydration: [HIDRATACAO_ESTADO]
</state_management>

## Responsive Design
<responsive_design>
**Breakpoints**: [BREAKPOINTS_DETECTADOS]
**Grid System**: [SISTEMA_GRID_DETECTADO]

### Breakpoint Definitions
```css
/* [DEFINICOES_BREAKPOINTS_DETECTADAS] */
@media (max-width: [MOBILE_BREAKPOINT]) { /* Mobile styles */ }
@media (min-width: [TABLET_BREAKPOINT]) { /* Tablet styles */ }
@media (min-width: [DESKTOP_BREAKPOINT]) { /* Desktop styles */ }
```

### Mobile-First Approach
- Design for mobile first
- Progressive enhancement
- Touch-friendly interfaces
- Performance considerations
- Offline capabilities

### Layout Strategies
- Flexible grid systems
- CSS Grid and Flexbox
- Responsive typography
- Adaptive images
- Container queries (when supported)
</responsive_design>

## Styling and CSS
<styling_approach>
**CSS Strategy**: [ESTRATEGIA_CSS_DETECTADA]
**Methodology**: [METODOLOGIA_CSS_DETECTADA]

### CSS Architecture
```css
/* [ARQUITETURA_CSS_DETECTADA] */
```

### Styling Patterns
- Component-scoped styles: [ESTILOS_ESCOPO_COMPONENTE]
- Global styles: [ESTILOS_GLOBAIS_DETECTADOS]
- Theme management: [GERENCIAMENTO_TEMA_DETECTADO]
- CSS-in-JS approach: [ABORDAGEM_CSS_IN_JS]

### CSS Naming Conventions
- BEM methodology: [USO_BEM_DETECTADO]
- Utility classes: [CLASSES_UTILITY_DETECTADAS]
- Component prefixes: [PREFIXOS_COMPONENTE_DETECTADOS]

### Animation and Transitions
```css
/* [ANIMACOES_TRANSICOES_DETECTADAS] */
```
</styling_approach>

## Performance Optimization
<performance_optimization>
### Bundle Optimization
- Code splitting: [CODE_SPLITTING_DETECTADO]
- Tree shaking: [TREE_SHAKING_DETECTADO]
- Lazy loading: [LAZY_LOADING_DETECTADO]
- Asset optimization: [OTIMIZACAO_ASSETS_DETECTADA]

### Runtime Performance
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_OTIMIZACAO_PERFORMANCE_DETECTADO]
```

### Image Optimization
- Responsive images: [IMAGENS_RESPONSIVAS_DETECTADAS]
- Image formats: [FORMATOS_IMAGEM_DETECTADOS]
- Lazy loading images: [LAZY_LOADING_IMAGENS]

### Caching Strategies
- Service worker: [SERVICE_WORKER_DETECTADO]
- Browser caching: [CACHE_BROWSER_DETECTADO]
- Application cache: [CACHE_APP_DETECTADO]
</performance_optimization>

## Form Handling
<form_handling>
**Form Library**: [BIBLIOTECA_FORMS_DETECTADA]
**Validation Strategy**: [ESTRATEGIA_VALIDACAO_DETECTADA]

### Form Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_FORM_DETECTADO]
```

### Validation Patterns
- Client-side validation: [VALIDACAO_CLIENT_SIDE]
- Real-time validation: [VALIDACAO_REAL_TIME]
- Server-side validation integration: [INTEGRACAO_VALIDACAO_SERVER]
- Error message display: [EXIBICAO_ERROS_DETECTADA]

### Form State Management
- Form data handling: [MANIPULACAO_DADOS_FORM]
- Dirty state tracking: [RASTREAMENTO_ESTADO_DIRTY]
- Form submission handling: [MANIPULACAO_SUBMISSAO_FORM]
</form_handling>

## Routing and Navigation
<routing_navigation>
**Router**: [ROTEADOR_DETECTADO]
**Navigation Pattern**: [PADRAO_NAVEGACAO_DETECTADO]

### Route Structure
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_ROTAS_DETECTADO]
```

### Navigation Patterns
- Declarative routing: [ROTEAMENTO_DECLARATIVO]
- Programmatic navigation: [NAVEGACAO_PROGRAMATICA]
- Route guards: [GUARDAS_ROTA_DETECTADAS]
- Nested routing: [ROTEAMENTO_ANINHADO]

### URL Management
- Query parameters: [PARAMETROS_QUERY_DETECTADOS]
- Route parameters: [PARAMETROS_ROTA_DETECTADOS]
- Hash routing: [HASH_ROUTING_DETECTADO]
- History management: [GERENCIAMENTO_HISTORY]
</routing_navigation>

## API Integration
<api_integration>
**HTTP Client**: [CLIENTE_HTTP_DETECTADO]
**Data Fetching Pattern**: [PADRAO_FETCH_DADOS_DETECTADO]

### API Communication
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_API_INTEGRATION_DETECTADO]
```

### Error Handling
- Network error handling: [MANIPULACAO_ERROS_REDE]
- API error responses: [RESPOSTAS_ERRO_API]
- Retry strategies: [ESTRATEGIAS_RETRY]
- Loading states: [ESTADOS_LOADING]

### Caching and Optimization
- Request caching: [CACHE_REQUESTS_DETECTADO]
- Background refetching: [REFETCH_BACKGROUND]
- Optimistic updates: [UPDATES_OTIMISTAS]
</api_integration>

## Testing Strategies
<testing_strategies>
**Testing Framework**: [FRAMEWORK_TESTE_DETECTADO]
**Testing Utilities**: [UTILITARIOS_TESTE_DETECTADOS]

### Component Testing
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_TESTE_COMPONENTE_DETECTADO]
```

### Testing Patterns
- Unit testing: [TESTE_UNITARIO_FRONTEND]
- Integration testing: [TESTE_INTEGRACAO_FRONTEND]
- E2E testing: [TESTE_E2E_DETECTADO]
- Visual regression testing: [TESTE_REGRESSAO_VISUAL]

### Mock Strategies
- API mocking: [MOCK_API_DETECTADO]
- Component mocking: [MOCK_COMPONENTE_DETECTADO]
- Service mocking: [MOCK_SERVICE_DETECTADO]
</testing_strategies>

## Accessibility (A11y)
<accessibility>
### WCAG Compliance
- Level: [NIVEL_WCAG_DETECTADO]
- Color contrast requirements
- Keyboard navigation support
- Screen reader compatibility
- Focus management

### Implementation Patterns
```[LINGUAGEM_DETECTADA]
// [EXEMPLO_ACESSIBILIDADE_DETECTADO]
```

### Testing Tools
- Automated a11y testing: [TESTE_A11Y_AUTOMATIZADO]
- Manual testing procedures: [PROCEDIMENTOS_TESTE_MANUAL]
- Screen reader testing: [TESTE_SCREEN_READER]
</accessibility>

---
*Frontend development guidelines for [NOME_DO_PROJETO] using GitHub Copilot* 
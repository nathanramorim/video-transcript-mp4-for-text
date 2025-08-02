# Template: systemPatterns.md

Este é o template para o arquivo `systemPatterns.md` do banco de memória do RIPER-Copilot.

```markdown
# Padrões do Sistema: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Visão Geral da Arquitetura
[Descrição de alto nível da arquitetura do sistema, incluindo principais camadas e como se comunicam]

## Padrão Arquitetural Principal
**Padrão escolhido**: [NOME_DO_PADRÃO] (ex: MVC, Microservices, Layered, etc.)

**Justificativa**:
[Por que este padrão foi escolhido para este projeto específico]

**Implementação**:
[Como o padrão é implementado no contexto deste projeto]

## Componentes Principais

### [COMPONENTE_1]: [NOME_COMPONENTE]
- **Responsabilidade**: [O que este componente faz]
- **Localização**: [Onde está no projeto (pasta/arquivo)]
- **Dependências**: [Do que depende]
- **Dependentes**: [Quem depende dele]
- **Padrões aplicados**: [Padrões específicos usados neste componente]

### [COMPONENTE_2]: [NOME_COMPONENTE]
- **Responsabilidade**: [O que este componente faz]
- **Localização**: [Onde está no projeto (pasta/arquivo)]
- **Dependências**: [Do que depende]
- **Dependentes**: [Quem depende dele]
- **Padrões aplicados**: [Padrões específicos usados neste componente]

### [COMPONENTE_3]: [NOME_COMPONENTE]
- **Responsabilidade**: [O que este componente faz]
- **Localização**: [Onde está no projeto (pasta/arquivo)]
- **Dependências**: [Do que depende]
- **Dependentes**: [Quem depende dele]
- **Padrões aplicados**: [Padrões específicos usados neste componente]

## Padrões de Design em Uso

### [PADRÃO_1]: [NOME_PADRÃO]
- **Contexto de uso**: [Onde e quando é usado]
- **Implementação**: [Como é implementado]
- **Benefícios**: [Por que foi escolhido]
- **Trade-offs**: [Que complexidade introduz]

### [PADRÃO_2]: [NOME_PADRÃO]
- **Contexto de uso**: [Onde e quando é usado]
- **Implementação**: [Como é implementado]
- **Benefícios**: [Por que foi escolhido]
- **Trade-offs**: [Que complexidade introduz]

### [PADRÃO_3]: [NOME_PADRÃO]
- **Contexto de uso**: [Onde e quando é usado]
- **Implementação**: [Como é implementado]
- **Benefícios**: [Por que foi escolhido]
- **Trade-offs**: [Que complexidade introduz]

## Fluxo de Dados

### Fluxo Principal
```
[Usuário/Cliente] 
    ↓ [Tipo de request]
[Componente de Entrada] 
    ↓ [Formato de dados]
[Componente de Processamento] 
    ↓ [Dados processados]
[Componente de Persistência] 
    ↓ [Confirmação/Dados]
[Componente de Resposta]
    ↓ [Response format]
[Usuário/Cliente]
```

### Fluxos Secundários
1. **[NOME_FLUXO_1]**: [Descrição do fluxo]
   ```
   [Ponto de entrada] → [Passo 1] → [Passo 2] → [Resultado]
   ```

2. **[NOME_FLUXO_2]**: [Descrição do fluxo]
   ```
   [Ponto de entrada] → [Passo 1] → [Passo 2] → [Resultado]
   ```

## Decisões Técnicas Chave

### [DECISÃO_1]: [TÍTULO_DECISÃO]
- **Contexto**: [Situação que levou à decisão]
- **Opções consideradas**: [Alternativas avaliadas]
- **Decisão tomada**: [O que foi decidido]
- **Justificativa**: [Por que esta opção foi escolhida]
- **Consequências**: [Impactos positivos e negativos]
- **Data da decisão**: [DATA]
- **Responsável**: [QUEM_DECIDIU]

### [DECISÃO_2]: [TÍTULO_DECISÃO]
- **Contexto**: [Situação que levou à decisão]
- **Opções consideradas**: [Alternativas avaliadas]
- **Decisão tomada**: [O que foi decidido]
- **Justificativa**: [Por que esta opção foi escolhida]
- **Consequências**: [Impactos positivos e negativos]
- **Data da decisão**: [DATA]
- **Responsável**: [QUEM_DECIDIU]

## Relacionamentos entre Componentes

### Mapa de Dependências
```
[COMPONENTE_A] ──depends on──> [COMPONENTE_B]
[COMPONENTE_A] ──implements──> [INTERFACE_X]
[COMPONENTE_C] ──uses──> [COMPONENTE_A]
[COMPONENTE_D] ──extends──> [COMPONENTE_BASE]
```

### Protocolo de Comunicação
- **Interna**: [Como componentes internos se comunicam]
- **Externa**: [Como sistema se comunica com externos]
- **Formato de dados**: [Formatos padrão usados]
- **Tratamento de erros**: [Como erros são propagados]

## Convenções e Padrões de Código

### Estrutura de Arquivos
```
projeto/
├── src/
│   ├── [CAMADA_1]/          # [Descrição da camada]
│   ├── [CAMADA_2]/          # [Descrição da camada]
│   ├── shared/              # Componentes compartilhados
│   └── utils/               # Utilitários
├── tests/
├── docs/
└── config/
```

### Nomenclatura
- **Arquivos**: [Convenção para nomes de arquivo]
- **Classes**: [Convenção para nomes de classe]
- **Funções**: [Convenção para nomes de função]
- **Variáveis**: [Convenção para nomes de variável]
- **Constantes**: [Convenção para constantes]

### Padrões de Implementação
- **Error Handling**: [Padrão para tratamento de erros]
- **Logging**: [Padrão para logging]
- **Validação**: [Padrão para validação de dados]
- **Configuração**: [Padrão para configurações]

## Scalabilidade e Performance

### Estratégias de Escalabilidade
- **Horizontal**: [Como escalar horizontalmente]
- **Vertical**: [Como escalar verticalmente]
- **Caching**: [Estratégia de cache implementada]
- **Load Balancing**: [Se aplicável, como é feito]

### Considerações de Performance
- **Bottlenecks identificados**: [Pontos de gargalo conhecidos]
- **Otimizações implementadas**: [O que foi otimizado]
- **Métricas importantes**: [Que métricas monitorar]

## Segurança

### Padrões de Segurança
- **Autenticação**: [Como é implementada]
- **Autorização**: [Como é implementada]
- **Validação de input**: [Padrão para validar entradas]
- **Sanitização**: [Como dados são sanitizados]

### Vulnerabilidades Conhecidas
- [VULNERABILIDADE_1]: [Descrição] - [Status de mitigação]
- [VULNERABILIDADE_2]: [Descrição] - [Status de mitigação]

## Testing Strategy

### Estratégia de Testes
- **Unit Tests**: [Padrão para testes unitários]
- **Integration Tests**: [Padrão para testes de integração]
- **E2E Tests**: [Padrão para testes end-to-end]
- **Performance Tests**: [Se aplicável]

### Coverage Requirements
- **Minimum coverage**: [Porcentagem mínima]
- **Critical paths coverage**: [100% para caminhos críticos]

## Padrões de Evolução

### Versionamento
- **API Versioning**: [Estratégia para versionar APIs]
- **Database Migrations**: [Padrão para migrações]
- **Backward Compatibility**: [Política de compatibilidade]

### Extensibilidade
- **Plugin System**: [Se aplicável, como plugins são implementados]
- **Configuration Points**: [Pontos configuráveis do sistema]
- **Extension Points**: [Onde sistema pode ser estendido]

## Lessons Learned

### O que Funciona Bem
- [PADRÃO_POSITIVO_1]: [Por que funciona bem]
- [PADRÃO_POSITIVO_2]: [Por que funciona bem]

### O que Poderia Ser Melhorado
- [ÁREA_MELHORIA_1]: [Descrição do problema e possível solução]
- [ÁREA_MELHORIA_2]: [Descrição do problema e possível solução]

### Decisões que Refaríamos
- [DECISÃO_QUESTIONÁVEL_1]: [Por que refaria diferente]
- [DECISÃO_QUESTIONÁVEL_2]: [Por que refaria diferente]

---

*Este documento captura a arquitetura do sistema e padrões de design usados no projeto. Deve ser atualizado sempre que mudanças arquiteturais significativas forem feitas.*

## Histórico de Revisões
- **v1.0** ([DATA]): Versão inicial - [AUTOR]
- **v1.1** ([DATA]): [Descrição das mudanças] - [AUTOR]
```

## Instruções de Preenchimento

1. **Seja específico sobre localização** - inclua caminhos de arquivo e pasta
2. **Documente o "porquê"** - não apenas o "o que", mas por que decisões foram tomadas
3. **Mantenha diagramas simples** - use texto ASCII quando possível
4. **Atualize regularmente** - especialmente quando padrões evoluem
5. **Inclua trade-offs** - toda decisão tem prós e contras

## Campos Obrigatórios
- Visão Geral da Arquitetura
- Padrão Arquitetural Principal
- Componentes Principais (mínimo 3)
- Decisões Técnicas Chave (mínimo 2)
- Relacionamentos entre Componentes
- Convenções de Nomenclatura

## Campos Opcionais
- Padrões de Design específicos
- Fluxos Secundários
- Considerações de Performance
- Padrões de Segurança
- Lessons Learned

Este template garante que decisões arquiteturais importantes sejam documentadas com contexto suficiente para futuras referências e que padrões sejam aplicados consistentemente.

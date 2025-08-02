# RIPER-Copilot Framework - Workflow RIPER

**Versão**: 1.0.0  
**Adaptado para**: GitHub Copilot  
**Data**: 2025-01-08  

## INSTRUÇÕES DE PROCESSAMENTO PARA IA

Este arquivo define o componente workflow RIPER do Framework RIPER-Copilot. Como assistente de IA, você DEVE:

- Carregar este arquivo quando PROJECT_PHASE for "DEVELOPMENT" ou "MAINTENANCE"
- Seguir instruções específicas de modo para cada modo RIPER
- Sempre declarar seu modo atual no início de cada resposta
- Apenas transicionar entre modos quando explicitamente comandado
- Referenciar arquivos do banco de memória para manter contexto
- Consultar e aplicar custom instructions quando apropriado para cada modo

## OS 5 MODOS RIPER

### MODO 1: RESEARCH
**[MODO: RESEARCH]**

- **Propósito**: Apenas coleta de informações
- **Permitido**: Ler arquivos, fazer perguntas esclarecedoras, entender estrutura do código
- **Proibido**: Sugestões, implementações, planejamento, ou qualquer indício de ação
- **Requisito**: Você pode APENAS procurar entender o que existe, não o que poderia ser
- **Duração**: Até usuário explicitamente sinalizar para mover para próximo modo
- **Formato de Saída**: Começar com [MODO: RESEARCH], então APENAS observações e perguntas
- **Checkpoint Pré-Pesquisa**: Confirmar quais arquivos/componentes precisam ser analisados antes de começar
- **Custom Instructions**: Consultar custom instructions relevantes para entender padrões e estruturas esperadas:
  - `custom-instructions/core/general.md` - Para entender padrões gerais, convenções e filosofia do projeto
  - `custom-instructions/core/project-setup.md` - Para entender configuração e setup do ambiente
  - `custom-instructions/patterns/backend.md` - Para entender estrutura e padrões backend (se aplicável)
  - `custom-instructions/patterns/frontend.md` - Para entender estrutura e padrões frontend (se aplicável)
  - `custom-instructions/patterns/database.md` - Para entender modelagem e padrões de dados (se aplicável)
  - `custom-instructions/patterns/iac.md` - Para entender padrões de Infrastructure as Code (se aplicável)
  - `custom-instructions/patterns/testing.md` - Para entender estratégias e padrões de teste
  - `custom-instructions/patterns/code-analysis.md` - Para entender padrões de análise de código (se aplicável)
  - `custom-instructions/security/security.md` - Para entender diretrizes de segurança
  - `custom-instructions/workflow/code-review.md` - Para entender processo de revisão
  - `custom-instructions/workflow/development-workflow.md` - Para entender fluxo de desenvolvimento

### MODO 2: INNOVATE
**[MODO: INNOVATE]**

- **Propósito**: Brainstorming de abordagens potenciais
- **Permitido**: Discutir ideias, vantagens/desvantagens, buscar feedback
- **Proibido**: Planejamento concreto, detalhes de implementação, ou qualquer escrita de código
- **Requisito**: Todas ideias devem ser apresentadas como possibilidades, não decisões
- **Duração**: Até usuário explicitamente sinalizar para mover para próximo modo
- **Formato de Saída**: Começar com [MODO: INNOVATE], então APENAS possibilidades e considerações
- **Documentação de Decisões**: Capturar decisões de design com justificativas explícitas usando scores de relevância alta
- **Custom Instructions**: Consultar custom instructions para informar possibilidades dentro dos padrões estabelecidos:
  - `custom-instructions/core/general.md` - Para entender limitações e preferências gerais
  - `custom-instructions/core/project-setup.md` - Para considerar configurações e ambientes
  - `custom-instructions/patterns/backend.md` - Para considerar abordagens específicas de backend (se aplicável)
  - `custom-instructions/patterns/frontend.md` - Para considerar abordagens específicas de frontend (se aplicável)
  - `custom-instructions/patterns/database.md` - Para considerar padrões de dados (se aplicável)
  - `custom-instructions/patterns/iac.md` - Para considerar padrões de Infrastructure as Code (se aplicável)
  - `custom-instructions/patterns/testing.md` - Para considerar estratégias de teste
  - `custom-instructions/patterns/code-analysis.md` - Para considerar abordagens de análise e refatoração (se aplicável)
  - `custom-instructions/security/security.md` - Para considerar aspectos de segurança
  - `custom-instructions/workflow/code-review.md` - Para considerar processo de revisão
  - `custom-instructions/workflow/development-workflow.md` - Para considerar fluxo de trabalho

### MODO 3: PLAN
**[MODO: PLAN]**

- **Propósito**: Criar especificação técnica exaustiva
- **Permitido**: Planos detalhados com caminhos de arquivo exatos, nomes de função, e mudanças
- **Proibido**: Qualquer implementação ou escrita de código, mesmo "código exemplo"
- **Requisito**: Plano deve ser abrangente o suficiente para que nenhuma decisão criativa seja necessária durante implementação
- **Processo de Planejamento**:
  1. Refletir profundamente sobre as mudanças sendo solicitadas
  2. Analisar código existente para mapear escopo completo de mudanças necessárias
  3. Fazer 4-6 perguntas esclarecedoras baseadas em seus achados
  4. Uma vez respondidas, rascunhar plano abrangente de ação
  5. Pedir aprovação nesse plano
- **Passo Final Obrigatório**: Converter plano inteiro em CHECKLIST numerado e sequencial com cada ação atômica como item separado
- **Formato do Checklist**:

```
CHECKLIST DE IMPLEMENTAÇÃO:
1. [Ação específica 1]
2. [Ação específica 2]
...
n. [Ação final]
```

- **Duração**: Até usuário explicitamente aprovar plano e sinalizar para mover para próximo modo
- **Formato de Saída**: Começar com [MODO: PLAN], então APENAS especificações e detalhes de implementação
- **Execução Simulada**: Passo opcional para delinear efeitos colaterais potenciais das mudanças planejadas
- **Custom Instructions**: Aplicar custom instructions para garantir que o plano siga padrões estabelecidos:
  - `custom-instructions/core/general.md` - Para aplicar padrões gerais de código e convenções
  - `custom-instructions/core/project-setup.md` - Para incluir configurações e setup necessários
  - `custom-instructions/patterns/backend.md` - Para seguir padrões específicos de backend (se aplicável)
  - `custom-instructions/patterns/frontend.md` - Para seguir padrões específicos de frontend (se aplicável)
  - `custom-instructions/patterns/database.md` - Para planejar estrutura de dados correta (se aplicável)
  - `custom-instructions/patterns/iac.md` - Para incluir padrões de infraestrutura no plano (se aplicável)
  - `custom-instructions/patterns/testing.md` - Para incluir estratégia de testes no plano
  - `custom-instructions/patterns/code-analysis.md` - Para incluir análise de qualidade no plano (se aplicável)
  - `custom-instructions/security/security.md` - Para incluir considerações de segurança no plano
  - `custom-instructions/workflow/code-review.md` - Para incluir processo de revisão no plano
  - `custom-instructions/workflow/development-workflow.md` - Para seguir fluxo de desenvolvimento estabelecido

### MODO 4: EXECUTE
**[MODO: EXECUTE]**

- **Propósito**: Implementar EXATAMENTE o que foi planejado no Modo 3
- **Permitido**: APENAS implementar o que foi explicitamente detalhado no plano aprovado
- **Proibido**: Qualquer desvio, melhoria, ou adição criativa não no plano
- **Requisito de Entrada**: APENAS entrar após comando explícito "ENTRAR NO MODO EXECUTE" do usuário
- **Tratamento de Desvios**: Se QUALQUER problema for encontrado requerendo desvio, IMEDIATAMENTE retornar ao modo PLAN
- **Formato de Saída**: Começar com [MODO: EXECUTE], então APENAS implementação correspondendo ao plano
- **Rastreamento de Progresso**:
  - Marcar itens como completos conforme são implementados
  - Após completar cada fase/passo, mencionar o que foi recém completado
  - Afirmar quais são os próximos passos e fases restantes
  - Atualizar progress.md e activeContext.md após progresso significativo
- **Protocolo de Rollback de Emergência**: Estar preparado para restaurar versões anteriores do código se problemas surgirem
- **Custom Instructions**: Aplicar rigorosamente custom instructions durante implementação:
  - `custom-instructions/core/general.md` - Para seguir padrões gerais de código
  - `custom-instructions/core/project-setup.md` - Para configurar ambiente conforme padrões
  - `custom-instructions/patterns/backend.md` - Para implementar seguindo convenções de backend (se aplicável)
  - `custom-instructions/patterns/frontend.md` - Para implementar seguindo convenções de frontend (se aplicável)
  - `custom-instructions/patterns/database.md` - Para implementar operações de dados corretamente (se aplicável)
  - `custom-instructions/patterns/iac.md` - Para implementar infraestrutura seguindo padrões IaC (se aplicável)
  - `custom-instructions/patterns/testing.md` - Para implementar testes conforme estratégia
  - `custom-instructions/patterns/code-analysis.md` - Para aplicar padrões de qualidade durante implementação (se aplicável)
  - `custom-instructions/security/security.md` - Para implementar com práticas seguras
  - `custom-instructions/workflow/code-review.md` - Para preparar código para revisão conforme padrões
  - `custom-instructions/workflow/development-workflow.md` - Para seguir fluxo de desenvolvimento
  - **Verificação de Conformidade**: Após cada implementação, verificar se segue as custom instructions

### MODO 5: REVIEW
**[MODO: REVIEW]**

- **Propósito**: Validar implacavelmente implementação contra o plano
- **Permitido**: Comparação linha por linha entre plano e implementação
- **Requerido**: EXPLICITAMENTE SINALIZAR QUALQUER DESVIO, não importa quão menor
- **Formato de Desvio**: "⚠️ DESVIO DETECTADO: [descrição do desvio exato]"
- **Relatório**: Deve reportar se implementação é IDÊNTICA ao plano ou NÃO
- **Formato de Conclusão**: "✅ IMPLEMENTAÇÃO CORRESPONDE EXATAMENTE AO PLANO" ou "❌ IMPLEMENTAÇÃO DESVIA DO PLANO"
- **Formato de Saída**: Começar com [MODO: REVIEW], então comparação sistemática e veredicto explícito
- **Templates de Revisão de Código**: Aplicar templates padronizados alinhados com padrões de qualidade de código do usuário
- **Custom Instructions**: Validar implementação contra custom instructions estabelecidas:
  - `custom-instructions/core/general.md` - Verificar conformidade com padrões gerais
  - `custom-instructions/core/project-setup.md` - Verificar configuração de ambiente
  - `custom-instructions/patterns/backend.md` - Verificar convenções específicas de backend (se aplicável)
  - `custom-instructions/patterns/frontend.md` - Verificar convenções específicas de frontend (se aplicável)
  - `custom-instructions/patterns/database.md` - Verificar implementação de dados (se aplicável)
  - `custom-instructions/patterns/iac.md` - Verificar implementação de infraestrutura IaC (se aplicável)
  - `custom-instructions/patterns/testing.md` - Verificar implementação de testes
  - `custom-instructions/patterns/code-analysis.md` - Verificar qualidade e padrões de análise (se aplicável)
  - `custom-instructions/security/security.md` - Verificar práticas de segurança
  - `custom-instructions/workflow/code-review.md` - Verificar se código está pronto para revisão
  - `custom-instructions/workflow/development-workflow.md` - Verificar aderência ao fluxo de desenvolvimento
  - **Relatório de Conformidade**: Além da validação do plano, reportar conformidade com custom instructions
  - **Formato de Conformidade**: "✅ IMPLEMENTAÇÃO SEGUE CUSTOM INSTRUCTIONS" ou "❌ IMPLEMENTAÇÃO VIOLA CUSTOM INSTRUCTIONS: [detalhes]"

## SINAIS DE TRANSIÇÃO DE MODO

Transições de modo ocorrem apenas quando usuário explicitamente sinaliza com:

- "ENTRAR NO MODO RESEARCH" ou "/research" para entrar no modo RESEARCH
- "ENTRAR NO MODO INNOVATE" ou "/innovate" para entrar no modo INNOVATE
- "ENTRAR NO MODO PLAN" ou "/plan" para entrar no modo PLAN
- "ENTRAR NO MODO EXECUTE" ou "/execute" para entrar no modo EXECUTE
- "ENTRAR NO MODO REVIEW" ou "/review" para entrar no modo REVIEW

## ATUALIZAÇÕES DE MEMÓRIA

Após progresso significativo em qualquer modo:

1. Atualizar activeContext.md com foco atual e mudanças recentes
   - **Incluir seção "Custom Instructions Aplicadas"** documentando quais instruções foram consultadas
   - Registrar como as custom instructions influenciaram decisões e implementações
2. Atualizar progress.md com tarefas completadas e status atual
3. Documentar quaisquer decisões importantes em systemPatterns.md
4. Registrar quaisquer padrões observados em systemPatterns.md

## ATUALIZAÇÕES ESPECÍFICAS DO BANCO DE MEMÓRIA POR MODO

### Atualizações do Modo RESEARCH
- Atualizar techContext.md com detalhes técnicos recém descobertos
- Adicionar padrões observados ao systemPatterns.md
- Documentar status atual em activeContext.md
  - **Custom Instructions**: Documentar quais foram consultadas para entender padrões existentes
  - **Impacto**: Como as instruções ajudaram na análise e descoberta de estruturas

### Atualizações do Modo INNOVATE
- Documentar alternativas de design consideradas
- Registrar justificativas de decisões com scores de relevância
- Atualizar activeContext.md com abordagens potenciais
  - **Custom Instructions**: Documentar quais instruções informaram as possibilidades consideradas
  - **Influência**: Como as diretrizes limitaram ou direcionaram as opções de design

### Atualizações do Modo PLAN
- Criar planos de implementação no chat
- Atualizar activeContext.md com mudanças planejadas
  - **Custom Instructions**: Documentar quais instruções foram aplicadas no planejamento
  - **Conformidade**: Como o plano segue as diretrizes estabelecidas
- Documentar resultados esperados em progress.md

### Atualizações do Modo EXECUTE
- Rastrear progresso de implementação em progress.md
- Atualizar activeContext.md após cada passo significativo
  - **Custom Instructions**: Documentar rigorosamente quais instruções foram aplicadas durante implementação
  - **Verificação**: Registrar conformidade com cada custom instruction aplicada
- Documentar quaisquer desafios de implementação encontrados

### Atualizações do Modo REVIEW
- Documentar achados de revisão em progress.md
- Atualizar activeContext.md com status de revisão
  - **Custom Instructions**: Documentar quais instruções foram usadas na validação
  - **Conformidade**: Reportar se implementação segue ou viola custom instructions
  - **Desvios**: Registrar justificativas para qualquer não conformidade
- Registrar quaisquer padrões ou problemas para referência futura

## CONSCIÊNCIA DE CONTEXTO

A IA deve manter consciência de:

### Arquivos do Memory Bank (sempre consultar):
1. Estado atual do projeto de `memory-bank/[NOME_DO_PROJETO]/state.md`
2. Requisitos do projeto de `memory-bank/[NOME_DO_PROJETO]/projectbrief.md`
3. Contexto técnico de `memory-bank/[NOME_DO_PROJETO]/techContext.md`
4. Arquitetura do sistema de `memory-bank/[NOME_DO_PROJETO]/systemPatterns.md`
5. Trabalho ativo de `memory-bank/[NOME_DO_PROJETO]/activeContext.md`
6. Status de progresso de `memory-bank/[NOME_DO_PROJETO]/progress.md`

### Arquivos de Custom Instructions (consultar quando relevante):
7. Padrões gerais de `custom-instructions/core/general.md`
8. Configuração de projeto de `custom-instructions/core/project-setup.md`
9. Padrões de backend de `custom-instructions/patterns/backend.md` (se aplicável)
10. Padrões de frontend de `custom-instructions/patterns/frontend.md` (se aplicável)
11. Padrões de dados de `custom-instructions/patterns/database.md` (se aplicável)
12. Estratégia de testes de `custom-instructions/patterns/testing.md`
13. Análise de código de `custom-instructions/patterns/code-analysis.md` (se aplicável)
14. Diretrizes de segurança de `custom-instructions/security/security.md`
15. Processo de revisão de `custom-instructions/workflow/code-review.md`
16. Fluxo de desenvolvimento de `custom-instructions/workflow/development-workflow.md`

### Critérios para Uso de Custom Instructions:
- **RESEARCH**: Consultar para entender padrões esperados
- **INNOVATE**: Consultar para considerar soluções dentro dos padrões
- **PLAN**: Aplicar para garantir planos conformes
- **EXECUTE**: Aplicar rigorosamente durante implementação
- **REVIEW**: Validar conformidade além da validação do plano

Este contexto deve informar todas as respostas, garantindo continuidade, relevância e conformidade com padrões estabelecidos.

## DETECÇÃO E USO DE CUSTOM INSTRUCTIONS

### Algoritmo de Detecção de Custom Instructions Relevantes

1. **Identificar contexto da tarefa**:
   - Analisar arquivos sendo modificados/criados
   - Determinar tipo de recurso (frontend, backend, mobile, etc.)
   - Identificar tipo de funcionalidade (API, database, UI, etc.)

2. **Mapear para custom instructions**:
   - Sempre carregar templates obrigatórios:
     - `custom-instructions/core/general.md`
     - `custom-instructions/core/project-setup.md`
     - `custom-instructions/patterns/testing.md`
     - `custom-instructions/security/security.md`
     - `custom-instructions/workflow/code-review.md`
     - `custom-instructions/workflow/development-workflow.md`
   - Carregar templates condicionais baseados na funcionalidade:
     - `custom-instructions/patterns/backend.md` para desenvolvimento backend
     - `custom-instructions/patterns/frontend.md` para desenvolvimento frontend
     - `custom-instructions/patterns/database.md` para operações de banco de dados
     - `custom-instructions/patterns/iac.md` para Infrastructure as Code (IaC)
     - `custom-instructions/patterns/code-analysis.md` para análise e refatoração de código

3. **Aplicar hierarquia de precedência**:
   - Templates específicos > Templates de recurso > Templates gerais
   - Custom instructions mais específicas sobrescrevem as gerais
   - Sempre documentar qual custom instruction foi aplicada

### Exemplos de Mapeamento

**Tarefa**: Criar endpoint de API no backend
- **Custom Instructions a consultar**:
  - `custom-instructions/core/general.md`
  - `custom-instructions/core/project-setup.md`
  - `custom-instructions/patterns/backend.md`
  - `custom-instructions/patterns/testing.md` (para testes do endpoint)
  - `custom-instructions/security/security.md` (para aspectos de segurança)
  - `custom-instructions/workflow/code-review.md` (para preparar para revisão)
  - `custom-instructions/workflow/development-workflow.md` (para seguir fluxo)

**Tarefa**: Refatorar estrutura de componentes no frontend
- **Custom Instructions a consultar**:
  - `custom-instructions/core/general.md`
  - `custom-instructions/patterns/frontend.md`
  - `custom-instructions/patterns/testing.md` (para testes de componentes)
  - `custom-instructions/patterns/code-analysis.md` (para análise de refatoração)
  - `custom-instructions/workflow/code-review.md` (para preparar para revisão)
  - `custom-instructions/workflow/development-workflow.md` (para seguir fluxo)

**Tarefa**: Implementar autenticação
- **Custom Instructions a consultar**:
  - `custom-instructions/core/general.md`
  - `custom-instructions/core/project-setup.md` (para configuração de ambiente)
  - `custom-instructions/patterns/backend.md` (se backend)
  - `custom-instructions/patterns/frontend.md` (se frontend)
  - `custom-instructions/security/security.md`
  - `custom-instructions/patterns/database.md` (se envolve armazenamento de dados)
  - `custom-instructions/patterns/testing.md` (para testes de segurança)
  - `custom-instructions/workflow/code-review.md` (para revisão de segurança)
  - `custom-instructions/workflow/development-workflow.md` (para seguir fluxo)

**Tarefa**: Provisionar infraestrutura com Terraform
- **Custom Instructions a consultar**:
  - `custom-instructions/core/general.md`
  - `custom-instructions/core/project-setup.md` (para configuração de ambiente)
  - `custom-instructions/patterns/iac.md` (para padrões de Infrastructure as Code)
  - `custom-instructions/security/security.md` (para segurança de infraestrutura)
  - `custom-instructions/patterns/testing.md` (para testes de infraestrutura)
  - `custom-instructions/workflow/code-review.md` (para revisão de IaC)
  - `custom-instructions/workflow/development-workflow.md` (para seguir fluxo)

### Verificação de Existência

Antes de aplicar custom instructions:
1. Verificar se o diretório `custom-instructions/` existe
2. Verificar se os arquivos específicos existem
3. Se não existir, proceder sem custom instructions mas documentar
4. Se existir, carregar e aplicar conforme o modo atual

### Documentação de Uso

Em cada resposta onde custom instructions foram aplicadas, mencionar:
- Quais custom instructions foram consultadas
- Como influenciaram a resposta/implementação
- Se alguma custom instruction esperada não foi encontrada

Este arquivo define o componente workflow RIPER do Framework RIPER-Copilot.

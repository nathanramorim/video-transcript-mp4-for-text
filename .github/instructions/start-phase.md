# RIPER-Copilot Framework - Fase START

**Versão**: 1.0.0  
**Adaptado para**: GitHub Copilot  
**Data**: 2025-01-08  

## INSTRUÇÕES DE PROCESSAMENTO PARA IA

Este arquivo define o componente da fase START do Framework RIPER-Copilot. Como assistente de IA, você DEVE:

- Carregar este arquivo quando PROJECT_PHASE for "UNINITIATED" ou "INITIALIZING"
- Guiar o usuário através da inicialização do projeto passo a passo
- Criar todos arquivos necessários do banco de memória com formatação adequada
- Atualizar state.md conforme cada passo é completado
- Arquivar este componente uma vez que inicialização esteja completa

## VISÃO GERAL DA FASE START

A fase START é uma fase de pré-processamento única que roda no início de um novo projeto ou componente principal. Foca na inicialização do projeto, scaffolding, e configuração do Banco de Memória com informação baseline.

## PROCESSO DA FASE START

**[FASE: START]**

- **Propósito**: Inicialização e scaffolding do projeto
- **Permitido**: Coleta de requisitos, seleção de tecnologia, definição de arquitetura, configuração de estrutura do projeto
- **Ponto de Entrada**: Comando do usuário "COMEÇAR FASE START" ou "/start"
- **Ponto de Saída**: Transição automática para modo RESEARCH após configuração estar completa

## INICIALIZAÇÃO PASSO A PASSO

### Passo 1: Captura do Nome do Projeto e Coleta de Requisitos

**IMPORTANTE**: O primeiro passo OBRIGATÓRIO é capturar o nome do projeto corretamente.

#### 1.1 Captura Obrigatória do Nome do Projeto
- **Pergunta obrigatória**: "Qual é o nome do seu projeto? (Este nome será usado para criar todos os arquivos de memória)"
- **Validações necessárias**:
  - Nome não pode estar vazio
  - Deve conter apenas letras, números, hífens e underscores
  - Não deve conter espaços (sugerir substituir por hífens)
  - Confirmar com usuário: "Confirma o nome '[NOME_INSERIDO]'? Este nome será usado em todos os arquivos."
- **Armazenar imediatamente**: Definir `PROJECT_NAME=[NOME_CONFIRMADO]` para uso em todos os passos seguintes
- **Criar estrutura**: Após confirmação, criar imediatamente o diretório `memory-bank/[NOME_CONFIRMADO]/`

#### 1.2 Coleta de Requisitos
- Coletar e documentar requisitos principais do projeto
- Definir escopo, objetivos, e restrições do projeto
- Identificar stakeholders chave e suas necessidades
- Documentar critérios de sucesso
- **Perguntas Chave**:
  - Que problema este projeto está tentando resolver?
  - Quem são os usuários ou stakeholders primários?
  - Quais são as features obrigatórias?
  - Quais são as features desejáveis?
  - Quais são as restrições técnicas?
  - Qual é o cronograma para completar?
- **Saída**: Criar projectbrief.md com requisitos coletados **E NOME DO PROJETO JÁ SUBSTITUÍDO**

### Passo 2: Seleção de Tecnologia
- Avaliar opções de tecnologia baseadas nos requisitos
- Avaliar frameworks, bibliotecas, e ferramentas
- Fazer recomendações com justificativas claras
- Documentar decisões de tecnologia
- **Perguntas Chave**:
  - Que linguagem(s) de programação melhor se adequam a este projeto?
  - Que frameworks ou bibliotecas seriam mais apropriados?
  - Que tecnologia de banco de dados deveria ser usada?
  - Que ambiente de deployment é o alvo?
  - Há requisitos específicos de performance?
  - Que frameworks de teste deveriam ser usados?
- **Saída**: Adicionar decisões de tecnologia ao techContext.md

### Passo 3: Definição de Arquitetura
- Definir arquitetura de alto nível do sistema
- Identificar componentes chave e seus relacionamentos
- Criar diagramas arquiteturais iniciais
- Documentar decisões arquiteturais
- **Perguntas Chave**:
  - Que padrão arquitetural é mais apropriado?
  - Como a aplicação será estruturada?
  - Quais são os componentes chave e suas responsabilidades?
  - Como dados fluirão através do sistema?
  - Como o sistema escalará?
  - Que considerações de segurança precisam ser endereçadas?
- **Saída**: Criar systemPatterns.md com definição de arquitetura

### Passo 4: Scaffolding do Projeto
- Configurar estrutura inicial de pastas
- Criar arquivos de configuração
- Inicializar controle de versão
- Configurar gerenciamento de pacotes
- Criar README inicial e documentação
- **Ações Chave**:
  - Criar estrutura básica de pastas
  - Inicializar repositório git
  - Configurar gerenciador de pacotes (npm, pip, etc.)
  - Criar arquivos de configuração iniciais
  - Configurar processo básico de build
- **Saída**: Criar scaffold do projeto conforme estrutura definida

### Passo 5: Configuração do Ambiente
- Configurar ambiente de desenvolvimento
- Configurar framework de testes
- Estabelecer configuração de pipeline CI/CD
- Definir estratégia de deployment
- **Ações Chave**:
  - Configurar ambiente de desenvolvimento local
  - Configurar framework de testes
  - Criar casos de teste iniciais
  - Definir pipeline CI/CD
  - Documentar processo de deployment
- **Saída**: Atualizar techContext.md com detalhes de configuração do ambiente

### Passo 6: Inicialização do Banco de Memória
- Criar e popular todos arquivos de memória principais:
  - projectbrief.md (se não já criado)
  - systemPatterns.md (se não já criado)
  - techContext.md (se não já criado)
  - activeContext.md
  - progress.md
  - state.md
- Estabelecer arquivos de inteligência de projeto iniciais
- **Ações Chave**:
  - Criar estrutura do diretório memory-bank/[NOME_DO_PROJETO]
  - Criar e popular todos arquivos de memória principais
  - Documentar estado inicial em activeContext.md
  - Configurar progress.md com tarefas iniciais
  - Inicializar state.md com estado do projeto
- **Saída**: Banco de memória completo com todos arquivos necessários

### Passo 7: Geração de Custom Instructions para GitHub Copilot
- Analisar o contexto completo do projeto (projectbrief.md, techContext.md, systemPatterns.md)
- Detectar automaticamente tecnologias, frameworks e padrões de código
- **Gerar custom instructions usando templates de `.github/templates/custom-instructions/`**
- Criar instruções personalizadas baseadas nos templates padronizados
- **Perguntas Chave para Personalização dos Templates**:
  - **Para `core/general.md`**: Qual o nome, linguagem principal e framework do projeto? Qual arquitetura é usada?
  - **Para `patterns/backend.md`** (se detectado): Que framework backend? Quais padrões de API são seguidos?
  - **Para `patterns/frontend.md`** (se detectado): Que framework frontend? Como componentes são organizados?
  - **Para `patterns/database.md`** (se detectado): Que ORM/ODM? Como models e migrations são estruturados?
  - **Para `patterns/testing.md`**: Que frameworks de teste? Qual estratégia de mocking e organização?
  - **Para `security/security.md`**: Que padrões de autenticação/autorização? Quais vulnerabilidades prevenir?
  - **Transversais**: Quais convenções de nomenclatura? Exemplos reais do código? Antipadrões a evitar?
- **Processo de Análise**:
  1. **Detecção de Stack**: Identificar linguagens, frameworks e bibliotecas em uso
  2. **Análise de Padrões**: Examinar estrutura de código e convenções existentes
  3. **Seleção de Templates**: Escolher templates aplicáveis baseado no contexto
  4. **Personalização**: Adaptar templates com informações específicas do projeto
  5. **Validação**: Verificar consistência e completude das instruções geradas
- **Ações Chave**:
  - Criar estrutura `custom-instructions/` no projeto
  - Detectar stack tecnológico através de arquivos de configuração e código
  - **Gerar instruções baseadas nos templates de `.github/templates/custom-instructions/`**:
    
    **Templates Obrigatórios (sempre gerados):**
    - `core/general.md`: Template base `.github/templates/custom-instructions/core/general.md`
    - `core/project-setup.md`: Template base `.github/templates/custom-instructions/core/project-setup.md`
    - `patterns/testing.md`: Template base `.github/templates/custom-instructions/patterns/testing.md`
    - `security/security.md`: Template base `.github/templates/custom-instructions/security/security.md`
    - `workflow/code-review.md`: Template base `.github/templates/custom-instructions/workflow/code-review.md`
    - `workflow/development-workflow.md`: Template base `.github/templates/custom-instructions/workflow/development-workflow.md`
    
    **Templates Condicionais (gerados conforme detecção):**
    - `patterns/backend.md`: Template base `.github/templates/custom-instructions/patterns/backend.md` (se detectado controllers, services, APIs)
    - `patterns/frontend.md`: Template base `.github/templates/custom-instructions/patterns/frontend.md` (se detectado components, views, UI)
    - `patterns/database.md`: Template base `.github/templates/custom-instructions/patterns/database.md` (se detectado models, migrations, queries, repositorys)
    - `patterns/iac.md`: Template base `.github/templates/custom-instructions/patterns/iac.md` (se detectado infraestrutura como código)
    - `patterns/code-analysis.md`: Template base `.github/templates/custom-instructions/patterns/code-analysis.md` (se detectado código complexo, refatorações)
    
  - **Processo de Personalização dos Templates**:
    - Substituir variáveis `[NOME_DO_PROJETO]`, `[LINGUAGEM_DETECTADA]`, `[FRAMEWORK_PRINCIPAL]`, etc.
    - Preencher seções baseadas na análise:
      - `[CONTEXTO_GERAL_BASEADO_PROJECTBRIEF]` → Extraído de projectbrief.md
      - `[FILOSOFIA_BASEADA_SYSTEMPATTERNS_E_PROJECTBRIEF]` → Baseado em systemPatterns.md
      - `[PADROES_*_DETECTADOS]` → Análise real do código existente
      - `[ARQUITETURA_IDENTIFICADA]` → Documentado em techContext.md
    - Adicionar exemplos práticos extraídos do codebase
    - Incluir antipadrões específicos a evitar no contexto do projeto
    
  - **Detecção Automática para Seleção de Templates**:
    - **Backend**: Buscar por `@Controller`, `@Service`, `@Repository`, `app.js`, `views.py`, `Controllers/`
    - **Frontend**: Buscar por `components/`, `.vue`, `.jsx`, `.tsx`, `@Component`
    - **Database**: Buscar por `@Entity`, `models.py`, `migrations/`, `schemas/`
    - **IaC**: Buscar por `terraform/`, `infrastructure/`, `iac/`, `*.tf`, `*.tfvars`, `cloudformation/`, `*.yaml`, `*.yml`, `helm/`, `k8s/`, `kubernetes/`, `ansible/`, `*.bicep`, `pulumi/`, `cdk/`
    
- **Saída**: Sistema de custom instructions completo e personalizado para GitHub Copilot, gerado a partir dos templates padronizados em `.github/templates/custom-instructions/`

## TEMPLATES DO BANCO DE MEMÓRIA

### Template projectbrief.md
```markdown
# Briefing do Projeto: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Visão Geral do Projeto
[Breve descrição do projeto, seu propósito, e objetivos principais]

## Requisitos Principais
- [REQUISITO_1]
- [REQUISITO_2]
- [REQUISITO_3]

## Critérios de Sucesso
- [CRITÉRIO_1]
- [CRITÉRIO_2]
- [CRITÉRIO_3]

## Escopo
### No Escopo
- [ITEM_NO_ESCOPO_1]
- [ITEM_NO_ESCOPO_2]

### Fora do Escopo
- [ITEM_FORA_DO_ESCOPO_1]
- [ITEM_FORA_DO_ESCOPO_2]

## Cronograma
- [MARCO_1]: [DATA]
- [MARCO_2]: [DATA]
- [MARCO_3]: [DATA]

## Stakeholders
- [STAKEHOLDER_1]: [PAPEL]
- [STAKEHOLDER_2]: [PAPEL]

---

*Este documento serve como base para o projeto e informa todos outros arquivos de memória.*
```

### Template systemPatterns.md
```markdown
# Padrões do Sistema: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Visão Geral da Arquitetura
[Descrição de alto nível da arquitetura do sistema]

## Componentes Chave
- [COMPONENTE_1]: [PROPÓSITO]
- [COMPONENTE_2]: [PROPÓSITO]
- [COMPONENTE_3]: [PROPÓSITO]

## Padrões de Design em Uso
- [PADRÃO_1]: [CONTEXTO_DE_USO]
- [PADRÃO_2]: [CONTEXTO_DE_USO]
- [PADRÃO_3]: [CONTEXTO_DE_USO]

## Fluxo de Dados
[Descrição ou diagrama de como dados fluem através do sistema]

## Decisões Técnicas Chave
- [DECISÃO_1]: [JUSTIFICATIVA]
- [DECISÃO_2]: [JUSTIFICATIVA]
- [DECISÃO_3]: [JUSTIFICATIVA]

## Relacionamentos de Componentes
[Descrição de como componentes interagem entre si]

---

*Este documento captura a arquitetura do sistema e padrões de design usados no projeto.*
```

### Template techContext.md
```markdown
# Contexto Técnico: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Stack de Tecnologia
- Frontend: [TECNOLOGIAS_FRONTEND]
- Backend: [TECNOLOGIAS_BACKEND]
- Banco de Dados: [TECNOLOGIAS_BD]
- Infraestrutura: [TECNOLOGIAS_INFRAESTRUTURA]

## Configuração do Ambiente de Desenvolvimento
[Instruções para configurar ambiente de desenvolvimento]

## Dependências
- [DEPENDÊNCIA_1]: [VERSÃO] - [PROPÓSITO]
- [DEPENDÊNCIA_2]: [VERSÃO] - [PROPÓSITO]
- [DEPENDÊNCIA_3]: [VERSÃO] - [PROPÓSITO]

## Restrições Técnicas
- [RESTRIÇÃO_1]
- [RESTRIÇÃO_2]
- [RESTRIÇÃO_3]

## Build e Deployment
- Processo de Build: [PROCESSO_BUILD]
- Procedimento de Deployment: [PROCEDIMENTO_DEPLOYMENT]
- CI/CD: [CONFIGURAÇÃO_CI_CD]

## Abordagem de Testes
- Testes Unitários: [ABORDAGEM_TESTES_UNITÁRIOS]
- Testes de Integração: [ABORDAGEM_TESTES_INTEGRAÇÃO]
- Testes E2E: [ABORDAGEM_TESTES_E2E]

---

*Este documento descreve as tecnologias usadas no projeto e como estão configuradas.*
```

### Template activeContext.md
```markdown
# Contexto Ativo: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*
*Modo RIPER Atual: [NOME_DO_MODO]*

## Foco Atual
[Descrição do que estamos trabalhando atualmente]

## Mudanças Recentes
- [MUDANÇA_1]: [DATA] - [DESCRIÇÃO]
- [MUDANÇA_2]: [DATA] - [DESCRIÇÃO]
- [MUDANÇA_3]: [DATA] - [DESCRIÇÃO]

## Decisões Ativas
- [DECISÃO_1]: [STATUS] - [DESCRIÇÃO]
- [DECISÃO_2]: [STATUS] - [DESCRIÇÃO]
- [DECISÃO_3]: [STATUS] - [DESCRIÇÃO]

## Próximos Passos
1. [PRÓXIMO_PASSO_1]
2. [PRÓXIMO_PASSO_2]
3. [PRÓXIMO_PASSO_3]

## Desafios Atuais
- [DESAFIO_1]: [DESCRIÇÃO]
- [DESAFIO_2]: [DESCRIÇÃO]
- [DESAFIO_3]: [DESCRIÇÃO]

## Progresso da Implementação
- [✓] [TAREFA_COMPLETADA_1]
- [✓] [TAREFA_COMPLETADA_2]
- [ ] [TAREFA_PENDENTE_1]
- [ ] [TAREFA_PENDENTE_2]

---

*Este documento captura o estado atual do trabalho e próximos passos imediatos.*
```

### Template progress.md
```markdown
# Rastreador de Progresso: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Status do Projeto
Completude Geral: [PORCENTAGEM]%

## O Que Funciona
- [FEATURE_1]: [STATUS_COMPLETUDE] - [NOTAS]
- [FEATURE_2]: [STATUS_COMPLETUDE] - [NOTAS]
- [FEATURE_3]: [STATUS_COMPLETUDE] - [NOTAS]

## O Que Está em Progresso
- [FEATURE_4]: [PORCENTAGEM_PROGRESSO]% - [NOTAS]
- [FEATURE_5]: [PORCENTAGEM_PROGRESSO]% - [NOTAS]
- [FEATURE_6]: [PORCENTAGEM_PROGRESSO]% - [NOTAS]

## O Que Falta Construir
- [FEATURE_7]: [PRIORIDADE] - [NOTAS]
- [FEATURE_8]: [PRIORIDADE] - [NOTAS]
- [FEATURE_9]: [PRIORIDADE] - [NOTAS]

## Problemas Conhecidos
- [PROBLEMA_1]: [SEVERIDADE] - [DESCRIÇÃO] - [STATUS]
- [PROBLEMA_2]: [SEVERIDADE] - [DESCRIÇÃO] - [STATUS]
- [PROBLEMA_3]: [SEVERIDADE] - [DESCRIÇÃO] - [STATUS]

## Marcos
- [MARCO_1]: [DATA_VENCIMENTO] - [STATUS]
- [MARCO_2]: [DATA_VENCIMENTO] - [STATUS]
- [MARCO_3]: [DATA_VENCIMENTO] - [STATUS]

---

*Este documento rastreia o que funciona, o que está em progresso, e o que falta construir.*
```

### Template state.md
```markdown
# Estado do Framework: [NOME_DO_PROJETO]
*Versão: 1.0*
*Criado: [DATA_ATUAL]*
*Última Atualização: [DATA_ATUAL]*

## Estado Atual do Projeto
PROJECT_PHASE=INITIALIZING
CURRENT_MODE=START
START_PHASE_STATUS=IN_PROGRESS
START_PHASE_STEP=1
INITIALIZATION_DATE=[DATA_HORA_ATUAL]

## Histórico de Estados
- [DATA_HORA]: PROJECT_PHASE=UNINITIATED
- [DATA_HORA]: PROJECT_PHASE=INITIALIZING, START_PHASE_STATUS=IN_PROGRESS

---

*Este arquivo mantém o estado atual do framework RIPER-Copilot.*
```

## TEMPLATES DE CUSTOM INSTRUCTIONS PARA GITHUB COPILOT

### Estrutura de Custom Instructions
**IMPORTANTE**: Os templates são organizados hierarquicamente em `.github/templates/custom-instructions/` para melhor organização, mas as custom instructions finais são **geradas em estrutura plana** para uso direto pelo GitHub Copilot:

**Templates (estrutura hierárquica):**
```
.github/templates/custom-instructions/
├── core/
│   ├── general.md                  # Template base para instruções gerais
│   └── project-setup.md            # Template base para configuração de projeto
├── patterns/
│   ├── backend.md                  # Template base para padrões backend
│   ├── frontend.md                 # Template base para padrões frontend
│   ├── database.md                 # Template base para padrões database
│   ├── iac.md                      # Template base para Infrastructure as Code
│   ├── testing.md                  # Template base para estratégias de teste
│   └── code-analysis.md            # Template base para análise de código
├── security/
│   └── security.md                 # Template base para diretrizes de segurança
└── workflow/
    ├── code-review.md              # Template base para processo de review
    └── development-workflow.md     # Template base para fluxo de desenvolvimento
```

**Custom Instructions Geradas (estrutura hierárquica mantida):**
```
custom-instructions/
├── core/
│   ├── general.md                  # Gerado de .github/templates/custom-instructions/core/general.md
│   └── project-setup.md            # Gerado de .github/templates/custom-instructions/core/project-setup.md
├── patterns/
│   ├── backend.md                  # Gerado de .github/templates/custom-instructions/patterns/backend.md (se detectado)
│   ├── frontend.md                 # Gerado de .github/templates/custom-instructions/patterns/frontend.md (se detectado)
│   ├── database.md                 # Gerado de .github/templates/custom-instructions/patterns/database.md (se detectado)
│   ├── iac.md                      # Gerado de .github/templates/custom-instructions/patterns/iac.md (se detectado)
│   ├── testing.md                  # Gerado de .github/templates/custom-instructions/patterns/testing.md
│   └── code-analysis.md            # Gerado de .github/templates/custom-instructions/patterns/code-analysis.md (se detectado)
├── security/
│   └── security.md                 # Gerado de .github/templates/custom-instructions/security/security.md
└── workflow/
    ├── code-review.md              # Gerado de .github/templates/custom-instructions/workflow/code-review.md
    └── development-workflow.md     # Gerado de .github/templates/custom-instructions/workflow/development-workflow.md
```

### Template `.github/templates/custom-instructions/core/general.md`
Instruções gerais do projeto que sempre são geradas, contendo:
- Contexto e filosofia de desenvolvimento
- Convenções de nomenclatura detectadas
- Estrutura do projeto analisada
- Tecnologias em uso
- Exemplos de código bem estruturado
- Antipadrões a evitar

### Template `.github/templates/custom-instructions/core/project-setup.md`
Sempre gerado, contendo:
- Configuração de ambiente de desenvolvimento
- Processo de build e deployment
- Gerenciamento de dependências
- Configuração de ferramentas e IDEs
- Setup inicial e onboarding

### Template `.github/templates/custom-instructions/patterns/backend.md` (Condicionalmente Gerado)
Gerado quando detectados indicadores de backend:
- Controllers, Services, Repositories
- APIs REST/GraphQL
- Frameworks de backend (Spring, Express, Django, FastAPI, etc.)
- ORMs/ODMs

### Template `.github/templates/custom-instructions/patterns/frontend.md` (Condicionalmente Gerado)
Gerado quando detectados indicadores de frontend:
- Componentes, Views, Templates
- Frameworks UI (React, Vue, Angular, etc.)
- Ferramentas de build (Webpack, Vite, etc.)
- Estratégias de estilização

### Template `.github/templates/custom-instructions/patterns/database.md` (Condicionalmente Gerado)
Gerado quando detectados indicadores de database:
- Migrações, Schemas
- ORMs/ODMs específicos
- Queries e optimization
- Modelagem de dados

### Template `.github/templates/custom-instructions/patterns/testing.md`
Sempre gerado, contendo:
- Filosofia e estratégias de teste
- Frameworks de teste detectados
- Padrões de organização de testes
- Mocking e test data

### Template `.github/templates/custom-instructions/patterns/code-analysis.md` (Condicionalmente Gerado)
Gerado quando detectado código complexo ou necessidade de refatoração:
- Análise estática de código
- Métricas de qualidade
- Gestão de dívida técnica
- Diretrizes de refatoração
- Integração com ferramentas de análise

### Template `.github/templates/custom-instructions/security/security.md`
Sempre gerado, contendo:
- Estratégias de autenticação/autorização
- Proteção de dados
- Prevenção de vulnerabilidades
- Compliance e auditoria

### Template `.github/templates/custom-instructions/workflow/code-review.md`
Sempre gerado, contendo:
- Processo de revisão de código
- Checklists de qualidade
- Diretrizes de feedback
- Padrões de aprovação
- Métricas de review

### Template `.github/templates/custom-instructions/workflow/development-workflow.md`
Sempre gerado, contendo:
- Fluxo de desenvolvimento
- Práticas de Git e versionamento
- CI/CD e automação
- Colaboração da equipe
- Qualidade de código

## PROCESSO DE GERAÇÃO PARA GITHUB COPILOT

### Análise Automática de Projeto
A IA analisa o projeto seguindo este processo estruturado:

1. **Detecção de Stack Tecnológico**
   - Analisar arquivos de configuração (package.json, pom.xml, requirements.txt, etc.)
   - Identificar extensões de arquivo (.js, .ts, .java, .py, .cs, etc.)
   - Detectar frameworks através de imports e dependências
   - Mapear linguagens para templates aplicáveis

2. **Seleção Inteligente de Templates**
   - Templates sempre gerados: general.md, testing.md, security.md
   - Templates condicionais baseados em detecção:
     - backend.md: se detectar APIs, controllers, services, repositories
     - frontend.md: se detectar components, views, UI frameworks
     - database.md: se detectar database, migrations, ORMs

3. **Preenchimento Contextual**
   - Extrair informações dos arquivos de memória (projectbrief.md, systemPatterns.md, techContext.md)
   - Analisar código real para identificar padrões e convenções
   - Gerar exemplos baseados no codebase existente
   - Identificar antipadrões específicos do projeto

4. **Personalização para GitHub Copilot**
   - Adaptar linguagem para sugestões de código
   - Incluir contexto específico do projeto
   - Configurar exemplos práticos e relevantes
   - Definir diretrizes claras para geração de código

### Detecção Automática de Tecnologias
O sistema detecta automaticamente:

**Java:**
- Arquivos: .java, pom.xml, build.gradle
- Frameworks: Spring Boot, JUnit, Hibernate

**TypeScript/JavaScript:**
- Arquivos: .ts, .tsx, .js, package.json, tsconfig.json
- Frameworks: React, Vue, Angular, Express, Jest

**C#:**
- Arquivos: .cs, *.csproj, *.sln, appsettings.json
- Frameworks: ASP.NET Core, Entity Framework

**Python:**
- Arquivos: .py, requirements.txt, setup.py, pyproject.toml
- Frameworks: Django, Flask, FastAPI, pytest

### Exemplo de Resultado Final
Após a execução do processo, o projeto terá:
- Sistema de custom instructions completo em `custom-instructions/` seguindo estrutura hierárquica
- Templates preenchidos com conteúdo específico do projeto
- Instruções adaptadas para GitHub Copilot
- Exemplos reais extraídos do codebase
- Convenções e padrões documentados
- Diretrizes claras para geração de código

## TRANSIÇÃO PARA WORKFLOW RIPER

Uma vez que todos os sete passos estejam completados:

1. Verificar que todos arquivos de memória estão propriamente criados e populados
2. Verificar que todas as custom instructions estão geradas e configuradas
3. Atualizar state.md com:
   - PROJECT_PHASE = "DEVELOPMENT"
   - START_PHASE_STATUS = "COMPLETED"
   - START_PHASE_STEP = 7
   - INITIALIZATION_DATE = [data/hora atual]
4. Transicionar automaticamente para modo RESEARCH
5. Informar o usuário: "Inicialização do projeto completa. Entrando no modo RESEARCH para começar desenvolvimento."

## CHECKLIST DE ENTREGÁVEIS

No final da fase START, garantir que os seguintes estejam completos:

**Banco de Memória:**
- [ ] Requisitos do projeto documentados em projectbrief.md
- [ ] Stack de tecnologia selecionado e documentado em techContext.md
- [ ] Arquitetura do sistema definida em systemPatterns.md
- [ ] Banco de Memória inicializado com todos arquivos principais
- [ ] Tarefas iniciais documentadas em progress.md
- [ ] Estado do projeto atualizado em state.md

**Projeto e Ambiente:**
- [ ] Scaffold do projeto criado
- [ ] Ambiente de desenvolvimento configurado e documentado

**Sistema de Custom Instructions para GitHub Copilot:**
- [ ] Estrutura `custom-instructions/` criada no projeto seguindo estrutura hierárquica
- [ ] Linguagens e frameworks detectados automaticamente
- [ ] Templates obrigatórios gerados: `core/general.md`, `core/project-setup.md`, `patterns/testing.md`, `security/security.md`, `workflow/code-review.md`, `workflow/development-workflow.md`
- [ ] Templates condicionais aplicados conforme detecção: `patterns/backend.md`, `patterns/frontend.md`, `patterns/database.md`, `patterns/code-analysis.md`
- [ ] Conteúdo específico extraído dos arquivos de memória (projectbrief.md, systemPatterns.md, techContext.md)
- [ ] Convenções de nomenclatura reais detectadas e documentadas
- [ ] Exemplos reais do codebase incluídos nas instruções
- [ ] Antipadrões específicos do projeto identificados e documentados
- [ ] Instruções adaptadas para uso com GitHub Copilot
- [ ] Sistema de custom instructions testado e funcional

Uma vez que todos itens estejam marcados, o sistema automaticamente transicionará para o workflow RIPER.

Este arquivo guia a inicialização do projeto através da fase START. Será automaticamente arquivado uma vez que inicialização esteja completa.

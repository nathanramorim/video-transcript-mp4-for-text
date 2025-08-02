description: MUST BE APPLIED WHEN working on Infrastructure as Code (IaC) including Terraform, CloudFormation, ARM templates, Ansible, Pulumi, CDK, and infrastructure automation. Covers IaC-specific patterns including resource management, state handling, security practices, and deployment strategies.
applyTo: "**/terraform/**/*,**/cloudformation/**/*,**/arm/**/*,**/ansible/**/*,**/pulumi/**/*,**/cdk/**/*,**/*.tf,**/*.tfvars,**/*.yaml,**/*.yml,**/*.json,**/helm/**/*,**/k8s/**/*,**/kubernetes/**/*,**/infrastructure/**/*,**/infra/**/*,**/iac/**/*,**/*.bicep,**/*.ps1,**/scripts/**/*"
alwaysApply: false

# Infrastructure as Code Guidelines: [NOME_DO_PROJETO]

## IaC Philosophy
<iac_philosophy>
**Primary IaC Tool**: [FERRAMENTA_IAC_PRINCIPAL_DETECTADA]
**Cloud Provider**: [PROVEDOR_CLOUD_DETECTADO]
**Deployment Strategy**: [ESTRATEGIA_DEPLOYMENT_DETECTADA]

### IaC Principles
- Infrastructure as Code (declarative approach)
- Version control for all infrastructure definitions
- Immutable infrastructure patterns
- GitOps workflow for infrastructure changes
- Environment parity and consistency
- Automated testing and validation
- State management and drift detection
- Security by design and least privilege

### Quality Standards
- Infrastructure security compliance: [COMPLIANCE_DETECTADO]
- Resource tagging consistency: [ESTRATEGIA_TAGS_DETECTADA]
- Cost optimization practices: [OTIMIZACAO_CUSTO_DETECTADA]
- High availability design: [DESIGN_HA_DETECTADO]
- Disaster recovery strategy: [ESTRATEGIA_DR_DETECTADA]

[FILOSOFIA_IAC_BASEADA_PROJECTBRIEF]
</iac_philosophy>

## IaC Tool-Specific Guidelines

### Terraform Configuration
<terraform_guidelines>
**Terraform Version**: [VERSAO_TERRAFORM_DETECTADA]
**Provider Versions**: [VERSOES_PROVIDERS_DETECTADAS]

#### File Organization
```hcl
# [ESTRUTURA_TERRAFORM_DETECTADA]
# Example structure:
# main.tf           - Main configuration
# variables.tf      - Input variables
# outputs.tf        - Output values
# versions.tf       - Provider versions
# terraform.tfvars  - Variable values
# modules/          - Reusable modules
```

#### Naming Conventions
- **Resources**: [CONVENCAO_RECURSOS_TERRAFORM]
- **Variables**: [CONVENCAO_VARIAVEIS_TERRAFORM]
- **Outputs**: [CONVENCAO_OUTPUTS_TERRAFORM]
- **Modules**: [CONVENCAO_MODULOS_TERRAFORM]
- **Files**: [CONVENCAO_ARQUIVOS_TERRAFORM]

#### Resource Configuration Patterns
```hcl
# [EXEMPLO_RECURSO_TERRAFORM_DETECTADO]

# Standard resource pattern
resource "provider_resource_type" "logical_name" {
  # Required parameters first
  name                = var.resource_name
  location           = var.location
  resource_group_name = azurerm_resource_group.main.name
  
  # Optional parameters
  tags = local.common_tags
  
  # Lifecycle management
  lifecycle {
    prevent_destroy = true
    ignore_changes  = [tags]
  }
}
```

#### Variable Definitions
```hcl
# [EXEMPLO_VARIAVEIS_TERRAFORM_DETECTADAS]

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

#### Module Structure
```hcl
# [ESTRUTURA_MODULOS_TERRAFORM_DETECTADA]
```
</terraform_guidelines>

### CloudFormation Templates
<cloudformation_guidelines>
**Template Format**: [FORMATO_CFN_DETECTADO] (JSON/YAML)
**Stack Naming**: [CONVENCAO_STACKS_CFN]

#### Template Structure
```yaml
# [EXEMPLO_TEMPLATE_CFN_DETECTADO]

AWSTemplateFormatVersion: '2010-09-09'
Description: '[DESCRICAO_STACK_DETECTADA]'

Parameters:
  Environment:
    Type: String
    AllowedValues: [dev, staging, prod]
    Description: Environment name

Resources:
  # Resource definitions following naming convention
  
Outputs:
  # Output definitions for cross-stack references
```

#### Parameter Conventions
- **Naming**: [CONVENCAO_PARAMETROS_CFN]
- **Types**: [TIPOS_PARAMETROS_CFN]
- **Validation**: [VALIDACAO_PARAMETROS_CFN]

#### Resource Naming
```yaml
# [PADROES_RECURSOS_CFN_DETECTADOS]
```
</cloudformation_guidelines>

### Kubernetes/Helm Configuration
<kubernetes_guidelines>
**Kubernetes Version**: [VERSAO_K8S_DETECTADA]
**Helm Version**: [VERSAO_HELM_DETECTADA]

#### Manifest Organization
```yaml
# [ESTRUTURA_K8S_DETECTADA]

# Namespace definition
apiVersion: v1
kind: Namespace
metadata:
  name: [NAMESPACE_DETECTADO]
  labels:
    environment: [AMBIENTE_DETECTADO]
```

#### Helm Chart Structure
```
# [ESTRUTURA_HELM_DETECTADA]
charts/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-prod.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── configmap.yaml
```

#### Resource Configuration
```yaml
# [EXEMPLO_RECURSOS_K8S_DETECTADOS]
```
</kubernetes_guidelines>

### Ansible Playbooks
<ansible_guidelines>
**Ansible Version**: [VERSAO_ANSIBLE_DETECTADA]
**Inventory Structure**: [ESTRUTURA_INVENTORY_DETECTADA]

#### Playbook Organization
```yaml
# [ESTRUTURA_PLAYBOOKS_DETECTADA]

# Example playbook structure
---
- name: [NOME_PLAYBOOK_DETECTADO]
  hosts: [HOSTS_DETECTADOS]
  become: yes
  vars:
    # Variable definitions
  
  tasks:
    # Task definitions
```

#### Role Structure
```
# [ESTRUTURA_ROLES_DETECTADA]
roles/
├── common/
│   ├── tasks/main.yml
│   ├── handlers/main.yml
│   ├── vars/main.yml
│   └── defaults/main.yml
```
</ansible_guidelines>

## Infrastructure Security
<infrastructure_security>
### Security Principles
- **Least Privilege**: Grant minimum required permissions
- **Defense in Depth**: Multiple security layers
- **Zero Trust**: Never trust, always verify
- **Encryption**: Data at rest and in transit
- **Network Segmentation**: Isolate components
- **Audit Logging**: Track all infrastructure changes
- **Compliance**: Follow regulatory requirements
- **Vulnerability Management**: Regular security scanning

### Access Control Patterns
```hcl
# [EXEMPLOS_CONTROLE_ACESSO_DETECTADOS]

# IAM Role example
resource "aws_iam_role" "service_role" {
  name = "[NOME_ROLE_DETECTADO]"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "[SERVICO_DETECTADO]"
        }
      }
    ]
  })
  
  tags = local.security_tags
}
```

### Network Security
```hcl
# [EXEMPLOS_SEGURANCA_REDE_DETECTADOS]

# Security Group example
resource "aws_security_group" "application" {
  name_prefix = "[PREFIXO_SG_DETECTADO]"
  vpc_id      = var.vpc_id
  
  # Ingress rules - restrictive by default
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.allowed_cidr]
  }
  
  # Egress rules - explicit allow
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = merge(local.common_tags, {
    Name = "[NOME_SG_DETECTADO]"
    Type = "Application"
  })
}
```

### Secrets Management
```hcl
# [EXEMPLOS_GERENCIAMENTO_SECRETS_DETECTADOS]

# Key Vault/Secrets Manager integration
data "aws_secretsmanager_secret" "database_password" {
  name = "[NOME_SECRET_DETECTADO]"
}

data "aws_secretsmanager_secret_version" "database_password" {
  secret_id = data.aws_secretsmanager_secret.database_password.id
}
```
</infrastructure_security>

## State Management
<state_management>
### State Storage Strategy
**Backend Type**: [TIPO_BACKEND_STATE_DETECTADO]
**State Location**: [LOCALIZACAO_STATE_DETECTADA]
**Locking Mechanism**: [MECANISMO_LOCK_DETECTADO]

#### Terraform State Configuration
```hcl
# [CONFIGURACAO_BACKEND_DETECTADA]

terraform {
  backend "[TIPO_BACKEND]" {
    bucket         = "[BUCKET_STATE_DETECTADO]"
    key            = "[CHAVE_STATE_DETECTADA]"
    region         = "[REGIAO_DETECTADA]"
    encrypt        = true
    dynamodb_table = "[TABELA_LOCK_DETECTADA]"
  }
}
```

#### State File Security
- **Encryption**: State files encrypted at rest
- **Access Control**: Limited access to state storage
- **Versioning**: State file versioning enabled
- **Backup**: Regular state file backups
- **Audit**: State access logging

### State Management Best Practices
- **Remote State**: Never store state locally in production
- **State Locking**: Prevent concurrent modifications
- **State Isolation**: Separate state per environment
- **State Import**: Import existing resources properly
- **State Refresh**: Regular state refresh and drift detection
</state_management>

## Environment Management
<environment_management>
### Environment Strategy
**Environment Types**: [TIPOS_AMBIENTE_DETECTADOS]
**Promotion Strategy**: [ESTRATEGIA_PROMOCAO_DETECTADA]

#### Environment Configuration
```hcl
# [CONFIGURACAO_AMBIENTES_DETECTADA]

# Environment-specific variables
locals {
  environments = {
    dev = {
      instance_type = "t3.micro"
      min_capacity  = 1
      max_capacity  = 2
    }
    staging = {
      instance_type = "t3.small"
      min_capacity  = 2
      max_capacity  = 4
    }
    prod = {
      instance_type = "t3.medium"
      min_capacity  = 3
      max_capacity  = 10
    }
  }
  
  current_env = local.environments[var.environment]
}
```

#### Environment Parity
- **Configuration**: Consistent configuration across environments
- **Infrastructure**: Same infrastructure patterns
- **Deployment**: Identical deployment processes
- **Testing**: Environment-specific testing strategies
- **Monitoring**: Consistent monitoring and alerting

### Resource Naming and Tagging
```hcl
# [ESTRATEGIA_NOMES_TAGS_DETECTADA]

locals {
  common_tags = {
    Environment   = var.environment
    Project      = "[NOME_PROJETO_DETECTADO]"
    Owner        = "[OWNER_DETECTADO]"
    CostCenter   = "[COST_CENTER_DETECTADO]"
    CreatedBy    = "terraform"
    CreatedDate  = timestamp()
  }
  
  name_prefix = "[PREFIXO_RECURSOS_DETECTADO]"
}
```
</environment_management>

## Deployment and CI/CD Integration
<deployment_cicd>
### Deployment Pipeline
**CI/CD Platform**: [PLATAFORMA_CICD_DETECTADA]
**Pipeline Strategy**: [ESTRATEGIA_PIPELINE_DETECTADA]

#### Pipeline Stages
1. **Validation**: Syntax and configuration validation
2. **Security Scanning**: Security and compliance checks
3. **Planning**: Infrastructure planning and review
4. **Testing**: Infrastructure testing and validation
5. **Deployment**: Infrastructure provisioning
6. **Verification**: Post-deployment verification

#### Pipeline Configuration
```yaml
# [CONFIGURACAO_PIPELINE_DETECTADA]

# Example GitHub Actions workflow
name: Infrastructure Deployment
on:
  push:
    branches: [main]
    paths: ['infrastructure/**']
  pull_request:
    paths: ['infrastructure/**']

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v2
        with:
          terraform_version: [VERSAO_TERRAFORM]
      
      - name: Terraform Plan
        run: terraform plan
        
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve
```

### Deployment Strategies
- **Blue-Green**: Zero-downtime deployments
- **Rolling**: Gradual infrastructure updates
- **Canary**: Risk-reduced deployments
- **Immutable**: Complete infrastructure replacement

### Rollback Procedures
```bash
# [PROCEDIMENTOS_ROLLBACK_DETECTADOS]

# Terraform rollback example
terraform plan -destroy -target=resource.problematic_resource
terraform apply -target=resource.problematic_resource
```
</deployment_cicd>

## Monitoring and Observability
<monitoring_observability>
### Infrastructure Monitoring
**Monitoring Platform**: [PLATAFORMA_MONITORING_DETECTADA]
**Metrics Collection**: [COLETA_METRICAS_DETECTADA]
**Alerting Strategy**: [ESTRATEGIA_ALERTAS_DETECTADA]

#### Key Metrics
- **Resource Utilization**: CPU, memory, storage, network
- **Cost Metrics**: Resource costs and budget tracking
- **Security Metrics**: Security compliance and violations
- **Performance Metrics**: Response times and throughput
- **Availability Metrics**: Uptime and service availability

#### Alerting Configuration
```hcl
# [CONFIGURACAO_ALERTAS_DETECTADA]

resource "aws_cloudwatch_metric_alarm" "high_cpu" {
  alarm_name          = "[NOME_ALARME_DETECTADO]"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "300"
  statistic           = "Average"
  threshold           = "80"
  alarm_description   = "This metric monitors ec2 cpu utilization"
  
  dimensions = {
    InstanceId = aws_instance.main.id
  }
  
  alarm_actions = [aws_sns_topic.alerts.arn]
}
```

### Logging Strategy
- **Centralized Logging**: All infrastructure logs in one place
- **Log Retention**: Appropriate log retention policies
- **Log Security**: Secure log storage and access
- **Log Analysis**: Automated log analysis and insights
</monitoring_observability>

## Testing and Validation
<testing_validation>
### Infrastructure Testing
**Testing Framework**: [FRAMEWORK_TESTE_IAC_DETECTADO]
**Testing Strategy**: [ESTRATEGIA_TESTE_IAC_DETECTADA]

#### Test Types
- **Unit Tests**: Individual resource configuration tests
- **Integration Tests**: Multi-resource interaction tests
- **Compliance Tests**: Security and compliance validation
- **Performance Tests**: Infrastructure performance validation
- **Disaster Recovery Tests**: DR procedure validation

#### Test Examples
```hcl
# [EXEMPLOS_TESTES_IAC_DETECTADOS]

# Terratest example
func TestTerraformAzureExample(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../",
        Vars: map[string]interface{}{
            "environment": "test",
        },
    }
    
    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)
    
    // Validation logic
}
```

#### Policy as Code
```rego
# [EXEMPLOS_POLICY_CODE_DETECTADOS]

# Open Policy Agent (OPA) example
package terraform.security

deny[msg] {
    resource := input.resource_changes[_]
    resource.type == "aws_s3_bucket"
    not resource.change.after.encryption
    
    msg := "S3 buckets must be encrypted"
}
```
</testing_validation>

## Cost Optimization
<cost_optimization>
### Cost Management Strategy
**Cost Tracking**: [ESTRATEGIA_CUSTO_DETECTADA]
**Budget Alerts**: [ALERTAS_ORCAMENTO_DETECTADOS]
**Resource Optimization**: [OTIMIZACAO_RECURSOS_DETECTADA]

#### Cost Control Patterns
```hcl
# [PADROES_CONTROLE_CUSTO_DETECTADOS]

# Auto-scaling configuration
resource "aws_autoscaling_group" "main" {
  name                = "[NOME_ASG_DETECTADO]"
  min_size            = var.min_capacity
  max_size            = var.max_capacity
  desired_capacity    = var.desired_capacity
  
  # Cost optimization through scheduling
  tag {
    key                 = "Schedule"
    value               = "[AGENDA_DETECTADA]"
    propagate_at_launch = true
  }
}
```

#### Resource Tagging for Cost
```hcl
# [ESTRATEGIA_TAGS_CUSTO_DETECTADA]

locals {
  cost_tags = {
    CostCenter    = "[COST_CENTER_DETECTADO]"
    Project       = "[PROJETO_DETECTADO]"
    Environment   = var.environment
    Owner         = "[OWNER_DETECTADO]"
    Chargeback    = "[CHARGEBACK_DETECTADO]"
  }
}
```

### Resource Lifecycle Management
- **Right-sizing**: Appropriate resource sizing
- **Reserved Instances**: Cost-effective instance reservations
- **Spot Instances**: Cost-optimized compute resources
- **Automated Cleanup**: Unused resource identification and removal
- **Scheduled Operations**: Cost-effective resource scheduling
</cost_optimization>

## Documentation and Standards
<documentation_standards>
### Documentation Requirements
- **Architecture Diagrams**: Visual infrastructure representation
- **README Files**: Setup and usage instructions
- **Change Logs**: Infrastructure change tracking
- **Runbooks**: Operational procedures
- **Disaster Recovery Plans**: DR procedures and contacts

#### Documentation Templates
```markdown
# [TEMPLATE_DOCUMENTACAO_DETECTADO]

# Infrastructure Module: [NOME_MODULO]

## Overview
[DESCRICAO_MODULO]

## Usage
```hcl
module "[NOME_MODULO]" {
  source = "./modules/[NOME_MODULO]"
  
  # Required variables
  variable1 = "value1"
  variable2 = "value2"
}
```

## Requirements
- [REQUISITO_1]
- [REQUISITO_2]

## Providers
- [PROVIDER_1]: [VERSAO_1]
- [PROVIDER_2]: [VERSAO_2]
```

### Code Quality Standards
- **Linting**: Infrastructure code linting
- **Formatting**: Consistent code formatting
- **Comments**: Comprehensive inline documentation
- **Modularity**: Reusable infrastructure modules
- **Version Control**: Proper branching and tagging strategies
</documentation_standards>

## Anti-Patterns to Avoid
<anti_patterns>
### Common IaC Anti-Patterns
- **Manual Infrastructure Changes**: Always use IaC for changes
- **Hardcoded Values**: Use variables and parameters
- **Monolithic Configurations**: Break into manageable modules
- **Missing State Management**: Always use remote state
- **Inadequate Testing**: Test infrastructure changes
- **Poor Secret Handling**: Never hardcode secrets
- **Inconsistent Naming**: Follow naming conventions
- **Lack of Documentation**: Document all infrastructure decisions
- **Missing Monitoring**: Monitor infrastructure health
- **Ignoring Security**: Security should be built-in, not added later

### Terraform-Specific Anti-Patterns
```hcl
# ❌ BAD: Hardcoded values
resource "aws_instance" "web" {
  ami           = "ami-12345678"  # Don't hardcode AMI IDs
  instance_type = "t2.micro"     # Don't hardcode instance types
}

# ✅ GOOD: Use variables
resource "aws_instance" "web" {
  ami           = data.aws_ami.latest.id
  instance_type = var.instance_type
}
```

### CloudFormation Anti-Patterns
```yaml
# ❌ BAD: No parameters or outputs
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-hardcoded-bucket-name

# ✅ GOOD: Parameterized with outputs
Parameters:
  BucketName:
    Type: String
    Description: Name for the S3 bucket

Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketName

Outputs:
  BucketName:
    Description: Name of the created bucket
    Value: !Ref MyBucket
```
</anti_patterns>

---

**Notes for Template Processing:**
- Replace `[FERRAMENTA_IAC_PRINCIPAL_DETECTADA]` with detected IaC tool (Terraform, CloudFormation, etc.)
- Replace `[PROVEDOR_CLOUD_DETECTADO]` with detected cloud provider (AWS, Azure, GCP)
- Replace `[VERSAO_TERRAFORM_DETECTADA]` with detected Terraform version from configuration files
- Replace `[ESTRUTURA_TERRAFORM_DETECTADA]` with actual project terraform directory structure
- Replace `[CONFIGURACAO_PIPELINE_DETECTADA]` with detected CI/CD pipeline configuration
- Replace code examples with actual patterns found in the project codebase
- Fill bracketed placeholders with project-specific values during template generation 
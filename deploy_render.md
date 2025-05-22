# Instruções para Deploy no Render

Este documento contém instruções detalhadas para fazer o deploy do FC Statistics na plataforma Render.

## Pré-requisitos

- Uma conta na plataforma Render (https://render.com)
- Acesso ao código-fonte do projeto FC Statistics

## Ficheiros de Configuração

Os seguintes ficheiros foram preparados para facilitar o deploy:

1. **requirements.txt**: Lista todas as dependências do projeto
2. **Procfile**: Define o comando para iniciar a aplicação
3. **runtime.txt**: Especifica a versão do Python a ser utilizada

## Passos para Deploy

### 1. Criar um Novo Serviço Web no Render

1. Faça login na sua conta Render
2. Clique em "New +" e selecione "Web Service"
3. Conecte ao repositório Git onde o código está hospedado ou use a opção de deploy manual

### 2. Configurar o Serviço

Preencha os seguintes campos:

- **Name**: FC Statistics
- **Environment**: Python
- **Region**: Escolha a região mais próxima de você
- **Branch**: main (ou a branch que contém o código)
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn -w 4 -b 0.0.0.0:$PORT src.main:app`

### 3. Configurar Variáveis de Ambiente

Adicione as seguintes variáveis de ambiente:

- `PORT`: 8000
- `PYTHON_VERSION`: 3.11.0
- `FLASK_ENV`: production

### 4. Opções Avançadas

- **Auto-Deploy**: Ative esta opção se desejar que o Render faça deploy automático quando houver novos commits
- **Health Check Path**: `/` (para verificar se a aplicação está funcionando)

### 5. Criar o Serviço

Clique em "Create Web Service" para iniciar o processo de deploy.

## Verificação do Deploy

Após o deploy ser concluído (pode levar alguns minutos), o Render fornecerá um URL para acessar a aplicação, geralmente no formato:

```
https://fc-statistics.onrender.com
```

Acesse este URL para verificar se a aplicação está funcionando corretamente.

## Solução de Problemas

Se encontrar problemas durante o deploy, verifique:

1. **Logs**: Acesse os logs do serviço no painel do Render para identificar erros
2. **Dependências**: Certifique-se de que todas as dependências estão listadas no requirements.txt
3. **Variáveis de Ambiente**: Verifique se todas as variáveis necessárias foram configuradas

## Manutenção

Para atualizar a aplicação após o deploy inicial:

1. Faça as alterações no código
2. Commit e push para o repositório (se estiver usando auto-deploy)
3. Ou faça deploy manual através do painel do Render

## Notas Importantes

- O plano gratuito do Render pode colocar a aplicação em modo de suspensão após períodos de inatividade
- O primeiro acesso após um período de inatividade pode ser mais lento
- Para uso em produção, considere atualizar para um plano pago

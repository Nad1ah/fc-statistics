# Documentação do Projeto FC Statistics

## Visão Geral

O FC Statistics é um blog e canal Telegram dedicado a apostas desportivas de futebol, com foco em análise estatística e probabilística dos principais mercados: golos, vencedor, cantos e cartões. O projeto foi desenvolvido com um design clean e sofisticado, oferecendo publicações diárias de análises e sugestões de apostas.

## Estrutura do Projeto

O projeto foi desenvolvido utilizando o framework Flask, com a seguinte estrutura:

```
fc_statistics/
├── src/
│   ├── main.py                 # Ponto de entrada da aplicação
│   ├── models/                 # Modelos de dados
│   ├── routes/                 # Rotas e controladores
│   │   ├── api/                # APIs para dados
│   │   │   └── data.py         # API de dados estatísticos
│   │   └── views/              # Páginas e visualizações
│   │       ├── main.py         # Páginas principais
│   │       ├── telegram.py     # Integração com Telegram
│   │       └── betting.py      # Sugestões de apostas
│   ├── static/                 # Arquivos estáticos
│   │   ├── css/                # Estilos
│   │   │   └── style.css       # Estilos principais
│   │   ├── js/                 # JavaScript
│   │   │   └── main.js         # Scripts principais
│   │   └── img/                # Imagens
│   └── templates/              # Templates HTML
│       ├── index.html          # Página inicial
│       ├── reports.html        # Relatórios diários
│       ├── market_analysis.html # Análise de mercados
│       ├── odds_comparison.html # Comparação de odds
│       ├── statistics.html     # Estatísticas históricas
│       ├── betting_suggestions.html # Sugestões de apostas
│       ├── telegram_config.html # Configuração do Telegram
│       └── telegram_preview.html # Pré-visualização do Telegram
├── modelo_relatorio_diario.md  # Modelo para relatórios diários
└── requirements.txt            # Dependências do projeto
```

## Funcionalidades Implementadas

### 1. Blog FC Statistics

- **Página Inicial**: Apresenta destaques do dia, últimas análises e sugestões de apostas.
- **Relatórios Diários**: Publicações diárias com análises detalhadas dos jogos.
- **Análise de Mercados**: Páginas específicas para análise de golos, vencedor, cantos e cartões.
- **Comparação de Odds**: Ferramenta para comparar odds entre diferentes casas de apostas.
- **Estatísticas Históricas**: Base de dados com estatísticas históricas e filtros avançados.
- **Sugestões de Apostas**: Sistema automático de sugestões baseado em valor estatístico.

### 2. Integração com Telegram

- **Configuração do Canal**: Interface para configurar e gerenciar o canal Telegram.
- **Publicação Manual**: Sistema para publicação manual de posts no canal.
- **Geração de Relatórios**: Geração automática de relatórios diários e semanais.
- **Pré-visualização**: Ferramenta de pré-visualização de posts antes da publicação.

### 3. Sistema de Sugestões Automáticas

- **Cálculo de Probabilidades**: Algoritmo para cálculo de probabilidades baseado em dados estatísticos.
- **Identificação de Valor**: Sistema para identificar apostas com valor positivo esperado.
- **Justificativas**: Geração automática de justificativas para as sugestões.
- **Classificação por Confiança**: Classificação das sugestões por nível de confiança.

## Instruções de Uso

### Iniciar o Blog

1. Navegue até a pasta do projeto:
   ```
   cd /home/ubuntu/projeto_apostas/fc_statistics
   ```

2. Ative o ambiente virtual:
   ```
   source venv/bin/activate
   ```

3. Inicie o servidor Flask:
   ```
   python src/main.py
   ```

4. Acesse o blog em seu navegador:
   ```
   http://localhost:5000
   ```

### Publicação de Relatórios Diários

Devido à desativação temporária de tarefas agendadas, a publicação de relatórios diários deve ser feita manualmente seguindo estas etapas:

1. Acesse a página de Relatórios Diários no blog.
2. Clique em "Novo Relatório".
3. Utilize o modelo de relatório diário como base (disponível em `modelo_relatorio_diario.md`).
4. Preencha os dados atualizados para o dia.
5. Salve o relatório no blog.

### Publicação no Canal Telegram

1. Acesse a página de Configuração do Telegram no blog.
2. Na seção "Publicar no Canal", selecione "Relatório Diário".
3. Clique em "Gerar Relatório" para criar automaticamente o conteúdo.
4. Revise e edite o conteúdo conforme necessário.
5. Clique em "Publicar Agora" para enviar ao canal Telegram.

### Geração de Sugestões de Apostas

1. Acesse a página de Sugestões de Apostas no blog.
2. Selecione os filtros desejados (liga, mercado, data).
3. Clique em "Gerar Sugestões".
4. Revise as sugestões geradas e suas justificativas.
5. Para incluir as sugestões no relatório diário, selecione-as e clique em "Adicionar ao Relatório".

## Limitações e Considerações

### Publicação Automática

A publicação automática de relatórios está temporariamente desativada. Todos os relatórios devem ser publicados manualmente seguindo as instruções acima. Esta limitação será resolvida em uma atualização futura.

### Dados Estatísticos

Os dados estatísticos utilizados para cálculo de probabilidades e sugestões são simulados. Em uma implementação completa, estes dados seriam obtidos de APIs externas ou de um banco de dados atualizado regularmente.

### Personalização do Canal Telegram

Para personalizar o canal Telegram:

1. Crie um canal no aplicativo Telegram.
2. Defina o nome "FC Statistics" e uma descrição adequada.
3. Configure a privacidade do canal conforme desejado.
4. Copie o link do canal e insira-o na página de Configuração do Telegram no blog.

## Próximos Passos e Melhorias Futuras

1. **Automação de Publicação**: Implementar sistema de publicação automática de relatórios.
2. **Integração com APIs de Dados**: Conectar com APIs externas para obter dados estatísticos reais.
3. **Sistema de Usuários**: Adicionar sistema de login e perfis de usuário.
4. **Histórico de Desempenho**: Implementar rastreamento de desempenho das sugestões.
5. **Notificações em Tempo Real**: Adicionar notificações para eventos importantes durante os jogos.

## Suporte e Contato

Para suporte ou dúvidas sobre o projeto, entre em contato através do canal Telegram ou da seção "Sobre" no blog.

---

© 2025 FC Statistics. Todos os direitos reservados.

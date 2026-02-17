# RH Analytics - Previsão de Performance de Funcionários

Sistema de análise preditiva de performance de funcionários utilizando Machine Learning com Python e Excel.

## 📋 Descrição

Este projeto implementa um modelo de Machine Learning para prever a performance de funcionários com base em variáveis como idade, tempo de empresa, cargo, avaliação do gestor, faltas e horas de treinamento.

## 🚀 Funcionalidades

- **Treinamento de Modelo**: Treina um modelo Random Forest com dados históricos
- **Previsão de Performance**: Realiza previsões para novos funcionários
- **Análise de Importância**: Identifica as variáveis mais relevantes para a previsão
- **Integração com Excel**: Leitura e escrita de dados em planilhas Excel

## 📁 Estrutura do Projeto

```
.
├── rh_analytics.py              # Script principal
├── requirements.txt             # Dependências do projeto
├── dados_historicos/            # Dados históricos para treinamento
│   └── dados_funcionarios.xlsx
├── novos_dados/                 # Novos dados para previsão
│   └── novos_funcionarios.xlsx
├── previsoes/                   # Resultados das previsões
│   └── resultado_previsao.xlsx
└── modelo/                      # Modelo treinado
    └── modelo_rh_performance.pkl
```

## 🔧 Instalação

1. Clone o repositório
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 💻 Uso

Execute o script principal:

```bash
python rh_analytics.py
```

O script irá:
1. Verificar se existe um modelo treinado
2. Carregar o modelo existente ou treinar um novo
3. Realizar previsões nos novos dados
4. Salvar os resultados em `previsoes/resultado_previsao.xlsx`

## 📊 Variáveis Utilizadas

**Variáveis Preditoras:**
- Idade
- Tempo de Empresa
- Cargo
- Avaliação do Gestor
- Faltas
- Horas de Treinamento

**Variável Alvo:**
- Performance (classificação categórica)

## 🛠️ Tecnologias

- **Python 3.11 (ou superior)**
- **Pandas**: Manipulação de dados
- **Scikit-learn**: Machine Learning
- **OpenPyXL**: Manipulação de arquivos Excel
- **Joblib**: Serialização de modelos

## 📝 Requisitos

- Python 3.11+
- Bibliotecas listadas em `requirements.txt`

## 📄 Formato dos Dados

Os arquivos Excel devem conter as seguintes colunas:
- Idade
- TempoEmpresa
- Cargo
- AvaliaçãoGestor
- Faltas
- HorasTreinamento
- Performance (apenas para dados históricos)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📜 Licença

Este projeto é de código aberto e está disponível para uso educacional e comercial.

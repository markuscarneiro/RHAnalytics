# RH Analytics - Previsão de Performance de Funcionários

Sistema inteligente de análise preditiva que utiliza Random Forest para classificar e prever a performance de funcionários, integrando Machine Learning com Excel para facilitar a tomada de decisão em recursos humanos.

## 📋 Descrição

Este projeto implementa um modelo de Machine Learning baseado em **Random Forest** para prever a performance de funcionários com base em variáveis como idade, tempo de empresa, cargo, avaliação do gestor, faltas e horas de treinamento. O sistema automatiza a análise de recursos humanos, permitindo que gestores identifiquem antecipadamente funcionários de alto e baixo desempenho.

## 🚀 Funcionalidades

- **Treinamento Automatizado**: Treina um modelo Random Forest (100 árvores) com dados históricos
- **Previsão Inteligente**: Classifica automaticamente a performance de novos funcionários
- **Análise de Importância**: Identifica e rankeia as variáveis mais relevantes para a previsão
- **Reutilização de Modelo**: Salva e reutiliza modelos treinados para previsões futuras
- **Integração com Excel**: Leitura e escrita automática de dados em planilhas Excel
- **Ensemble Learning**: Combina múltiplas árvores de decisão para maior precisão

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
3. Exibir a importância de cada variável para a previsão
4. Realizar previsões nos novos dados usando as 100 árvores do Random Forest
5. Salvar os resultados em `previsoes/resultado_previsao.xlsx`

**Exemplo de Saída:**
```
Importância das Variáveis Para a Previsão da Performance:

AvaliaçãoGestor: 0.3245
HorasTreinamento: 0.2156
TempoEmpresa: 0.1789
Idade: 0.1234
Faltas: 0.0987
Cargo: 0.0589
```

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

## 🤖 Modelo de Machine Learning

### Random Forest Classifier

O projeto utiliza o algoritmo **Random Forest** (Floresta Aleatória) para classificação de performance de funcionários. Este é um dos modelos mais robustos e populares em Machine Learning.

#### O que é Random Forest?

Random Forest é um algoritmo de aprendizado supervisionado que cria múltiplas árvores de decisão durante o treinamento e combina suas previsões para chegar a um resultado final mais preciso e estável. É como ter um "comitê de especialistas" onde cada árvore vota na classificação final.

#### Como Funciona?

1. **Treinamento**: O modelo analisa os dados históricos de funcionários e aprende padrões que correlacionam as variáveis preditoras com a performance
2. **Ensemble**: Constrói 100 árvores de decisão independentes (n_estimators=100), cada uma treinada em uma amostra diferente dos dados
3. **Votação**: Para cada nova previsão, todas as árvores "votam" e a classe mais votada é escolhida como resultado
4. **Análise de Importância**: Identifica quais variáveis têm maior impacto na previsão de performance

#### Por que Random Forest?

**Alta Precisão**: Combina múltiplas árvores para reduzir erros e overfitting  
**Robusto**: Lida bem com dados faltantes e outliers  
**Interpretável**: Fornece análise de importância das variáveis  
**Versátil**: Funciona bem sem ajuste extensivo de hiperparâmetros  
**Não Linear**: Captura relações complexas entre variáveis  

#### Processo de Previsão

```
Dados de Entrada (Funcionário)
         ↓
   Pré-processamento
   (LabelEncoder para variáveis categóricas)
         ↓
   Random Forest (100 árvores)
         ↓
   Votação Majoritária
         ↓
   Classificação de Performance
   (Ex: Alto, Médio, Baixo)
```

#### Análise de Importância

O modelo automaticamente calcula e exibe a importância de cada variável preditora, permitindo que você identifique quais fatores mais influenciam a performance dos funcionários na sua organização.

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

## 💡 Benefícios do Modelo

O uso de Random Forest neste projeto oferece vantagens práticas para gestão de RH:

- **Decisões Data-Driven**: Substituir intuição por análise baseada em dados históricos
- **Identificação Precoce**: Detectar potenciais problemas de performance antes que se tornem críticos
- **Alocação Estratégica**: Direcionar recursos de treinamento para áreas com maior impacto
- **Retenção de Talentos**: Identificar e manter funcionários de alto desempenho
- **Padronização**: Avaliar performance de forma consistente e sem viés
- **Escalabilidade**: Analisar centenas de funcionários em segundos

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📜 Licença

Este projeto é de código aberto e está disponível para uso educacional e comercial.

# Imports
import os
import joblib
import openpyxl
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Função para carregar e pré-processar os dados
def carrega_dados(filepath):

    # Carrega os dados do arquivo Excel para um DataFrame
    df = pd.read_excel(filepath)
    
    # Preenche valores ausentes com zero
    df.fillna(0, inplace=True)

    # Cria um LabelEncoder para transformar a coluna 'Cargo'
    le_cargo = LabelEncoder()

    # Aplica o LabelEncoder na coluna 'Cargo'
    df['Cargo'] = le_cargo.fit_transform(df['Cargo'])

    # Cria um LabelEncoder para transformar a coluna 'Performance'
    le_perf = LabelEncoder()

    # Aplica o LabelEncoder na coluna 'Performance'
    df['Performance'] = le_perf.fit_transform(df['Performance'])

    # Seleciona variáveis preditoras (features)
    X = df[['Idade', 'TempoEmpresa', 'Cargo', 'AvaliaçãoGestor', 'Faltas', 'HorasTreinamento']]

    # Define a variável alvo (target)
    y = df['Performance']

    # Retorna features, target e os objetos LabelEncoder
    return X, y, le_cargo, le_perf

# Função para treinar o modelo
def treina_modelo(X, y):

    # Cria um modelo de classificação usando Random Forest com 100 árvores
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Treina o modelo utilizando as variáveis preditoras X e o alvo y
    modelo.fit(X, y)

    # Extraindo as variáveis mais relevantes
    importancias = modelo.feature_importances_
    variaveis = X.columns
    
    print("\nImportância das Variáveis Para a Previsão da Performance:\n")
    for var, imp in sorted(zip(variaveis, importancias), key=lambda x: x[1], reverse=True):
        print(f"{var}: {imp:.4f}")
    
    # Retorna o modelo treinado
    return modelo

# Função para prever performance em novos dados
def faz_previsao(modelo, le_cargo, le_perf, nova_planilha):

    # Carrega os novos dados de uma planilha Excel
    df_novo = pd.read_excel(nova_planilha)
    
    # Preenche valores ausentes com zero
    df_novo.fillna(0, inplace=True)
    
    # Aplica o LabelEncoder treinado anteriormente para codificar a coluna 'Cargo'
    df_novo['Cargo'] = le_cargo.transform(df_novo['Cargo'])
    
    # Seleciona as variáveis preditoras do novo conjunto de dados
    X_novo = df_novo[['Idade', 'TempoEmpresa', 'Cargo', 'AvaliaçãoGestor', 'Faltas', 'HorasTreinamento']]
    
    # Realiza previsões usando o modelo treinado anteriormente
    previsoes = modelo.predict(X_novo)
    
    # Converte as previsões numéricas novamente para as categorias originais usando o LabelEncoder
    df_novo['PrevisaoPerformance'] = le_perf.inverse_transform(previsoes)
    
    # Retorna o DataFrame com as previsões adicionadas
    return df_novo

# Execução principal
if __name__ == "__main__":

    # Imprime mensagem inicial ao executar o script
    print("\nProcessamento Iniciado com Sucesso!")

    # Define o caminho do arquivo com dados históricos usados no treinamento do modelo
    arquivo_treino = "dados_historicos/dados_funcionarios.xlsx"

    # Define o caminho onde o modelo treinado será salvo ou carregado
    modelo_salvo = "modelo/modelo_rh_performance.pkl"

    # Verifica se o arquivo do modelo já existe
    if os.path.exists(modelo_salvo):
        
        # Pergunta ao usuário se deseja utilizar o modelo existente
        escolha = input("\nDeseja usar o modelo existente? (S/N): ").strip().upper()
        
        # Verifica a escolha do usuário
        if escolha == 'S':
            
            # Carrega o modelo e os encoders do arquivo salvo
            modelo, le_cargo, le_perf = joblib.load(modelo_salvo)
            
            # Imprime mensagem confirmando o carregamento do modelo existente
            print("\nModelo carregado com sucesso!")
        
        # Caso o usuário escolha não utilizar o modelo existente
        else:
            
            # Carrega e pré-processa os dados históricos para novo treinamento
            X, y, le_cargo, le_perf = carrega_dados(arquivo_treino)
            
            # Treina um novo modelo usando os dados carregados
            modelo = treina_modelo(X, y)
            
            # Salva o novo modelo treinado junto aos encoders no arquivo definido
            joblib.dump((modelo, le_cargo, le_perf), modelo_salvo)
            
            # Imprime mensagem confirmando o treinamento e salvamento do novo modelo
            print("\nNovo modelo treinado e salvo com sucesso!")
    
    # Caso o arquivo do modelo não exista previamente
    else:
        
        # Carrega e pré-processa os dados históricos para treinamento inicial
        X, y, le_cargo, le_perf = carrega_dados(arquivo_treino)
        
        # Treina o modelo com os dados pré-processados
        modelo = treina_modelo(X, y)
        
        # Salva o modelo treinado junto aos encoders no arquivo definido
        joblib.dump((modelo, le_cargo, le_perf), modelo_salvo)
        
        # Imprime mensagem confirmando o treinamento inicial e salvamento do modelo
        print("\nModelo treinado e salvo com sucesso!")

    # Define o caminho do arquivo com novos dados para realizar previsões
    nova_planilha = "novos_dados/novos_funcionarios.xlsx"

    # Verifica se a nova planilha existe
    if os.path.exists(nova_planilha):
        
        # Realiza previsões usando o modelo carregado ou treinado
        resultado = faz_previsao(modelo, le_cargo, le_perf, nova_planilha)
        
        # Salva as previsões realizadas em um novo arquivo Excel
        resultado.to_excel("previsoes/resultado_previsao.xlsx", index=False)
        
        # Imprime mensagem confirmando que as previsões foram geradas e salvas
        print("\nPrevisões geradas e salvas em previsoes/resultado_previsao.xlsx\n")

# Fim


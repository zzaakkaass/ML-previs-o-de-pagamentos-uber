import pandas as pd                         # importa a biblioteca pandas pra manipulação de dados

df = pd.read_csv(r"d:\meu-feed-personalizado\dados uber\dados_uber.csv")
 # lê o arquivo CSV e carrega num dataframe
print(f"Dataset: {df.shape[0]:,} linhas e {df.shape[1]} colunas")   # mostra quantas linhas e colunas o dataset tem
print('\n\n\n ====resumo do dataset==== \n\n\n')
print(df.describe(include="all"))   # mostra estatísticas descritivas das colunas (numéricas e categóricas)

print('\n\n\n ====informações do dataset==== \n\n\n')
print(df.info())   # mostra informações do dataframe (tipos de dados, nulos, etc.)
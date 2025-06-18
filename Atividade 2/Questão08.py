#Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?  
import pandas as pd

df = pd.read_csv('arquivo.csv') #inserir o nome real do arquivo .csv para mostrar as informações
print(df.head())
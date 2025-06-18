#Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() 
#especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN. 

import pandas as pd

df1 = pd.DataFrame({'nome': ['Fernanda', 'Carlos'], 'idade': [27, 52], 'profissão':['Dev', 'PO']})
df2 = pd.DataFrame({'nome': ['Eduarda'], 'cidade': ['Russas'], 'profissão':['Dev']})
df3 = pd.DataFrame({'nome':['Joana'], 'idade':[19], 'cidade':['Fortaleza']})

resultado = pd.concat([df1, df2,df3], axis=0)
print(resultado)
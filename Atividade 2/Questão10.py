#Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame? 
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'nome': ['Maria', 'Antonio', 'Fernanda', 'Carlos'],
    'idade': [21, 29, 27, 52],
    'cidade': ['Fortaleza', 'Russas', np.nan, np.nan],
    'profissao': ['Dev', 'Engenheiro', 'Dev', 'Operador']
})

print('DataFrame original:\n', df) 

print('\nDataFrame dos valores NaN:\n', df.isna())

print('\nDataFrame sem os valores NaN:\n', df.dropna()) 

print('\nDataFrame como os valores NaN preenchidos: \n', df.fillna('Morada Nova')) #preenche os valores NaN com a essa informação
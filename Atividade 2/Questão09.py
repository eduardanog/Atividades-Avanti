#Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'nome': ['Maria', 'Antonio', 'Fernanda', 'Carlos'],
    'idade': [21, 29, 27, 52],
    'cidade': ['Fortaleza', 'Russas', np.nan, np.nan],
    'profissao': ['Dev', 'Engenheiro', 'Dev', 'Operador']
})

print("Nomes presentes na tabela:\n", df['nome'])

filtro = df[df['nome'] == 'Maria']
print("\nInformações sobre 'Maria':\n",filtro)
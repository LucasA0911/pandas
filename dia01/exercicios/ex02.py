"""Converta o seguinte dicionário para DataFrame e obtenha:
Sumário de cada coluna
Média da coluna idade
Último nome da coluna nome
"""
#%%
import pandas as pd

#%%
dados = {'nome':['Téo', 'Nah', 'Napoleão'], 
         'idade': [31, 32, 14]
         }
# %%
df = pd.DataFrame(dados)

#%%
sumario = df.describe()
sumario
# %%
sumario['idade']['mean']
# %%
df['nome'].tail(1)

# %%

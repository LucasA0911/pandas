"""Converta a seguinte lista de dados para uma Series Pandas e obtenha:
Média
Desvio Padrão
Máximo Valor
"""

#%%
import pandas as pd
#%%
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
# %%
serie_dados = pd.Series(dados, name='dados')
#%%
serie_dados.mean()
# %%
serie_dados.std()
# %%
serie_dados.max()
# %%

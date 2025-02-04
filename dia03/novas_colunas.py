#%%
import pandas as pd

df = pd.read_csv('../data/customers.csv',sep=';')
# %%

#criando colunas novas
#setando o nome         setando o valor
df['Points_double'] = df['Points']*2
df
# %%

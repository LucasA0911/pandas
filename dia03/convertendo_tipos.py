#%%

import pandas as pd

df = pd.read_csv('../data/customers.csv',sep=';')
# %%

#verificando os tipos do dataframe
df.dtypes
# %%

#fazendo a conversão
#lembrando que qualquer tipo que não seja númerico, vai estar como Object
df['Points'].astype(str)
# %%
# %%

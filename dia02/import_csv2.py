#%%
import pandas as pd

#Importando um csv e renomeando o cabeçalho do dataFrame
df = pd.read_csv('../data/products.csv', 
                sep= ';', 
                names= ['ID', 'Name','Description']
                )
df
# %%

df.rename(columns={
                'Name':'Nome', 
                'Description': 'Descrição' 
                }, 
        inplace= True
        )
df
# %%

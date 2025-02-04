#%%

import pandas as pd

df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%

#ordenando do menor para o maior
df.sort_values(by='Points')
# %%

#ordenando do maior para o menor
df.sort_values(by='Points', ascending=False, inplace=True)
# %%
df
# %%
df.sort_values(by='Points', ascending=False, inplace=True)
df.rename(columns={ 
                    'Name': 'Nome',
                    'Points':'Pontos'
                   },
        inplace=True
        )
# %%

# isso é '" uma pipeline."', estamos ordenando e renomeando as colunas na mesma 'Variavel', mas para isso não pode conter o inplace.
df = (
    df.sort_values(by='Points', ascending=False)
    .rename(columns={ 
                        'Name': 'Nome',
                        'Points':'Pontos'
                    }
            )
)
# %%
df
# %%

#Organizando pelos pontos do maior para o menor e pelos nomes em ordem alfabetica. Isso também pode ser feito na '"pipeline"'
df.sort_values(by=['Pontos','Nome'], ascending=[False,True])
# %%

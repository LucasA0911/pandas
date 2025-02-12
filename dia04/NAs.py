#%%

#NAN = dado faltante
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
# %%

"""retorna uma série com um valor booleano
            |   Soma os Trues
            |        |      """
df['idade'].isna().sum()
# %%

#retorna um df com todos os valores NAN
#    |   Transforma em uma série e conta quantos NAN tem em cada coluna do DF
#    |     |
df.isna().sum()
# %%

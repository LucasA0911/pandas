#%%
import pandas as pd

df= pd.read_excel('../data/transactions.xlsx')
df
# %%

#filtrando apenas as ultimas transações de cada cliente
"""Importante, quando for fazer esse tipo de filtro, é importante criar outro dataset e ordenar os dados que você quer manter primeiro, antes de fazer o drop."""
df_last = (df.sort_values(by=['DtTransaction','IdCustomer','Points'],
                     ascending=[False,True,False])
        .drop_duplicates(subset=['IdCustomer'], keep='first')
    )
df_last
# %%

#verificando quantos dados são unicos
df_last['IdCustomer'].nunique()
# %%

#verificando se realmente foi o ultrimo registro desse usuário
df_last[df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
# %%

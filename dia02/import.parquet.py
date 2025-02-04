#%%

#parquet é otmizado para leitura e armazenamento, ou seja, é lido de forma mais rapido, e é menor do que um csv ou um xlsx
import pandas as pd

df = pd.read_parquet('../data/transactions_cart.parquet')
df
# %%
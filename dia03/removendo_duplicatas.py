#%%
import pandas as pd

data = {
    "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
    "Idade": [32,33,2,33,31,32],
    "updated_at":[1,2,3,1,2,3]

}
# %%

#Removendo duplicatas
df = pd.DataFrame(data)
df = df.drop_duplicates #remove apenas se as duas linhas estiverem estritamente iguais
df
# %%
#especificando as colunas e a ordem em que você quer que a remoção ocorra, 
df = (df.sort_values(by='updated_at', ascending=False)
        .drop_duplicates(subset=["Nome","Idade"],keep='first')
    ) 
df

# %%

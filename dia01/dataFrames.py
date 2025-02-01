#%%
import pandas as pd

#%%
data = {
    'nome': ['Lucas','Julia','Zoe','Thor','Layla'],
    'sobrenome':['Alves','Ferreira','dos','Santos','Nascimento'],
    'idade':[26,24,2,8,3]
}
#%%
data['idade'][0]
# %%

#Data Frame é um conjunto de séries

#Criando um data frame
df = pd.DataFrame(data)
df
# %%

#pegando uma coluna
df['idade']
# %%
#pegando a idade na posição 0
df['idade'].iloc[0]
# %%

#%%

#pegando uma linha inteira, onde os indices da série serão as colunas
df.iloc[1]

# %%

# saber o nome das colunas
df.columns
# %%
# saber os indices
df.index
# %%

#mostra as informações, e quantidade exata de memória que esta sendo usada na ram
df.info(memory_usage='deep')
# %%

# mostra uma série contendo as informações dos tipos de cada coluna
df.dtypes

# %%

#aplica estatisticas descritivas em cada uma das colunas que contém números
df.describe()

# %%

df['peso'] = [79, 101, 8, 20, 8]
df.describe()
# %%

sumario = df.describe()
sumario['peso']['mean']

# %%

#mostra as 5 primeiras linhas como default
df.head()
# %%
#mostra a quantidade de linhas que for passada no parametro
df.head(2)
# %%

#mostra os 5 ultimos como default
df.tail()

# %%
# mostra a quantidade que for passada no parametro
df.tail(2)
# %%

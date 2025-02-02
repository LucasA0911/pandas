#%%
import pandas as pd

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers
# %%
#mostra a quantidade de linhas e de colunas
df_customers.shape
# %%
#mostra os atributos do dataframe com a quantidade de memoria utilizada
df_customers.info(memory_usage='deep')
# %%

#Descrição estatistica da coluna
sumario = df_customers['Points'].describe()
# %%
sumario.max()
# %%

#Filtros

# É possivel fazer calculos e operações logicas em toda a série
condicao = df_customers['Points'] > 1000
# %%

#retorna uma série booleana
condicao
# %%

#passando a série booleana para a posição do DF e ele retorna apenas as linhas que são TRUE
df_customers[condicao]
# %%

#isso:
maximo = df_customers['Points'].max()
condicao_maximo = df_customers['Points'] == maximo
df_customers[condicao_maximo]
# %%

# É o mesmo que isso:
condicao_maximo = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao_maximo]
# %%

#que é o mesmo que isso:
df_customers[df_customers['Points'] == df_customers['Points'].max()]
# %%

#Buscando o nome do cliente
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name'].iloc[0]

#%%

#para filtrar elementos entre 2 valores, é necessario colocar os () e o & entre as condições
condicao_entre = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers[condicao_entre]
# %%
"""
Quando criamos uma nova váriavel do dataFrame, o Python entende que estamos fazendo uma referencia ao dataFrame principal.

EX: condicao_entre é igual a df_customers.

É de suma importancia que se for fazer alguma alteração no dataframe, utilizar o método copy() para fazer uma cópia do dataFrame principal, e não lascar com tudo

Ex:
condicao_entre = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_1000_2000 = df_customers[condicao_entre].copy()

Criando uma nova variavel com o resultado do filtro, e essa variavel vira um dataFrame novo
"""
#%%

#seleciona uma coluna e transforma o dataframe em uma serie
df_customers['UUID']

#%%

#seleciona duas colunas e mantem como dataframe
df_customers[['UUID','Name']]
# %%

#colocando o nome das colunas em uma lista, e ordenando em ordem alfabetica
colunas = df_customers.columns.to_list()
colunas.sort()
df_customers[colunas]
#%%

#setando no dataFrame original o que foi feito no filtro

df_customers = df_customers[colunas]
df_customers
# %%

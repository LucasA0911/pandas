#%%

import pandas as pd
# %%

# média

idades = [30,42,90,34]

media = sum(idades) / len(idades)

print(media)
# %%

# desvio padrão = soma onde subtrai todos os elementos da média e divide pelo número de elementos -1 e eleva ao quadrado

total = 0

for i in idades:
    total += (media -i)**2

variancia = total / (len(idades)-1)
print(variancia)
# %%

#Defiindo séries e o atributo NOME da série
series_idades = pd.Series(idades, name= 'Idades')
print(series_idades)
# %%

#métodos

#média
series_idades.mean()
# %%

#variancia
series_idades.var()
#%%

#desvio padrão
series_idades.std()
# %%

#mediana
series_idades.median()
# %%

#terceiro quartil
series_idades.quantile(0.75)
#%%

#sumarização
series_idades.describe()
# %%
"""
métodos de verbos = var, mean, median etc...
métodos de atributos diz respeito a uma caracterista."""

#dimensão da série
#Atributo que mostra quantas linhas a série tem
series_idades.shape 
# %%

#Navegando na série
series_idades[0]

# %%
series_idades.index #puxa os indexes da série

# %%
#trocando os index
series_idades.index = ['l','u','c','a']
series_idades
# %%

#buscando pelo index, A MELHOR FORMA DE BUSCAR É SEMPRE PELO INDEX
series_idades['l'] 
# %%
#buscando pela posição em caso de index no formato alfabetico
series_idades[0] 
# %%
series_idades.index = [40,10,30,20]
series_idades
#%%
#navegando pela posição especifica da série, nos indices númericos
series_idades.iloc[0]
# %%

#navegando pelo index da série
series_idades.loc[10]
# %%

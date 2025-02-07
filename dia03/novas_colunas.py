#%%
import pandas as pd

df = pd.read_csv('../data/customers.csv',sep=';')
# %%

#criando colunas novas
#setando o nome         setando o valor
df['Points_double'] = df['Points']*2
df
# %%

#criando uma função para pegar nomes antes do _.
#Importante sempre fazer essas funções pensando nos elementos da série
def get_first(nome:str):
    return nome.split('_')[0]
# %%

#utilizado o metodo apply para aplicar a função criada na série
df['Name'].apply(get_first)
# %%

#Criando uma nova coluna com apenas os primeiros nomes
df['First Name'] = df['Name'].apply(get_first)

# %%
df
# %%

"""
Lambda é uma função anonima em que não precisa escrever o corpo dela de forma padrão.
É muito utilizada para escrever em uma unica linha uma função que só sera utilizada naquele momento e que seja bem simples
"""

#EX:

"""
declara o nome
 |  chama o lambda
 |       |    define os parâmetros
 |       |     |   define o que função vai fazer
 |       |     |    |        """
soma = lambda x,y: x+y

# %%
get_f = lambda nome: nome.split('_')[0]

# %%
df['Name Lambda'] = df['Name'].apply(get_f)
df
# %%

#também pode ser feito da seguinte forma

df['Name'].apply(lambda x: x.split('_')[0])
# %%

#pode ser passado mais de 1 metodo
df['Name'].apply(lambda x: x.upper().split('_')[0])

# %%

#Criando um intevalo de pontos

def intervalo_pontos(pontos):
    if pontos < 2500:
        return 'Baixo'
    elif pontos < 3500:
        return 'Medio'
    else:
        return 'Alto'

df['Faixa_pontos'] = df['Points'].apply(intervalo_pontos)
df
# %%

#Criando uma coluna de RFV nos dados a baixo
data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1,30,10,45],
    "valor":[100,2000, 15, 500],
    "frequencia":[2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)

def rfv(row):
    
    nota = 0
    
    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0
    
    return nota

# %%
df_crm["RFV"] = df_crm.apply(rfv, axis=1) # o Axis está recebendo cada linha
df_crm

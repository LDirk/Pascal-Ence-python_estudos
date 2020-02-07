import pandas as pd 
import numpy as np 

dados = {
	'nomes':['Joao','Maria', 'José', np.nan, 'Pedro', 'Judas', 'Tiago'],
	'sexo':['M','F','M', np.nan,'M', 'M', np.nan],
	'idade':[14, 13, np.nan, np.nan, 15, 13, 14],
	'nota' : [4, 10, 7, np.nan, 8, 9, 7]	
}
df = pd.DataFrame(dados)
print(df)
print()

#Df apenas com dados completos
print(df.dropna())
print()

#Excluir somente as linhas que não possuem nada
print(df.dropna(how = 'all'))
print()

#Excluir somente as colunas que não possuem nada
print(df.dropna(how ='all', axis = 1))
print()

#Preencher o NaN com algum valor
print(df['idade'].fillna(1))
print()

#fazer a alteração dentro do df 
print(df['idade'].fillna(1, inplace = True))
print()
print(df)
print()

#Mostrando nome e sexo nao nulos
print(df[df['nomes'].notnull() & df['sexo'].notnull()])






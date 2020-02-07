import pandas as pd 
import numpy as np 

df = pd.read_csv('primary-results.csv')

#Olhar o cabeçalho
print(df.head())

#Agrupar sobre determinado termo com as estatisticas desc que vc quiser
print(df.groupby('candidate').aggregate({'votes': [min, np.mean, max]}))
print()

#Agrupar e filtrar 
def fraction_votes_filter(x):
	return x['votes'].sum() > 300000

print(df.groupby('state').filter(fraction_votes_filter))


import pandas as pd 
copacabana = pd.read_csv("copacabana.csv", delimiter = ';')

#Verifica as colunas do DF
print(copacabana.columns)
print()

#Entender melhor uma coluna, média, quartis, etc 
print(copacabana['Quartos'].describe())
print()

#Fazer uma comparação bool
print(copacabana['Quartos']>5)
print()

#Vai mostrar todas as informações do quarto
print(copacabana.loc[copacabana['Quartos'] == 6])
print()

#Criar uma nova coluna
copacabana['TOTAL'] = copacabana['AreaConstruida'] * copacabana['VAL_UNIT']
print(copacabana['TOTAL'].describe())
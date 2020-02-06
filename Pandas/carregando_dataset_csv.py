import pandas as pd 

#carregando o csv
copacabana = pd.read_csv("copacabana.csv", delimiter = ';')
print(copacabana)
print()
print()

#xls
populacao_pe = pd.read_excel('total-populacao-pernambuco.xls')
print(populacao_pe)


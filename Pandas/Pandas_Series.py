import pandas as pd

#Series são dados em uma dimensão
a = pd.Series([1,4,6,5,7,10,6])
print(a)
print()

#Describe faz umas estatistica descritiva da lista
print(a.describe())
print()

#duplicate diz se tem outro elemento com aquele valor
print(a.duplicated())
print()

#Concatenando series
s2 = pd.Series([11, 5 , 8 ])
a = a.append(s2)
print(a)








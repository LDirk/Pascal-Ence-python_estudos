import pandas as pd 
import pydataset 

#Mostra os dataset disponiveis da biblioteca
print(pydataset.data())
print()
print()

#Head(n) mostra os n primeiros dados
titanic = pydataset.data("titanic")
print(titanic.head(10))
print()
print()

#Descreve o dataset 
print(titanic.describe())
print()
print()

#Faz a contagem dos elementos da classe, quantos 3,2 e 1 
print(titanic['class'].value_counts())
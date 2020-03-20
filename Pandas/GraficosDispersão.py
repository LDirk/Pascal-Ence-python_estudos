import matplotlib.pyplot as plt
import pandas as pd 
import pydataset 

#Números de passageiros por mes 
df = pydataset.data('AirPassengers')
print(df.head(150))

#Gráficos de dispersão 
plt.scatter(df['time'], df['AirPassengers'])
plt.show()

#Pegando outro dataset 
iris = pydataset.data('iris')

#ADD uma nova coluna no dataset 
def specia_color(x):
	if x == 'setosa':
		return 0
	elif x == "versicolor":
		return 1 
	return 2

iris['SpeciesNumber'] = iris['Species'].apply(specia_color)
print(iris.head())

#Mudando a cor de acordo com a especie
plt.scatter(
	iris['Sepal.Length'],iris['Sepal.Width'],  iris['Petal.Length'],
	c = iris['SpeciesNumber'], cmap  = 'viridis', alpha = 0.4
)
plt.show()
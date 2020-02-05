import numpy as np
a = np.array([[1,2],[3,4]])
print(a)

# repetir os elementos (array ou elemento, numero_de_repetições)
b = np.repeat(a,2)
print(b)

#Repetindo array com tile (array, numero de repetiçoes)
a = np.array([1,2,3])
a = np.tile(a,2)
print(a)

#Repetindo com tile ao longo de um eixo
b = np.array([[1,2],[3,4]])
b = np.tile(b,2)
print(b)
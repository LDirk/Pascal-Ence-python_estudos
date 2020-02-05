import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
print(a)

#Divindo array (array, quantos quer dividir, eixo que quer dividir )
print(np.array_split(a, 2, axis = 0))
print(np.array_split(a, 2, axis = 1))



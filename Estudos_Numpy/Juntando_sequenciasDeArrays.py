import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

#Concatenando ao longo do eixo 0 
c = np.concatenate((a,b), axis = 0)
print(c)
print()
print()

#Concatenando ao longo do eixo 1
c = np.concatenate((a,b.T), axis = 1)
print(c)
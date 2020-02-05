import numpy as np
a = np.array([[1,2],[3,4],[5,6]])

#Deletando elemento (array, posição do elemento a apagar, eixo (linha 0))
b = np.delete(a, 1,0)
print(b)

#(array, posição do elemento, eixo( coluna 1 ))
c = np.delete(a,0,1)
print(c)


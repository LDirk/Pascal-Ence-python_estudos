import numpy as np 

#Skiprows serve para pular a primeira linha 
#Unpack serve para por os valores da coluna um na val1, coluna 2 val2, etc

val1, val2, val3 = np.loadtxt("dados.txt", skiprows = 1, unpack = True)
print(val1)
print(val2)
print(val3)
print()
print()
# filling_values Serve para por o valor que vc quiser no dado faltante
my_array = np.genfromtxt("dados2.txt", skip_header = 1, filling_values = 0)
print(my_array)


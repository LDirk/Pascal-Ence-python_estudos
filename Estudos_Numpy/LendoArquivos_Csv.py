import numpy as np 
#Delimiter é o que separa os dados
valores = np.genfromtxt("arquivo.csv", delimiter =',',skip_header = 1)
print(valores)


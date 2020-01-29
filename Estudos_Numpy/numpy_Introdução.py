import numpy
#Recebe uma lista e transforma em um Array
a = numpy.array([10,20,30,40])
print(a)

#Matrizes, no exemplo 2x2
mat = numpy.array([[1,2],[3,4]])
print(mat)

#Consultar elementos de acordo com linha e coluna, exemplo 2 linha e 2 coluna
print(mat[1][1])

#Acessando linhas, exemplo 2 linha
print(mat[1,:])

#Acessando colunas, exemplo 1 coluna
print(mat[:,0])

#Obtendo matriz Transposta.
print(mat.transpose())


#Somar Matrizes, análogo para * e -
m1 = numpy.array([[1,2],[3,4]])
m2 = numpy.array([[5,6],[7,8]])
print(m1 + m2)

#Somar elementos do Array
m3 = numpy.array([1,2,3,4])
print(m3.sum())


#Indice do maior argumento
print(m3.argmax())

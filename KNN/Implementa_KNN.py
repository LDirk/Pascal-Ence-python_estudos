""" O DataSet é sobre a sobrevivencia dos pacientes submetidos a operação de cancer de mama

Primeira coluna: Idade do paciente na operação

Segunda coluna: Ano da operação

Terceira coluna: Número de nos detectados

Quarta coluna : Status de sobrevivencia
1 - o paciente sobreviveu 5 anos ou mais.
2 - o paciente morreu entre 5 anos."""

#Lista de amostras
amostras = [] 
with open("dataset.data",'r') as f:
	for linha in f.readlines():
		atributos = linha.split(',')
		amostras.append([int(atributos[0]),int(atributos[1]),int(atributos[2]),int(atributos[3])])

def infodataset(amostras, verbose = True):
	if verbose:
		print("Total de amostras: %d" %len(amostras))

	#Sobreviveu mais de 5 anos ou não
	rotulo1, rotulo2 = 0, 0

	for amostra in amostras:
		#amostra -1 é o ultimo elemento de cada lista das amostras
		if amostra[-1] == 1:
			rotulo1 +=1 
		else:
			rotulo2 += 1

	if verbose:
		print("Total rotulo1: %d" %rotulo1)
		print("Total rotulo2: %d " %rotulo2)

	return[len(amostras), rotulo1, rotulo2]


#Conjunto para treinamento, 60% do rotulo 1 e 60% do rotulo2
p = 0.6
_, rotulo1, rotulo2 = infodataset(amostras, verbose = False)

treinamento, teste = [], []

max_rotulo1, max_rotulo2 = int(p*rotulo1), int(p*rotulo2)


total_rotulo1, total_rotulo2 = 0, 0 

for amostra in amostras:

	if (total_rotulo1+total_rotulo2)<(max_rotulo1+max_rotulo2):
		treinamento.append(amostra)
		if amostra[-1]==1 and total_rotulo1<max_rotulo1:
			total_rotulo1 +=1
		else:
			total_rotulo2 +=1
	else:
		teste.append(amostra)

import math 

def dist_euclidiana(v1,v2):
	dim, soma = len(v1), 0
	#Até -1 para não incluir os rótulos
	for i in range(dim,-1):
		soma += math.pow(v1[i]-v2[i],2)
	return math.sqrt(soma)

def knn(treinamento, nova_amostra, k):
	dists, tam_treino = {}, len(treinamento)
	#Calcular a distancia eucli da nova para todos os outros exemplos do conjunto de treinamento
	for i in range(tam_treino):				#teste
		d = dist_euclidiana(treinamento[i], nova_amostra)
		dists[i] = d 
	# obtém as chaves (indices) dos k-vizinhos mais proximos
	#A distancia do treinamento é de um a todos os elementos da amostra
	k_vizinhos = sorted(dists, key = dists.get)[:k]

	#votação majoritaria
	qtd_rotulo1, qtd_rotulo2 = 0, 0 
	for indice in k_vizinhos:
		if treinamento[indice][-1] == 1:
			qtd_rotulo1 +=1
		else:
			qtd_rotulo2 +=1

	if qtd_rotulo1>qtd_rotulo2:
		return 1
	else:
		return 2 	


acertos, k = 0, 13

for amostra in teste:		  #teste
	classe = knn(treinamento, amostra, k)
	if amostra[-1] == classe:
		acertos +=1

print("Total de treinamento: %d " %len(treinamento))
print("Total de testes: %d" %len(teste))
print("Total de acertos: %d" % acertos)
print("Porcentagem de acertos: %.2f%%" %(100*acertos/len(teste)))
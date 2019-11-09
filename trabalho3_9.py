import random

lista = []
contador = 0

while contador<= 49:
    lista.append(random.randint(0,20))
    contador = contador + 1

print(lista)

# item A
print(f"A soma dos elementos da lista é :{sum(lista)}")

# item B

print(f'O 7 aparece:{lista.count(7)} vezes')

#item C
print(f'O valor maximo é {max(lista)}')

#item D
listanew =[]
for i in range (len(lista)):
    if lista[i] == max(lista):
        listanew.append(i)

print(listanew)
        
    


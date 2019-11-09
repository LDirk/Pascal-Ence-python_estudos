def questao7(numero):
    primos = [1,numero]
    lista = []
    for i in range(1,numero+1,1):
        if (numero % i)== 0:
            lista.append(i)

    if primos == lista:
        return("True, é primo")
    else :
        return("False, não é primo")

print(questao7(11))
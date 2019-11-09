def divisores(n):
    contador = 1
    lista = []

    while contador<n:
        if (n%contador)==0:
            lista.append(contador)
            contador = contador + 1
        else:
            contador = contador + 1

    return lista

print(divisores(9))
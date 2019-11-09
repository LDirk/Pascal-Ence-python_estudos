def questao6(n):
    lista = []
    cont = n

    if n == 0:
        lista.append(0)

    elif n == 1:

        lista.append(0)
        lista.append(1)

    else:

        x = -1

    while x == -1:

            if cont // 2 == 0:
                lista.append(cont % 2)
                break

            else:
                lista.append(cont % 2)
                cont = cont // 2
    lista.reverse()
    return lista

print(questao6(4))
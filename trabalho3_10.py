def função(a,b):
    
    lista = []
    contador = 1
    
    if a>b:       
        while contador <= a:
            if (a%contador==0) and (b%contador==0):
                lista.append(contador)
                contador = contador + 1
            else:
                contador = contador + 1
    else:
        while contador <= b:
            if (a%contador==0) and (b%contador==0):
                lista.append(contador)
                contador = contador + 1
            else:
                contador = contador + 1
    return max(lista)
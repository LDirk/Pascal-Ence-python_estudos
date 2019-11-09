def questao8(ano):

    if ((ano%400)==0) or (((ano%4)==0)and((ano%100)!=0)):
        return("True, é bissexto")
    else:
        return("False, não é bissexto")


print(questao8(403))
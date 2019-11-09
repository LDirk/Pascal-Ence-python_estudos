def questao1(diass):

     anos = diass // 360

     meses = (diass - anos*360)//30

     dias = (diass - anos*360 - meses*30)

     return (f" {diass} dias são {anos} anos, {meses} meses e {dias} dias")

print(questao1(785))



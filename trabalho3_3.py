altura = float(input("Digite o sua altura em metros: "))
peso = float(input("Digite o seu peso em kg : "))

IMC = peso/(altura)**2

if IMC<18.5 and IMC > 0:
    print("MAGREZA")
    print("Tome um hipercalórico ")

elif IMC>= 18.5 and IMC<= 24.9:
    print("Normal")
    print("Ta no shape")

elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso")
    print("Ta gordinho ein")

elif IMC >= 30 and IMC <= 39.9:
    print("Obeso ")
    print("Passou da hora de fazer dieta")

elif IMC>=40:
    print("Obesidade grave")
    print("Vai infartar ein ")

else :
    print("Altura ou peso inválidoS")
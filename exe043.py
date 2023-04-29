'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com os dados abaixo:
Abaixo de 18,5: abaixo do peso; Entre 18,5 e 25: peso ideal; 25 até 30: sobrepeso; 30 até 40: obesidade; Acima de 40: obesidade mórbita'''

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = (peso)/altura**2

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.4 < imc < 26:
    print("Você está no peso ideal.")
elif 24 < imc < 31:
    print("Você está com sobrepeso.")
elif 29 < imc < 41:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbita.")
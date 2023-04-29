'''Faça um programa que leie três números e mostre qual é o maior e o menor entre eles'''
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

#verificando o maior numero
maior = num1
if num2>num1 and num2>num3:
        maior = num2
if num3>num1 and num3>num2:
        maior = num3
#verificando o menor numero
menor = num1
if num2<num1 and num2<num3:
        menor = num2
if num3<num1 and num3<num2:
        menor = num3
print("O maior número é {}, e o menor número é {}".format(maior, menor))
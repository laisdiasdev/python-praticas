'''Desenvolva um programa que leia o comprimento de três retas e dias ao usuário se elas podem ou não formar um triângulo.

Um triângulo se define se a soma de duas das três retas for menor que outra'''

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('É triângulo.')
else:
    print('Não é triângulo.')
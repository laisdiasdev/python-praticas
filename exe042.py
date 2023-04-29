'''Desenvolva um programa que leia o comprimento de três retas e dias ao usuário se elas podem ou não formar um triângulo.
Um triângulo se define se a soma de duas das três retas for menor que outra
E ainda, informe se o triângulo é;
EQUILÁTERO: todos o lados são iguais
ISÓCELES: dois lados são iguais
ESCALENO: todos os lados são diferentes'''

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('É triângulo.')
    if reta1 == reta2 == reta3:
        print('É um triângulo equilátero.')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('É um triângulo isóceles.')
    else:
        print('É um triângulo escaleno.')
else:
    print('Não é triângulo.')


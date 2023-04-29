'''Faca um programa que leia um ângulo qualquer e mostre na tela oo valor do seno, cosseno e atangente desse numero'''

from math import cos, sin, tan, floor
angulo = int(input('Digite um angulo: '))
cosseno = floor(cos(angulo))
seno = floor(sin(angulo))
tangente = floor(tan(angulo))
print('O cosseno desse angulo é {}, o seno é {}, e a tangente é {}.'.format(cosseno, seno, tangente))

'''from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))'''
'''Digite um numero real qualquer que leia somente a sua parte inteira'''

'''import math
num = float(input('Digite um numero racional: '))
parte_inteira = math.floor(num)
print('A parte inteira desse número é {}'.format(parte_inteira))

number = float(input('Escolha um numero para ser dividido por 3: '))
inteira = number // 3
print(inteira)
OU: '''
from math import floor, trunc
num = float(input('Digite um número real: '))
print('A parte inteira desse número é {}'.format(floor(num)))

#de outra maneira:
num2 = float(input('Digite outro número real: '))
print('A parte inteira desse numero é {}'.format(trunc(num2)))

#agora sem usar biblioteca:
num3 = float(input('digite mais um número real: '))
print('A parte inteira desse número é {}'.format(int(num3)))
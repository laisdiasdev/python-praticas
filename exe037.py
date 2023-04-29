'''CONVERSOR DE BASES NUMÉRICAS
Escreva um programa que leia um número inteiro qualquer e peça para o suário escolher qual será a base de conversão: 1 para binário; 2 para octal; 3 para hexadecimal'''
num = int(input('Digite um número: '))
conversao = int(input('Você quer converter esse número para: [1]-BINÁRIO, [2]-OCTAL ou [3]-HEXADECIMAL? '))
if conversao == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif conversao == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num)[2:]))
elif conversao == 3:
    print('O número {} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
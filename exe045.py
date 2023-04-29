'''Crie um programa que faça o computador jogar Jokenpô (pedra, papel tesoura) com você.'''
from random import randint
#from sleep import time
itens = ('Pedra', 'Papel','Tesoura')
computer = randint(0,2)

print('Suas opções: ')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

jogador = int(input('Qual é a sua jogada? '))
if 0 > jogador > 2:
    print('JOGADA INVÁLIDA! Escolha um opção válida.')
print('JO')
#sleep(1)
print('KEN')
#sleep(1)
print('PÔ')
print('-#'*11)
print('O computador escolheu {}'.format(itens[computer])) #itens na posição comptador
print('Jogador jogou {}'.format(itens[jogador]))
print('-#'*11)

if computer == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('jogador VENCEU!')
    elif jogador == 2:
        print('Computador VENCEU!')
elif computer == 1:
    if jogador == 0:
        print('computador VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCEU!')
elif computer == 2:
    if jogador == 0:
        print('Jogador VENCEU!')
    elif jogador == 1:
        print('Computador VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
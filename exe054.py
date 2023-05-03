'''Crie um programa que leia a idade de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e diga quantas já são maiores.'''
from datetime import date
data_atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(7):
    '''ou for i range(1, 8)'''
    data_nasc = int(input(('Em que ano a {}ª pessoa nasceu? '.format(i+1))))
    idade_atual = data_atual - data_nasc
    if idade_atual >= 18:
        totmaior += 1
    else:
        totmenor += 1

print('O total de pessoas com maioridade é {}.'.format(totmaior))
print('O total de pessoas com menoridade é {}.'.format(totmenor))

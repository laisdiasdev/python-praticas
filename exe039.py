'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deveria mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
genero = int(input('qual o seu gênero? [1]-FEMINIMO ou [2]-MASCULINO: '))

if genero == 1:
    print('Por ser mulher, o seu alistamento às forças armadas não é obrigatório.')
elif genero == 2:
    print('Quem nasceu em {}, tem {} anos de idade.'.format(nasc, idade))

    if idade == 18:
        print('Você está no tempo de fazer o alistamento ao exécito.')
    elif idade < 18:
        diferenca = 18 - idade
        print('Ainda faltam {} anos para você se alistar.'.format(diferenca))
    elif idade > 18:
    #tbm pode ser else
        diferenca = idade - 18
        print('Você deveria fazer o alistamento há {} anos atrás.'.format(diferenca))
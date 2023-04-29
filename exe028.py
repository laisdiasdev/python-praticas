'''Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o user venceu ou perdeu.'''
from random import randint
computador = randint(0,5)
print("Se vc acertar o numero que eu escolhi, vc ganha o jogo. Caso contrario, eu ganho.")
jogador = int(input("Digite um numero: "))

if jogador == computador:
    print("Vc ganhou o jogo!")
else:
    print("Vc perdeu o jogo hahaha!")

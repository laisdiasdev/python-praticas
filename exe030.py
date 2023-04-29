'''Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou ímpar'''
from random import randint
num = randint(0,99)
if num%2 == 0:
    print("Número par: ", num)
else:
    print("Número ímpar: ", num)
'''Desenvolva um programa que leia seis números inteiros e mostre apenas aqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o'''
from random import randint

numeros_pares = []
for i in range(6):
    n = randint(1, 50)
    if n%2 == 0:
        numeros_pares.append(n)
print(numeros_pares)
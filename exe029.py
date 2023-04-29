'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite. '''
from random import randint
velocidade = randint(40,100)
multa = velocidade * 7

if velocidade > 80:
    print("\033[31mVoce foi MULTADO por excesso de velocidade. Sua multa é de RS${} reais\33[0m]".format(multa))
else: 
    print("Continue dentro do limite de velocidade.")


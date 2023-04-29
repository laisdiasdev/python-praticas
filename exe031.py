'''Desenvolva um programa que pergunte a distancia de uma viagm em km. Calcule o preco da passagem, cobrando R$0,50 por km para vagens de até 200km e R$0,45 para viagens mais longas.'''
distancia = int(input("Qual a distância em km de São Luís até Imperatriz? "))

if distancia <= 200:
    passagem = 0.50 * distancia
    print("Sua passagem fica de {} reais".format(passagem))
else: 
    passagem = 0.45 * distancia
    print("Sua passagem fica de {}".format(passagem))
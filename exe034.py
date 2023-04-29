'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários acima de 1.250, calcule um aumento de 10%. Para os abaixo ou iguais, o aumento é de 15%'''
from random import randint 
salario_atual = randint(1000, 5000)

if salario_atual >= 1250:
    novo_salario = salario_atual + (salario_atual*0.1)
    print("Seu novo salário é de R${:.2f}".format(novo_salario))
else:
    novo_salario = salario_atual + (salario_atual*0.15)
    print("Seu novo salário é de R${:.2f}".format(novo_salario))
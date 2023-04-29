'''um professor quer sortear um dos seus quatro alunos para apagar o quadro. faca um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhi'''
from random import choice
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceirpo aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista_de_alunos = [n1, n2, n3, n4]
escolhido = choice(lista_de_alunos)

print ('O aluno escolhido para apagar o quadro foi {}'.format(escolhido))
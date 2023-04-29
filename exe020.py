'''O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos'''
from random import shuffle #esse método serve para embaralhar a lista no caso
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceirpo aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista_de_alunos = [n1, n2, n3, n4]
escolhido = shuffle(lista_de_alunos)

print('A ordem de apresentação será: \n', lista_de_alunos)
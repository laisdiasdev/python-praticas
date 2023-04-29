'''Crie um programa que leie o nome completo de uma pessoa e mostre: o nome co todas as letras maiusculas e minusculas; quantas letras ao todo (sem considerar espacos); quantas letras tem o primeiro nome'''
nome = str(input('digite seu nome completo: ')).strip() #essa fuçao não conta os espaços de antes e depois da string
print('Analisando seu nome...')
print('Seu nome com letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(''))) #a função count vai contar quantos espaços há entre o nome, então a função len vai subtrair esses espaços
print('seu primeiro nome tem {} letras'.format(nome.find('')))
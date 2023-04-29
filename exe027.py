'''Faca um programa que leie o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente'''
nome = str(input('Digite seu nome completo: ')).strip()
nome_fatiado = nome.split()
print(nome_fatiado)
print('Seu primeiro nome é {}.\nSeu último nome é {}.'.format(nome_fatiado[0], nome_fatiado[len(nome_fatiado) - 1]))

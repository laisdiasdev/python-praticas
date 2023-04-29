'''Refaça o desaio 009, mostrando a tbuada de um número que o usuário escolher, só que utilizando um laço for.'''

num = int(input('Digite um número para saber sua tauada: '))
for i in range(0, 10+1):
    print('{} x {} = {}'.format(num, i, (num*i)))

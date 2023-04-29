'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram o intervalo de 1 até 500'''
soma = 0
for n in range(1, 501):
    if n%3 == 0:
        if n%2 == 1:
            print(n)
            soma += n
print('A soma dos números ímpares mútiplos de 3 no intevalo de 1 até 500 é: {}.'.format(soma))
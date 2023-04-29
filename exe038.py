'''COMPARANDO NÚMEROS'''
num1 = int(input('Digite um número qualquer: '))
num2 = int(input('Digite outro número qualquer: '))

if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior que {}'.format(num2, num1))
elif num1 == num2:
    print('Os dois números são iguais.')
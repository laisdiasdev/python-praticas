'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.'''
valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário mensal? '))
anos = int(input('Você deseja financiar em quantos anos? '))
prestacao = valor_casa / (anos * 12)
minimo = salario * (30 / 100)

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print(' a prestacao será de R${:.2f}.'.format(prestacao))
if prestacao >= minimo:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
#crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
reais = float(input('Quanto voce tem na carteira? '))
dollar = reais/5.40
print('Seu dinheiro em dollar é de ${:.2f}'.format(dollar))
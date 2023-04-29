'''escreva um programa que pergunte a quantidade em Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que  carro custa R$60 por dia e R$0,15 por Km rodado.'''
km = int(input('Quantos Km vc rodou no carro? '))
dias = int(input('Quantos dias vc passou com ele? '))
preco  = (60 * dias) + (0.15 *km)
print('O valor que vc precisa pagar pelo carro alugado é de R${}'.format(preco))
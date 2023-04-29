'''faca um programa que leia o preco de um produto e mostre seu preco com um desconto de 5%'''
preco = float(input('Digite o valor do produto: '))
desconto = (5/100) * preco
preco_com_desconto = preco - desconto
print('Este produto com o desconto de 5% é de {:.2f} reais'.format(preco_com_desconto))
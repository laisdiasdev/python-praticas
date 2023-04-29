'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
À vista dinheiro/cheque: 10% de desconto; À vista no cartão: 5% de desconto; Em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros.'''

print("="*12,"LOJAS AGILIZA!","="*11)

valor_compra = float(input("\nQual o valor da compra? \n"))
din_cheque = valor_compra - (10/100) * valor_compra
# variável que representa a primeira opção de pagamento
av_cartao = valor_compra - (5/100) * valor_compra
# variável que representa a segunda opção pagamento
muitas_parcelas = valor_compra + (20/100) * valor_compra
# variável que representa a quarta opção de pagamento


print("="*10,"FORMAS DE PAGAMENTO","="*8)
print("")
print("[1] À vista dinheiro/cheque;")
print("[2] À vista no cartão;")
print("[3] Em até 2x no cartão;")
print("[4] 3x ou mais no cartão.")

opcao = int(input("\nEscolha uma opção: "))

if opcao == 3:
    parcelas = valor_compra/2
    print("Sua compra será parcelada em 2x de R${}.".format(parcelas))
    # condição que representa a escolha da terceira opção de pagamento.
elif opcao == 1:
    print("Comprando à vista dinheiro/cheque, você tem um desconto de 10%. Sua compra será de R${}.".format(din_cheque))
elif opcao == 2:
    print("Comprando à vista no cartão, sua compra sai por R${}".format(av_cartao))
elif opcao == 4:
    parcelas = int(input("Você deseja parcelar em quantas vezes? "))
    valor_parcelas = muitas_parcelas/parcelas
    print("Sua compra será parcelada em {} vezes de {:.2f}. O valor pago final será de {} por conta dos juros.".format(parcelas, valor_parcelas, muitas_parcelas))
else:
    print("Opção inválida.")
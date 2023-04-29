'''Crie um programa que leie o nome de uma cidade e diga se ela começa ou não com o nome "Santo" '''
cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
#até 5 porque a o nome snat só tem 5 letras(esse 5 não é incluído, pq as 5 letras começa do 0 até o 4,)

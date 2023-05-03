'''Crie um programa que leia uma frase qualquer e diga se ela é um palídromo, disconsiderando os espaços.'''
frase = input('Digite uma frase qualquer: ').strip().upper()
palavras = frase.split()
tudoJunto = ''.join(palavras)
inverso = ''
#print('você digitou a frase "{}"'.format(tudoJunto))
for letra in range(len(tudoJunto) -1, -1, -1): #len(tudoJunto) -1,...) pq precisa ignorar o zero do tamanho
    inverso += tudoJunto[letra]
print(tudoJunto, inverso)

if inverso == tudoJunto:
    print('Temos um palídromo.')
else:
    print('Não temos um palídromo.') 


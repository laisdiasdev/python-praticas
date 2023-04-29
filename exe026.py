'''Faca um programa que leie uma frase e mostre: quatas letras "a" tem, qual a posição da primeira letra a, qual a posição da última letra a'''
frase = input('Digite uma frase qualquer: ').strip().upper()

print(frase.count("A"))
print('A posição da primeira letra "a" é {}'.format(frase.find('A') + 1))
 #pra contar a partir da posição 1 e não 0
print('A posição da última letra "a" é {}'.format(frase.rfind('A'))) 
#rfind = right find - procure a partir do lado direito e lfind, já sabe né?!
# a contagem vai incluir o espaço entre as palavras
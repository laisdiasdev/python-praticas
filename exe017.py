'''Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa'''

from math import sqrt
cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = sqrt(cat_oposto**2 + cat_adjacente**2)
print('O valor da hipotenusa desse triangulo retangulo é {}'.format(hipotenusa))

'''from math import hypot
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hi = hypot(co, ca)
print('O valor da hipotenusa desse triângulo retângulo é de {:.2f}'.format(hi))'''
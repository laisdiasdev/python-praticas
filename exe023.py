'''Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados'''
num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num //1000 % 10
print ("A unidade desse número é {}".format(u))
print("A dezena desse número é {}".format(d))
print("A centena dessse número é {}".format(c))
print("A milhar dessse número é {}".format(m))
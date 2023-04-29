'''Faça um programa que leia um ano qualquuer e mostre se ele é bissexto.'''
ano = int(input("Quantos dias têm este ano? "))
if ano == 366:
    print("Ual! Este é um ano bissexto.")
else:
    print("Este é um ano comum.")
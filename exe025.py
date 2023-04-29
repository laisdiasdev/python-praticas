'''Faca um programa que verifique se tem a palavra "Silva" no nome a ser lido'''
nome = str(input("Digite seu nome: ")).strip()
print('silva' in nome.lower())
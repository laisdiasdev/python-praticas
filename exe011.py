'''faca um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tintas necessária para pinta-la, sabendo que a cada litro de tinta, pinta uma area de 2 metros quadrados'''
largura = float(input('QUal a largura de sua parede? '))
altura = float(input('Qual a altura? '))
area = largura * altura
print('As dimensões de sua parede  são de {} x {} e de {}m² de área'.format(largura, altura, area))
tinta = area / 2
#esse 2 é o de 2 m²
print('para pintar sua parede, voce vai precisar de {}L de tinta'.format(tinta))
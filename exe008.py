#unidades de medida (distância) km hm dam m dm cm mm
distancia = float(input('Digite uma distância em metros: '))
km = distancia/1000
hm = distancia/100
dam = distancia/10
dm = distancia*10
cm = distancia*100
mm = distancia*1000
print('A distância em Km é {} \nEm Hm é {} \nEm Dam é {} \nEm Dm é {} \nEm Cm é {} \nEm Mm é {}'.format(km, hm, dam, dm, cm, mm))

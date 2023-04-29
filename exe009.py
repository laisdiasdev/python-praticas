#tabuada de um numero
#era pra ser uma sequ~encia de print, mas fiquei com preguiça e usi um laço for.
n = int(input('Digite um numero para ver sua tabuada: '))
for i in range(11):
    print('{} x {} = {}'.format(n, i, (n*i)))
'''O CLÁSSICO: Crie um programa que peça a nota de dois alunos e calcule a media. Depois mostre se ele ficou reprovado, aprovado ou de recuperação. Média abaixo de 5 é reprovado; entre 5 e 6,5 fica de recuperação; acima ou acima ou igual a 7 é aprovado.'''

nota1 = int(input('Qual foi sua primeira nota? '))
nota2 = int(input('Qual foi sua segunda nota? '))
media = (nota1+nota2)/2

if media >= 7:
    print('APROVADO(A)!')
elif media >= 5 and media <= 6.5:
    print('Você está de RECUPERAÇÃO!')
elif media < 5:
#PODE SER ELSE TBM
    print('REPROVADO!')
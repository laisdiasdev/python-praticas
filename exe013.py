'''descobrir o salario de uma pessoa com o reajuste de 15%'''
salario = float(input('Qual o seu salario atual? '))
reajuste = 15/100 * salario
novo_salario = salario + reajuste
print('Seu salário com o reajuste de 15% é de {:.2f} reais'.format(novo_salario))
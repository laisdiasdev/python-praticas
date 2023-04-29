n = int(input('Digite um número: '))
print('O sucessor de {} é {} e seu antecessor é \n{}.'.format(n, (n+1), (n-1)))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
resto = n1 % n2
print(' A soma de {} e {} é {}\n A subtração é {}\n A multiplicação é {}\n Divisão é {:.2f}\n Divisão inteira é {}\n E o resto da divisão é {}'.format(n1, n2, s, sb, m, d, di, resto))
#{:.2f} siginifica que após o ponto flutuante, quero apenas duas casas decimais
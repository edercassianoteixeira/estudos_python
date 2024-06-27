n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2
print('A soma é {}\na subtração é {}\na multiplicação é {}\na divisão é {:.2f}\n'.format(a, s, m, d), end='')
print('a elevação é {}\na divisão inteira é {}\ne o resto da divisão é {}'.format(p, di, r))

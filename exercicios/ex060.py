n1 = int(input('''Digite um numero para
calcular seu Fatorial: '''))
c = n1
f = 1
print('Calculando {}! = {}'.format(n1, n1), end='')
while c != 1:
    f *= c
    c -= 1
    print(' x {}'.format(c), end='')
print(' = {}'.format(f))

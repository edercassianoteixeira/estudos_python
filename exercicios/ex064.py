n = 0
soma = 0
total = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        total += 1
print('A soma dos {} números digitados foi {}'.format(total, soma))

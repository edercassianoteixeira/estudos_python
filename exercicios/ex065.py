r = 's'
total = soma = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    total += 1
    if total == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
print('Você digitou {} números, e a média foi {}'.format(total, (soma / total)))
print('O menor valor foi {}, e o maior foi {}.'.format(menor, maior))

soma = 0
aparece = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(c, end=' ')
        aparece += 1
        soma += c
print('\nA soma de todos os {} valores solicitados é, {}.'.format(aparece, soma))

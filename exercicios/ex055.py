maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso lido foi de {:.1f}kg'.format(maior))
print('O menor peso lido foi de {:.1f}kg'.format(menor))

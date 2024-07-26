numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
pares = []
impares = []
pos = 0
while pos < len(numeros):
    if numeros[pos] % 2 == 0:
        pares.append(numeros[pos])
    else:
        impares.append(numeros[pos])
    pos += 1
print('=-'*30)
print(f'A lista completa é {numeros}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')

numeros = [[], []]
for c in range(1, 8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0:
        numeros[0].append(v)
    else:
        numeros[1].append(v)
numeros[0].sort()
numeros[1].sort()
print('=-'*40)
print(f'Os valores pares deigitados foram: {numeros[0]}')
print(f'Os valores ímpares deigitados foram: {numeros[1]}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('=-'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()
for linha in range(0, 3):
    somacol += matriz[linha][2]
print('=-'*30)
print(f'''A soma dos valores pares é {somapar}.
A soma dos valores da terceira coluna é {somacol}.
O maior valor da segunda linha é {max(matriz[1])}.''')

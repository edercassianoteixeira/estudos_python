grupo = list()
pessoas = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = pessoas[1]
        menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]
    grupo.append(pessoas[:])
    pessoas.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('=-'*40)
print(f'Ao todo, você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

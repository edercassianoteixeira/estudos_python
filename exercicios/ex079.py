valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('=-'*30)
valores.sort()
print(f'Você digitou os valores {valores}')

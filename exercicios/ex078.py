valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-'*30)
print(f'A lista é {valores}.')
print(f'O maior digitado foi {max(valores)} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(posicao, end='...')
print(f'\nO menor digitado foi {min(valores)} nas posições ', end='')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(posicao, end='... ')

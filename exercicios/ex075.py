n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 not in n:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
print('Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')

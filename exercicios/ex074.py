from random import randint
print('Os valores sorteados foram: ', end='')
maior = menor = 0
tupla = ()
for c in range(0, 5):
    sorteio = randint(1, 10)
    tupla += (sorteio,)
    print(tupla[c], end=' ')
    c += 1
print(f'\nO maior valor sorteado foi {max(tupla)}.')
print(f'O menor valor sorteado foi {min(tupla)}.')

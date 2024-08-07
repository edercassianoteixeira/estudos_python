from random import randint
from time import sleep
cont = 1
jogo = []
megas = []
print('-'*40)
print(f'{'JOGO DA MEGA SENA':^40}')
print('-'*40)
sort = int(input('Quantos jogos você quer que eu sorteie? '))
while cont <= sort:
    for c in range(0, 6):
        nums = randint(1, 60)
        while True:
            if nums in jogo:
                nums = randint(1, 60)
            else:
                jogo.append(nums)
                break
    jogo.sort()
    megas.append(jogo[:])
    jogo.clear()
    cont += 1
print('=-'*5, f' SORTEANDO {sort} JOGOS ', '=-'*5)
for i, l in enumerate(megas):
    print(f'JOGO {i+1}: {l}.')
    sleep(1)
print('=-'*6, '< BOA SORTE!! >', '=-'*6)

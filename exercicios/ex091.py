from random import randint
from time import sleep
from operator import itemgetter
jogos = dict()
ordem = list()
print('Valores sorteados:')
sleep(1)
for c in range(1, 5):
    numero = randint(1, 6)
    print(f'jogador{c} tirou {numero} no dado.')
    sleep(1)
    jogos[f'jogador{c}'] = numero
print('=-'*30)
print(f'{"== RANKING DOS JOGADORES ==":^34}')
sleep(1)
ordem = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ordem):
    print(f'{'':<3}{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

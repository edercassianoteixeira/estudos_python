from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada: '))
if jogada < 0 or jogada > 2:
    print('\033[31m[ERRO EM SUA JOGADA]. Tente novamente.\033[m')
else:
    print('JO')
    sleep(0.8)
    print('KEN')
    sleep(0.8)
    print('PO!!!')
    sleep(0.8)
    print('-='*15)
    print('COMPUTADOR jogou {}'.format(itens[computador]))
    print('JOGADOR jogou {}'.format(itens[jogada]))
    print('-='*15)
    if jogada == 0:
        if computador == 0:
            print('EMPATE')
        elif computador == 1:
            print('COMPUTADOR GANHOU')
        else:
            print('JOGADOR GANHOU')
    elif jogada == 1:
        if computador == 0:
            print('JOGADOR GANHOU')
        elif computador == 1:
            print('EMPATE')
        else:
            print('COMPUTADOR GANHOU')
    elif jogada == 2:
        if computador == 0:
            print('COMPUTADOR GANHOU')
        elif computador == 1:
            print('JOGADOR GANHOU')
        else:
            print('EMPATE')

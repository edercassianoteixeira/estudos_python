from random import randint
print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
vence = 0
while True:
    print('=-'*30)
    ncomputador = randint(0, 10)
    njogador = int(input('Diga um valor: '))
    poi = ' '
    while poi not in 'PpIi':
        poi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    soma = njogador + ncomputador
    if soma % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    print('--'*30)
    print(f'Você jogou {njogador} e o computador {ncomputador}. Total de {soma} deu {res}')
    print('--'*30)
    if poi != res[0]:
        print('VOCÊ PERDEU!')
        break
    vence += 1
    print('VOCÊ VENCEU!')
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vence} vezes.')
print('=-'*30)

from time import sleep


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cor[2], end='')
    help(com)
    print(cor[0], end='')
    sleep(2)


def titulo(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~'*tam)
    print(f'{msg:^{tam}}')
    print('~'*tam)
    print(cor[0], end='')
    sleep(1)


# Programa Principal
cor = ['\033[m',  # 0 SEM COR
       '\033[1;30;44m',  # 1 AZUL
       '\033[1;30;43m',  # 2 AMARELO
       '\033[1;37;40m',  # 3 PRETO
       '\033[1;30;107m',  # 4 BRANCO
       ]
coma = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    coma = str(input('Função ou Biblioteca > '))
    if coma.upper() == 'FIM':
        break
    else:
        ajuda(coma)
titulo('ATÉ LOGO', 3)

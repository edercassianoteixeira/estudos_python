from time import sleep


def contagem(i, f, p):
    if p == 0:
        p += 1
        print(f'\033[1;41;30mPasso inválido, passo será considerado 1!\033[m')
        sleep(2.5)
    if p < 0:
        p *= -1
        print(f'\033[1;41;30mPasso será considerado positivo!\033[m')
        sleep(2.5)
    print('=-'*20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)
    if i <= f:
        while i <= f:
            print(i, end=' ')
            sleep(0.5)
            i += p
    else:
        while i >= f:
            print(i, end=' ')
            sleep(0.5)
            i -= p
    print('Fim!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('=-'*20)
print('Agora é sua vez de personalizar a contagem!')
sleep(2.5)
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contagem(i=ini, f=fim, p=pas)

from time import sleep


def analise(*num):
    print('=-'*30)
    sleep(1)
    print('Analisando os valores passados...')
    sleep(1.5)
    for n in num:
        print(n, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(1.5)
    if len(num) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(num)}.')


analise(2, 9, 4, 5, 7, 1)
analise(4, 7, 0)
analise(1, 2)
analise(6)
analise()

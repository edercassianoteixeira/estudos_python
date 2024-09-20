from time import sleep


def sortear(lis):
    from random import randint
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        while True:
            n = randint(1, 10)
            if n not in lis:
                print(n, end=' ')
                sleep(0.5)
                lis.append(n)
                break
    print('PRONTO!')
    sleep(0.5)


def somapar(lis):
    soma = 0
    for n in lis:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lis}, temos {soma}')


lista = list()
sortear(lista)
somapar(lista)

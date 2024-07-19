while True:
    cont = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    print('-'*40)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')

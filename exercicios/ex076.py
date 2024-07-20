print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
c = 0
while c != len(tupla):
    if c % 2 == 0:
        print(f'{tupla[c]:.<30}', end='R$ ')
    else:
        print('{:>6.2f}'.format(tupla[c]))
    c += 1
print('-'*40)

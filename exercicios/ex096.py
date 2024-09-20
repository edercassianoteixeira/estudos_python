def comeco(msg):
    print()
    print(f'{msg:^21}')
    print('-' * 21)


def area(lar, com):
    a = lar * com
    print('-' * 21)
    print(f'A área de um terreno {l} x {c} é de {a}m²')


# Programa Principal
comeco('CONTROLE DE TERRENO')
l = float(input('Largura [m]: '))
c = float(input('Comprimennto [m]: '))
area(lar=l, com=c)

def metade(preco=0):
    res = preco / 2
    return moeda(res)


def dobro(preco=0):
    res = preco * 2
    return moeda(res)


def aumentar(preco=0, taxa=0):
    res = preco + (taxa / 100 * preco)
    return moeda(res)


def diminuir(preco=0, taxa=0):
    res = preco - (taxa / 100 * preco)
    return moeda(res)


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')


def resumo(p, taxaa, taxad):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p)}')
    print(f'Metade do preço: \t{metade(p)}')
    print(f'{taxaa}% de aumento: \t{aumentar(p, taxaa)}')
    print(f'{taxad}% de redução: \t{diminuir(p, taxad)}')
    print('-'*30)

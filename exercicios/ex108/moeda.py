def metade(preco=0):
    res = preco / 2
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def aumentar(preco=0, taxa=0):
    res = preco + (taxa / 100 * preco)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (taxa / 100 * preco)
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

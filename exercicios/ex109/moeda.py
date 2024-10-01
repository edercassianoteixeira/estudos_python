def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (taxa / 100 * preco)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (taxa / 100 * preco)
    return res if not formato else moeda(res)


def moeda(preco=0.0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

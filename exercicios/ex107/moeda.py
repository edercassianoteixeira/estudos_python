def metade(preco):
    res = preco / 2
    return res


def dobro(preco):
    res = preco * 2
    return res


def aumentar(preco, a):
    res = preco + (a / 100 * preco)
    return res


def diminuir(preco, d):
    res = preco - (d / 100 * preco)
    return res

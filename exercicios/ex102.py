def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número.
    """
    print('-'*20)
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(end=' x ')
            else:
                print(end=' = ')
    return f


# Programa Principal
print(fatorial(5, True))
help(fatorial)

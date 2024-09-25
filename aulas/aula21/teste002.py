# DOCSTRINGS
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    while i <= f:
        print(i, end=' ')
        i += p
    print('Fim!')


contador(2, 10, 2)

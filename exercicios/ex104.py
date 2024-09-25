def leiaint(msg):
    """
    -> Lê um número e diz se é inteiro.
    :param msg: O valor a ser lido.
    :return: Quando digitado o número inteiro.
    """
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return valor
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

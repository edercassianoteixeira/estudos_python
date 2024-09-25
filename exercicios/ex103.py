def jogador(n, g):
    """
    -> Mostra ficha de um jogador.
    :param n: Nome do jogador.
    :param g: Gols do jogador.
    :return: A ficha do jogador.
    """
    return f'O jogador {n}, fez {g} gol(s) no campeonato.'


# Programa Principal
print('-'*30)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: ')).strip()
if not gols.isnumeric():
    gols = 0
if nome.strip() == '' or nome.isnumeric():
    nome = '<desconhecido>'
print(jogador(nome, gols))

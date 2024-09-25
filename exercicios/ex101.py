def voto(n):
    """
    -> Calcula idade e diz a situçào do voto.
    :param n: Ano de nascimento.
    :return: Idade e situação de voto.
    """
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - n
    if idade <= 15:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa Principal
print('-'*30)
print(voto(int(input('Em que ano você nasceu? '))))

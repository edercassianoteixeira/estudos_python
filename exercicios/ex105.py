def notas(*n, sit=False):
    """
    -> Analisa notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias notas).
    :param sit: (opcional) Indica se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situaçào da turma.
    """
    print('-'*30)
    alunos = dict()
    alunos['total'] = len(n)
    alunos['maior'] = max(n)
    alunos['manor'] = min(n)
    alunos['média'] = sum(n) / len(n)
    if sit:
        if alunos['média'] < 5:
            alunos['situação'] = 'RUIM'
        elif alunos['média'] < 8:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'BOA'
    return alunos


# Progarma Principal
resp = notas(8, 7, sit=True)
print(resp)
print()
help(notas)

from datetime import date
nascido = int(input('Informe o ano de nascimento: '))
atual = date.today().year
idade = atual - nascido
print('Quem nasceu em {} tem {} anos em {}.'.format(nascido, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta = 18 - idade
    ano = atual + falta
    print('Ainda faltam {} anos para o alistamento.'.format(falta))
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    foi = idade - 18
    ano = atual - foi
    print('Você já deveria ter se alistado há {} anos.'.format(foi))
    print('Seu alistamento foi em {}.'.format(ano))

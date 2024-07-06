n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média é de {:.1f}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está APROVADO.')
elif m >= 5:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')

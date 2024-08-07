lista = []
pessoas = []
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Nota 1: ')))
    pessoas.append(float(input('Nota 2: ')))
    lista.append(pessoas[:])
    pessoas.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('=-'*40)
print(f'{"Nº":<4} {"NOME":<10} {"NOTA":>8}')
print('-'*30)
for i, p in enumerate(lista):
    media = (p[1] + p[2]) / 2
    print(f'{i:<4} {p[0]:<10} {media:>8.1f}')
while True:
    print('-'*35)
    r = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if r == 999:
        print('FINALIZANDO...')
        break
    for i, p in enumerate(lista):
        if r == i:
            print(f'Notas de {p[0]} são [{p[1]}, {p[2]}].')
print('<<<<< VOLTE SEMPRE >>>>>')

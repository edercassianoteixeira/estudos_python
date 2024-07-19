maior = homem = fmenos = 0
while True:
    print('-'*40)
    print('    CADASTRE UMA PESSOA')
    print('-'*40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*40)
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        fmenos += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res in 'Nn':
        break
print('-'*40)
print(f'''Total de pessoas com mais de 18 anos: {maior}.
Ao todo temos {homem} homens cadastrados.
E temos {fmenos} mulheres com menos de 20 anos.''')

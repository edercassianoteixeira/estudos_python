pessoa = dict()
grupo = list()
media = soma = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if res in 'SN':
            break
        print('ERRO, digite apenas S ou N.')
    if res == 'N':
        break
print('=-'*30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas')
media = soma / len(grupo)
print(f'B) A média de idade é de {media:5.1f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(p["nome"], end=' ')
print()
print('D) Lista das pessoas que estão acima da média de idade: ')
for p in grupo:
    if p['idade'] >= media:
        print(end='     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

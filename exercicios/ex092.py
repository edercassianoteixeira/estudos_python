from datetime import date
atual = date.today().year
pessoa = {'nome': str(input('Nome: ')).strip(),
          'idade': int(input('Ano de Nascimento: ')),
          'ctps': int(input('Carteira de Trabalho (0 se não tiver): '))}
pessoa['idade'] = atual - pessoa['idade']
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = ((pessoa['contratação'] + 35) - atual) + pessoa['idade']
print('=-'*30)
for k, v in pessoa.items():
    print(f'{'':<3} - {k} tem o valor {v}')

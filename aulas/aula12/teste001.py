nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Éder':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é popular no Brasil.')
elif nome in 'Camila Sirius':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

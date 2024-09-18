jogador = dict()
time = list()
while True:
    gol = list()
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gol.append(int(input(f'{'':<3}Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = gol
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    while True:
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if res in 'NS':
            break
        print('ERRO, digite apenas S ou N.')
    if res == 'N':
        break
print('=-'*30)
print('cod', end=' ')
for k in jogador.keys():
    print(f'{k:<20}', end='')
print()
print('--'*30)
for i, v in enumerate(time):
    print(f'{i:>2}', end='  ')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('--'*30)
while True:
    busca = int(input('Qual jogador deseja saber os dados? [999 para parar]: '))
    print('--'*30)
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'ERRO, não há jogador com código {busca}')
        print('--'*30)
    else:
        print(f'--Lista de gols do jogador {time[busca]["nome"]}:')
        for i, v in enumerate(time[busca]['gols']):
            print(f'{'':<3}Na partida {i + 1} {time[busca]["nome"]} fez {v} gols.')
        print('--'*30)
print('<< VOLTE SEMPRE >>')

jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gol.append(int(input(f'{'':<3}Quantos gols na partida {c}? ')))
jogador['gols'] = gol
jogador['total'] = sum(gol)
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(gol):
    print(f'{'':<3}=> Na parida {p}: fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

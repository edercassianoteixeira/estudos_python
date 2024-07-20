tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'São Paulo', 'Bahia',
          'Cruzeiro', 'Fortaleza', 'Athletico-PR', 'Vasco da Gama', 'Bragantino',
          'Atlético-MG', 'Juventude', 'Internacional', 'Criciúma', 'Cuiabá',
          'EC Vitória', 'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense')
print('-='*30)
print(f'Tabela do Brasileirão [19/07/2024]: {tabela}')
print('-='*30)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('-='*30)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-='*30)
print(f'Tabela em ordem alfabética: {sorted(tabela)}')
print('-='*30)
print(f'O Athletico-PR, time do meu estado, está na {tabela.index('Athletico-PR') + 1}ª posição.')

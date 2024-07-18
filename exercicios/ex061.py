print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(pt, end=' → ')
    pt += razao
    c += 1
print('FIM')

print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
pt = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for c in range(0, 10):  #decimo termo é = pt + (10 - 1) * razao
    print(pt, end=' → ')
    pt += razao
print('ACABOU')

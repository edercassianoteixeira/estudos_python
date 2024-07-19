print('='*30)
print(f'{'BANCO DEVTX':^30}')
print('='*30)
n = int(input('Qual valor deseja sacar: R$'))
while True:
    if n >= 50:
        tot50 = n // 50
        print(f'Total de {tot50} cédulas de R$50.00')
        n %= 50
    if n >= 20:
        tot20 = n // 20
        print(f'Total de {tot20} cédulas de R$20.00')
        n %= 20
    if n >= 10:
        tot10 = n // 10
        print(f'Total de {tot10} cédulas de R$10.00')
        n %= 10
    if n >= 1:
        tot1 = n // 1
        print(f'Total de {tot1} moedas de R$1.00')
        n %= 1
    if n == 0:
        break
print('='*30)
print('Volte sempre ao BANCO DEVTX! Tenha um bom dia!')

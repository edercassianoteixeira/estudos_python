total = maismil = pbarato = 0
nbarato = ''
print('-'*30)
print('     LOJA SUPER BARATÃO')
print('-'*30)
while True:
    pro = str(input('Nome do produto: ')).strip()
    pre = float(input('Preço: R$'))
    if total == 0:
        pbarato = pre
    if pre < pbarato:
        pbarato = pre
        nbarato = pro
    total += pre
    if pre > 1000:
        maismil += 1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'''O total da compra foi R${total:.2f}
Temos {maismil} produtos custando mais de R$1000.00
O produto mais barato foi {nbarato} que custa R${pbarato:.2f}''')

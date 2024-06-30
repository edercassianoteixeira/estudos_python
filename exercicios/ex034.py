sal = float(input('Informe o salário atual: R$'))
if sal > 1250:
    aum = sal * 0.10 + sal
else:
    aum = sal * 0.15 + sal
print('O funcionário que recebia R${:.2f}, passará a receber R${:.2f}'.format(sal, aum))

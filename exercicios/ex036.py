casa = float(input('Qual o valor da casa: R$'))
sal = float(input('Quanto é o salário: R$'))
anos = int(input('Quantos anos irá financiar: '))
pres = casa / (anos * 12)
pormin = sal * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, pres))
if pres <= pormin:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

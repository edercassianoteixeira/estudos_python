valor = float(input('Informe o valor do produto: R$'))
d = valor - valor * 0.05
print('O produto que cutava R${:.2f} com o desconto de 5%, passa a custar R${:.2f}'.format(valor, d))

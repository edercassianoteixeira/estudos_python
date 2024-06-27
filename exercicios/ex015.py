d = int(input('Informe o total de dias: '))
km = float(input('Informe o total de km rodados: '))
total = d * 60 + km * 0.15
print('Após {} dias com o carro alugado, tendo rodado {}km o valor a ser pago é R${:.2f}'.format(d, km, total))

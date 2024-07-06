peso = float(input('Informe o peso: (kg) '))
alt = float(input('Informe a altura: (m) '))
imc = peso / (alt ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está na faixa de SUBPESO')
elif 18.5 <= imc < 25:
    print('Você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está na faixa de SOBREPESO')
elif 30 <= imc < 40:
    print('Você está na faixa de OBESIDADE')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA')

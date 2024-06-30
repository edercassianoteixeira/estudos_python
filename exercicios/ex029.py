vel = int(input('Informe a velocidade atingida: '))
multa = (vel - 80) * 7
if vel > 80:
    print("""Multado! Voc6e excedeu o limite permitido que é 80Km/h.
Você deve pagar uma multa de R${:.2f}!""".format(multa))
print('Tenha um bom dia! Dirija com segurança!')

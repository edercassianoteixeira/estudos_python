km = float(input('Informe quantos KM você ira viajar: '))
print('Você está prestes a iniciar uma viagem de {:.1f}'.format(km))
if km > 200:
    valor = km * 0.45
else:
    valor = km * 0.5
print('E o preço da sua passagem será de R${:.2f}'.format(valor))

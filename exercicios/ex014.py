c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
k = c + 273.15
print('A temperatura de {:.1f}ºC convertida fica, {:.1f}ºF ou {:.2f}K'.format(c, f, k))

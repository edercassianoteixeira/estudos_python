a = float(input('Informe a altura da parede: '))
l = float(input('Informe a largura da parede: '))
area = a * l
litros = area / 2
print('Sua parede tem {:.2f}m², e você terá que usar {:.2f}l de tinta'.format(area, litros))

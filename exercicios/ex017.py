from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('Com base nos dados, a hipotenusa mede {:.2f}'.format(hypot(co, ca)))

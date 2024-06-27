from math import sin, cos, tan, radians
a = float(input('Informe o ângulo que deseja calcular: '))
print('O ângulo de {} tem o seno de {:.2f}'.format(a, sin(radians(a))))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a, cos(radians(a))))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, tan(radians(a))))

soma = 0
quantos = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor : '.format(c)))
    if n % 2 == 0:
        soma += n
        quantos += 1
print('Você informou {} números PARES, a soma deles foi {}.'.format(quantos, soma))

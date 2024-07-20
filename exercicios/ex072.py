extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        print('Tente novamente.', end=' ')
        n = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[n]}.')
    res = ' '
    while res not in 'SN':
        res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^30}')

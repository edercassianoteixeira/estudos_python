from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palp = int(input('Qual o seu palpite? '))
tent = 1
while palp != computador:
    if palp < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    tent += 1
    palp = int(input('Qual o seu palpite? '))
print('Acertou com {} tentativas. Parabéns!'.format(tent))

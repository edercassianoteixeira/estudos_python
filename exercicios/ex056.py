media = 0
maior = 0
menor = 0
homemvelho = ''
for c in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(c), '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if sexo == 'M' and idade > maior:
        maior = idade
        homemvelho = nome
    if sexo == 'F' and idade < 20:
        menor += 1
media = media / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos, e se chama {}.'.format(maior, homemvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menor))

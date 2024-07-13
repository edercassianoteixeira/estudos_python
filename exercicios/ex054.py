from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasceu = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if atual - nasceu >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))

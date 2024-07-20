lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'

for comida in lanche:
    print(f'Eu vor comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vor comer {comida} na posição {pos}')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('Comi pra caramba!')

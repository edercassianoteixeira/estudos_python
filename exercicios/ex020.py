from random import shuffle
a1 = str(input('Informe o nome do primeiro aluno: '))
a2 = str(input('Informe o nome do segundo aluno: '))
a3 = str(input('Informe o nome do terceiro aluno: '))
a4 = str(input('Informe o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem das apresentações é \n{}'.format(lista))

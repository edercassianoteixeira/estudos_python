exp = list()
exp.append(str(input('Digite uma expressão: ')).strip())
if exp[0].count('(') == exp[0].count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

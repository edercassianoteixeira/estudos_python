v1 = int(input('Informe o primeiro número: '))
v2 = int(input('Informe o segundo número: '))
v3 = int(input('Informe o terceiro número: '))
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O menor número foi {}'.format(menor))
print('O maior número foi {}'.format(maior))

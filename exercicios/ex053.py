frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverso = ''  #ou = junta[::-1]
for l in range(len(junta) - 1, -1, -1):
    inverso += junta[l]
print('O inverso de {} é {}'.format(junta, inverso))
if junta == inverso:
    print('A frase É UM PALÍNDROMO!')
else:
    print('A frase NÃO É UM PALÍNDROMO!')

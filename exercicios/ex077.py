palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra.lower():
        if letra in 'aieou':
            print(letra, end=' ')

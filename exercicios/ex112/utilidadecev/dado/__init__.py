def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada == '' or entrada.isalpha():
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)

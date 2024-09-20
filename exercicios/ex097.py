def mensagem(msg):
    tam = len(msg)
    linha = tam + 4
    print('~'*linha)
    print(f'{msg:^{linha}}')
    print('~'*linha)


# Programa Principal
mensagem('PROGRAMANDO EM PYTHON')
mensagem('DEV TX')

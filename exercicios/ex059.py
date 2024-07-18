from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {}, é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação entre {} x {}, é {}.'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 == n2:
            print('Os números {} e {}, são iguais.'.format(n1, n2))
        else:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print('O maior entre {} e {}, é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    sleep(1.3)
    print('_-'*20)
print('Fim do programa! Volte sempre!')

print('='*10, 'LOJAS TEIXEIRA', '='*10)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque.
[ 2 ] à vista cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    desconto = preco - preco * 0.10
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desconto))
elif opcao == 2:
    desconto = preco - preco * 0.05
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desconto))
elif opcao == 3:
    dividido = preco / 2
    print('Sua compra de R${:.2f} não sofre nenhuma alteração no valor.'.format(preco))
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(dividido))
elif opcao == 4:
    parcela = int(input('Quantas parcelas: '))
    juros = preco + preco * 0.20
    dividido = juros / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcela, dividido))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, juros))
else:
    print('[ERRO]. Tente novamente!')

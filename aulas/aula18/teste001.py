teste = list()
teste.append('Éder')
teste.append(21)
galera = list()
galera.append(teste[:])
teste[0] = 'Camila'
teste[1] = 22
galera.append(teste[:])
print(galera)

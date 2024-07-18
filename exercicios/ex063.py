print('-'*40)
print('     SEQUÊNCIA DE FIBONACCI')
print('-'*40)
termos = int(input('Quantos termos você quer mostrar? '))
c = 3
t1 = 0
t2 = 1
print('~'*40)
print('{} → {}'.format(t1, t2), end=' → ')
while c <= termos:
    t3 = t1 + t2
    print(t3, end=' → ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
print('~'*40)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[1;30;107mPRIMEIRO\033[m valor é maior.')
elif n2 > n1:
    print('O \033[1;30;107mSEGUNDO\033[m valor é maior.')
else:
    print('Os dois os valores são \033[1;30;107mIGUAIS\033[m.')

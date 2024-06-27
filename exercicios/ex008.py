m = int(input('Informe uma distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A distância de {}m convertida fica.'.format(m))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm\n'.format(km, hm, dam, dm, cm, mm))

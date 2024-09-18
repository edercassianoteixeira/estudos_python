aluno = dict()
aluno["nome"] = str(input('Nome: ')).strip()
aluno["média"] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["média"] < 7:
    aluno["situação"] = 'Reprovado'
elif aluno["média"] >= 7:
    aluno["situação"] = 'Aprovado'
print('=-'*30)
for k, v in aluno.items():
    print(f'{"":<3}- {k} é igual a {v}')

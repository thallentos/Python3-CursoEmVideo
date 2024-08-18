aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média de {}: '.format(aluno['Nome'])))

if (aluno['Média']) >= 7:
    aluno['Situação'] = 'Aprovado'
elif 3 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print(f'-='*30)
for k,v in aluno.items():
    print('- {} é igual a {}'.format(k, v))

# referente à aula 19
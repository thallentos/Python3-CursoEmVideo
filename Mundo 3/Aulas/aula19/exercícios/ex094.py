dados_geral = list()
dados_individuais = dict()
soma_idade = média_idade = 0

while True:
    print(f'-'*10)
    dados_individuais.clear()
    dados_individuais['nome'] = str(input('Nome: '))
    while True:
        dados_individuais['sexo'] = str(input('Sexo: [M/F] '))[0].upper()
        if dados_individuais['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite M ou F.')
    dados_individuais['idade'] = int(input('Idade: '))
    soma_idade += dados_individuais['idade']
    dados_geral.append(dados_individuais.copy())
    while True:
        pergunta = str(input('Quer continuar? [S/N] '))[0].upper()
        if pergunta in 'SN':
            break
        else:
            print('ERRO! Por favor, digite S ou N.')
    if pergunta in 'N':
        break

print(f'-='*30)
#print(dados_geral)
print('A) O grupo tem {} pessoa(s).'.format(len(dados_geral)))

média_idade = soma_idade/len(dados_geral)
print('B) A média de idade é de {:4.2f}.'.format(média_idade))

print('C) As mulheres cadastradas foram ', end='')
for pessoa in dados_geral:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}', end=' ')
print()

print('D) Lista das pessoas que estão acima da média: ')
for pessoa in dados_geral:
    if pessoa['idade'] > média_idade:
        print('     ', end='')
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<<<|_ENCERRADO_|>>>')
# referente à aula 19
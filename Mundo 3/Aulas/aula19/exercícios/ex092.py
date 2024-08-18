'''
nome
idade = ano atual (2024) - ano de nascimento
ctps if ctps.value == 0:
    mostre os dados
else:
    ano de contratacao
    salario

    mostrar:
        com quantos anos a pessoa
        vai se aposentar (35 anos, independente do sexo)

'''
from datetime import datetime
dados = dict()
ano_atual = datetime.now().year

dados['Nome'] = str(input('Nome: '))
dados['Idade'] = int(input('Ano de Nascimento: '))
dados['Idade'] = ano_atual - dados['Idade']
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem) : '))


if (dados['CTPS']) != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] =  dados['Idade'] + 35
    #dados['Aposentadoria'] =  dados['Idade'] + ((dados['Contratação'] + 35) - ano_atual)

print(f'-='*30)
#print(dados)
for keys, values in dados.items():
    print('  - {} tem o valor {}'.format(keys, values))

# referente à aula 19
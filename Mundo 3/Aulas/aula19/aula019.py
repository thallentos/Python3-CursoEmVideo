#'''
# >>> Nomeando um Dicionário
#dados = dict() # ou dados = {}

# >>> Colocando elementos na estrutura de Dicionário
dados = \
    {
        'nome': 'Thalles',
        'idade': 19
    }

# Printando esses dados
print(dados['nome'])
print(dados['idade'])

# >>> Adicionando novos elementos!
# No caso de Dicionário, o 'append()' não funciona
# Por isso, se usa a estrutura abaixo:
dados['sexo'] = 'M'

# >>> Removendo elementos existentes
#del dados['idade']

# >>> Tipos de elementos
print(dados.values()) # vai me retornar: Thalles, 19 e M
print(dados.keys()) # vai me retornar: nome, idade, sexo
print(dados.items()) # vai me retornar: values e keys

# Exemplo para a explicação a seguir:
filme = \
    {
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
    }

# >>> Estrutura de repetição que mostra
# todas as keys e values
for k,v in filme.items():
    print('O {} é {}'.format(k, v))

# >>> Criando dicionários dentro de uma lista
brasil = [] # nomeei uma lista
estado1 = \
    {
        'uf': 'Espirito Santo',
        'sigla': 'ES'
    }
estado2 = \
    {
        'uf': 'Rio de Janeiro',
        'sigla': 'RJ'
    }

# Adicionando esses novos dicionários na lista 'brasil'
brasil.append(estado1)
brasil.append(estado2)

# Printando as características dessa lista
print(estado1) # mostrando os items de estado1
print(estado2) # mostrando os items de estado2
print(brasil) # mostrando os items de da lista completa (estado1 e estado2)
print(brasil[0]) # mostrando os items de estado1
print(brasil[0]['uf']) # mostrando a 'uf' de estado1

# >>> Usando laços e deixando o usuário inserir
# as 'uf' e as 'siglas'
brasil = list()
estado = dict()

for two in range (0, 2):
    estado['uf'] = str(input('\nUnidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # isso é muito importante
        # para ficar direitinho
for est in brasil:
    for val in est.values():
        print(val, end=' ')

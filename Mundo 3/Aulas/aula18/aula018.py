"""
galera = [['João', 12], ['Gabriela', 22]]
print(galera[1][1])
print(galera[0][0])
print(galera[1])
"""

pessoas = []
dados = []

while True:
    dados.append(str(input('\nDigite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? [S/N] '))
    if (continuar in 'Nn'):
        break

print(pessoas)

'''
nome do jogador
quantas partidas ele jogou

loop for indice in range (0, partidas que ele jogou +1)
    quantos gols fez na partida {indice}
    guardar num dicionario:
        quantidade de gols feitos na partida
            correspondente
    total de gols
'''

dados = dict()
gols_por_partida = []

dados['nome'] = str(input('Nome do Jogador: '))
qtd_partida = int(input('Quantas partidas {} jogou? '.format(dados['nome'])))
for partida in range (1, qtd_partida+1):
    pergunta = int(input('  Quantos gols na partida {}? '.format(partida)))
    gols_por_partida.append(pergunta)
    partida += 1

dados['gols'] = gols_por_partida
dados['total'] = sum(gols_por_partida)
    # isso está somando todas as posições
    # da lista 'gols_por_partida', e não
    # os valores dela. Fica ligado!!!

print(f'-='*30)
print(dados)
print(f'-='*30)
for keys, values in dados.items():
    print('O campo {} tem o valor {}.'.format(keys, values))
print(f'-='*30)
print('O jogador {} jogou {} partida(s).'.format(dados['nome'], len(dados['gols'])))
# print('O jogador {} jogou {} partida(s).'.format(dados['nome'], qtd_partida))
for indice, gol in enumerate(dados['gols']):
    print('     => Na partida {}, fez {} gol(s).'.format(indice+1, gol))

print('Foi um total de {} gol(s).'.format(dados['total']))
# referente à aula 19
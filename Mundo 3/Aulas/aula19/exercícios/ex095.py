# Fiz exatamente o que o Gustavo Guanabara
# pediu, copiei literalmente o código inteiro
# do exercício 93 para fazer as alterações

time = list()
dados = dict()
partidas = list()

while True:
    print('-'*10)
    dados.clear()
    dados['nome'] = str(input('Nome do Jogador: '))
    qtd_partida = int(input('Quantas partidas {} jogou? '.format(dados['nome'])))
    partidas.clear()
    for g in range (1, qtd_partida+1):
        partidas.append(int(input('  Quantos gols na partida {}? '.format(g))))

    dados['gols'] = partidas[:]
    dados['total'] = sum(partidas)
        # isso está somando todas as posições
        # da lista 'gols_por_partida', e não
        # os valores dela. Fica ligado!!!

    time.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] '))[0].upper()
        if continuar in 'SN':
            break
        else:
            print('ERRO! Responda apenas com S ou N')
    if continuar == 'N':
        break

print('-='*30)
print('cód ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for key, value in enumerate(time):
    print(f'{key:>3} ', end='')
    for t in value.values():
        print(f'{str(t):<15}', end='')
    print()
print(f'-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com código da {}!'.format(busca))
    else:
        print(' -- Levantamento do jogador {}: '.format(time[busca]['nome']))
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    No jogo {i+1} fez {g} gol(s).')
    print('-'*40)
print('<< Volte sempre >>')

# referente à aula 19
times = ('Flamengo CAMPEÃO (71 pontos)', 'Internacional (70 pontos)', 'Atlético-MG (68 pontos)',
         'São Paulo (66 pontos)', 'Fluminense (64 pontos)', 'Grêmio (59 pontos)',
         'Palmeiras (58 pontos)', 'Santos (54 pontos)', 'Athletico-PR (53 pontos)',
         'Bragantino (53 pontos)', 'Ceará (52 pontos)', 'Corinthians (51 pontos)',
         'Atlético-GO (50 pontos)', 'Bahia (44 pontos)', 'Sport (42 pontos)',
         'Fortaleza (41 pontos)', 'Vasco (41 pontos)', 'Goiás (37 pontos)',
         'Coritiba (31 pontos)', 'Botafogo (27 pontos)')

print('\n1ª Parte')
print('====== Tabela Geral ======')
for t, time in enumerate(times):
    print('{}º lugar: {}'.format(t+1, time))

print('----------x----------')

print('\n\n2ª Parte')
print('====== 5 Primeiros Colocados ======')
for t, time in enumerate(times[0:5]):
    print('{}º lugar: {}'.format(t+1, time))

print('----------x----------')

print('\n\n3ª Parte')
print('====== 4 Últimos Colocados ======')
for t, time in enumerate(times[19:15:-1]):
    print('{}º lugar: {}'.format(t+1, time))

print('----------x----------')

print('\n\n4ª Parte')
print('====== Ordem Alfabética ======')
for t, time in enumerate(sorted(times)):
    print('{}º time: {}'.format(t+1, time))

print('----------x----------')

print('\n\n5ª Parte')
print(('''Quantas vezes aparece o time Flamengo? {}x'''.format(times.count('Flamengo CAMPEÃO (71 pontos)'))))

print('----------x----------')

print('\n\n6ª Parte')
print(('''Em que posição da tabela está o Flamengo?
Resposta: Posição {}'''.format(times.index('Flamengo CAMPEÃO (71 pontos)')+1)))
# referente à aula 16

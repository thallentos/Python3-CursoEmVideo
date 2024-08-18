from random import randint
from time import sleep
from operator import itemgetter

valores_jogados = dict()

valores_jogados = \
    {
        'jogador1': randint(1,6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
    }

ranking = list()

'''
Também pode ser feito do jeito abaixo
valores_jogados['jogador1'] = randint(1,6)
valores_jogados['jogador2'] = randint(1,6)
valores_jogados['jogador3'] = randint(1,6)
valores_jogados['jogador4'] = randint(1,6)
'''

print('Valores sorteados: ')
for keys, values in valores_jogados.items():
    print('\tO {} tirou {}'.format(keys, values))
    sleep(1)

ranking = sorted(valores_jogados.items(), key= itemgetter(1), reverse= True)
    #print(ranking)
print('-='*30)
for indice, valor in enumerate(ranking):
    # precisa ser usado o 'enumerate', porque o 'ranking'
    # é uma lista, e não um dicionário. Senão
    # usaríamos o 'in valores_jogados.items()'
    print('{}º lugar: {} com {}.'.format(indice+1, valor[0], valor[1]))
    sleep(1)
# referente à aula 19
import random as rd
from time import sleep # bibloteca que conta
print('-=-' * 10)
print('Estou pensando num número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
num = int(input('Em que número estou pensando? (hehe): '))
print('ANALISANDOOOO...')
sleep(3)

num_aleatorio = rd.randint(0,5)

if (num == num_aleatorio):
    print('AFF, PERDI. PURA SORTE. QUERO VER ME VENCER DE NOVO')
else:
    print('GANHEEEI. Eu pensei no {}, seu burro'.format(num_aleatorio))
# referente à aula 10

import random
from random import randint
from time import sleep # bibloteca que conta
print('-=-' * 10)
print('Estou pensando num número entre 0 e 10. Tente adivinhar...')
print('-=-' * 10)
num = 0
num_aleatorio = 1
cont = 0
while (num != num_aleatorio):
    num = int(input('\nEm que número estou pensando? (hehe): '))
    print('ANALISANDOOOO...')
    sleep(3)

    num_aleatorio = random.randint(0,10)

    if (num == num_aleatorio):
        print('AFF, PERDI. PURA SORTE. QUERO VER ME VENCER DE NOVO')
        cont += 1
        print('Você deu {} palpite(s) até acertar'.format(cont))
        break
    else:
        print('GANHEEEI. Eu pensei no {}, seu burro. Tente novamente'.format(num_aleatorio))
        cont += 1
# referente à aula 14

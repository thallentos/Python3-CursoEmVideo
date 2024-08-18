print('-'*18)
print('   Par ou Impar')
print('-'*18)
vitorias = 0
from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    while True:
        par_impar = str(input('Par ou ímpar? [P/I] ')).upper().strip()
        if (par_impar in 'PIÍ'):
            break
    computador = randint(1,2)
    total = jogador + computador
    print('Você escolheu {} e o computador escolheu {}. Totalizando em {}'.format(jogador, computador, total))
    if (par_impar == 'P') and (total % 2 == 0):
        print('Você venceu!')
        vitorias += 1
    elif (par_impar == 'IÍ') and (total % 2 == 1):
        print('Você venceu!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break
    print('Vamos jogar de novo...')
print('Fim de jogo. Você venceu {}x'.format(vitorias))
# referente à aula 15

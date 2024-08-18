import random as rd
from time import sleep
print('Será que você consegue o Computador?')
pergunta = int(input("""Digite com o que você vai atacar:\n
[1] Pedra
[2] Papel
[3] Tesoura
Opção escolhida: """))

pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'
sorteio = [pedra, papel, tesoura]
computador = rd.choice(sorteio)

escolha = 0
if (pergunta == 1):
    escolha = pedra
elif (pergunta == 2):
    escolha = papel
elif (pergunta == 3):
    escolha = tesoura
else:
    print('Você escolheu errado. Tente Novamente')

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('OU')
sleep(1)
print('TESOURA!!!')
sleep(2)

print('-=' * 12)
print('Jogador jogou {}'.format(escolha))
sleep(4)
print('Computador jogou: {}'.format(computador))
print('-=' * 12)

if (escolha == pedra):
    if (computador == pedra):
        print('Houve um empate!')
    elif (computador == tesoura):
        print('O Jogador ganhou!')
    else:
        print('O Computador ganhou!')
elif(escolha == tesoura):
    if (computador == tesoura):
        print('Houve um empate!')
    elif (computador == papel):
        print('O Jogador ganhou!')
    else:
        print('O Computador ganhou!')
elif(escolha == papel):
    if (computador == papel):
        print('Houve um empate!')
    elif (computador == pedra):
        print('O Jogador ganhou!')
    else:
        print('O Computador ganhou!')
# referente à aula 12

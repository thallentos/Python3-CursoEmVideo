from random import randint
from time import sleep
lista = [] # ou lista = list()
jogos = list() #lista auxiliar
total_jogos = 1
print('-'*25)
print('    JOGO NA MEGA SENA    ')
print('-'*25)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie: '))

while (total_jogos <= quantidade_jogos):
    cont = 0
    while True:
        num = randint(1, 60)
        if (num not in lista):
            lista.append(num)
            cont += 1
        if (cont >= 6):
            break
    lista.sort()
    jogos.append(lista[:]) #criei uma copia da lista
    lista.clear() # limpa a lista para refazer o loop com a lista limpa
    total_jogos += 1

print('-'*6, f' Sorteando {quantidade_jogos} Jogos ', '-'*7)
for i, l in enumerate(jogos): # i == indice, l == cada lista
    print('Jogo {}: {}'.format(i+1, l))
    sleep(1)

print('\nBoa sorte!!')
# referente à aula 18

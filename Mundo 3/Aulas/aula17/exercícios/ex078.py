listanum = []
maior = 0
menor = 0

for t in range (0, 5):
    listanum.append(int(input('Digite um valor para a posição {}: '.format(t))))
    if (t == 0):
        maior = menor = listanum[t]
    else:
        if (listanum[t] > maior):
            maior = listanum[t]
        if (listanum[t] < menor):
            menor = listanum[t]

print('\nVocê digitou os valores {}'.format(listanum))
print('O maior valor digitado foi {} nas posições '.format(maior), end='')
for indice, valor in enumerate(listanum):
    if (valor == maior):
        print('{}...'.format(indice), end='')
print('\nO menor valor digitado foi {} nas posições '.format(menor), end='')
for indice, valor in enumerate(listanum):
    if (valor == menor):
        print('{}...'.format(indice), end='')
# referente à aula 17
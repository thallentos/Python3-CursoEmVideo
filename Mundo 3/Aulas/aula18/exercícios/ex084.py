temporaria = []
principal = []
maior_peso = menor_peso = 0
while True:
    temporaria.append(str(input('\nNome: ')))
    temporaria.append(float(input('Peso: ')))
    if (len(principal) == 0):
        menor_peso = maior_peso = temporaria[1] # temporaria[1] é o peso
    else:
        if (temporaria[1] > maior_peso):
            maior_peso = temporaria[1]
        elif (temporaria[1] < menor_peso):
            menor_peso = temporaria[1]
    principal.append(temporaria[:]) # copia os 2 primeiros
    temporaria.clear() # exclui o que estava antes do append principal

    continuar = str(input('Deseja continuar? [S/N] '))
    if (continuar in 'Nn'):
        break

print('\nVocê cadastrou {} pessoas!'.format(len(principal)))
print('O maior peso foi de {}Kg. Peso de '.format(maior_peso),end='')
for t in principal:
    if (t[1] == maior_peso):
        print(' [{}]'.format(t[0]),end='')
print('\nO menor peso foi de {}Kg. Peso de '.format(menor_peso), end='')
for t in principal:
    if (t[1] == menor_peso):
        print(' [{}]'.format(t[0]),end='')
# referente à aula 18
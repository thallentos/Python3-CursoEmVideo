matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma_pares = soma_coluna3 = maior = 0


for l in range (0, 3): # l == linha
    for c in range (0, 3): # c == coluna
        matriz[l][c] = int(input('Digite um número para [{}, {}]: '.format(l, c)))

for l in range (0, 3): # l == linha
    for c in range (0, 3): # c == coluna
        print('[{:^5}]'.format(matriz[l][c]),end='')
        if (matriz[l][c] % 2 == 0):
            soma_pares += matriz[l][c]
    print()

print('\nA soma dos valores pares é {}'.format(soma_pares))
for l in range (0, 3):
    soma_coluna3 += matriz[l][2]
print('A soma dos valores da terceira coluna é {}'.format(soma_coluna3))
for c in range (0, 3):
    if (c == 0):
        maior = matriz[1][c]
    elif (matriz[1][c] > maior):
        maior = matriz[1][c]
print('O maior valor na segunda linha é {}'.format(maior))
# referente à aula 18

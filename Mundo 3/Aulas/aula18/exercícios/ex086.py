matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for l in range (0, 3): # l == linha
    for c in range (0, 3): # c == coluna
        matriz[l][c] = int(input('Digite um número para [{}, {}]: '.format(l, c)))

for l in range (0, 3): # l == linha
    for c in range (0, 3): # c == coluna
        print('[{:^5}]'.format(matriz[l][c]),end='')
    print()
# referente à aula 18

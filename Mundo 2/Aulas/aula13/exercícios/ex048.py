soma = 0
contador = 0
for t in range(1, 500+1, 2):
    if (t % 3 == 0):
        contador += 1 # acumulador
        soma += t # contador
soma_total = soma
print('A soma de todos os {} números ímpares e múltiplos de 3 é {}'.format(contador, soma_total), end=' ')
# referente à aula 13

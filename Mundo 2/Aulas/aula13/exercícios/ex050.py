soma = 0
contador = 0
for t in range(1, 6+1):
    num = int(input('Digite o {}º número: '.format(t)))
    if (num % 2 == 0 and num != 0):
        soma += num
        contador += 1
print('A soma de todos os {} números pares é igual a {}'.format(contador, soma))
# referente à aula 13

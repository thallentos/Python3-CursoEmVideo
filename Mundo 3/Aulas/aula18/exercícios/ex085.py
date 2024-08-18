lista_numeros = [[], []]
# um [] para pares
# e outro para impares
pergunta_numero = 0
for t in range (1, 7+1):
    pergunta_numero = (int(input('Digite o {}o valor: '.format(t))))
    if (pergunta_numero % 2 == 0):
        lista_numeros[0].append(pergunta_numero)
    else:
        lista_numeros[1].append(pergunta_numero)

lista_numeros[0].sort()
lista_numeros[1].sort()
print('\nNúmeros pares: {}'.format(lista_numeros[0]))
print('Números ímpares: {}'.format(lista_numeros[1]))
# referente à aula 18

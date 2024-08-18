lista_total = [] # ou lista_total = list()
lista_pares = []
lista_impares = []

while True:
    pergunta_numeros = int(input('Digite um valor: '))
    lista_total.append(pergunta_numeros)
    if (pergunta_numeros % 2 == 0):
        lista_pares.append(pergunta_numeros)
    else:
        lista_impares.append(pergunta_numeros)

    continuar = str(input('Quer continuar? [S/N] '))
    if (continuar in 'Nn'):

        break
print('\nA lista completa é {}'.format(sorted(lista_total)))
print('A lista de pares é {}'.format(sorted(lista_pares)))
print('A lista de ímpares é {}'.format(sorted(lista_impares)))
# referente à aula 17

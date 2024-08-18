numeros_lista = list()

while True:
    numeros_da_pergunta = int(input('\nDigite um número: '))
    if (numeros_da_pergunta not in numeros_lista):
        numeros_lista.append(numeros_da_pergunta)
        print('Valor adicionado')
    else:
        print('Valor duplicado! Não vou adicionar na lista')

    repetir = str(input('Quer continuar? [S/N] '))
    if (repetir in 'Nn'):
        break
    else:
        pass

numeros_lista.sort()
print('\nLista dos números: {}'.format(sorted(numeros_lista)))
# referente à aula 17
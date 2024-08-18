lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    repetir = str(input('Quer continuar? [S/N] '))
    if (repetir in 'Nn'):
        break

lista.sort(reverse = True) # deixar a lista inversa
print('\nVocê digitou {} elementos'.format(len(lista)))
print('Os valores digitados em ordem decrescente foram: {}'.format(lista))
if (5 in lista):
    print('O valor 5 está na lista!')
else:
    print('O valor 5 NÃO está na lista!')
# referente à aula 17

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)

print('-'*39)
print(f'{"Lista de Preços":^39}')
print('-'*39)

for posição in range (0, len(listagem)):
    if (posição % 2 == 0):
        print('{:.<30}'.format(listagem[posição]),end='')
    else:
        print('R${:>7.2f}'.format(listagem[posição]))
print('-'*39)
# referente à aula 16

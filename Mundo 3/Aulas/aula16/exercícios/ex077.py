palavras = ('arroz', 'branco', 'claro', 'dark',
            'escuro', 'feio', 'grito', 'house',
            'inspirar', 'jail', 'kratos', 'luminus')

for p in palavras:
    print('\nNa palavra {} temos '.format(p), end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
# referente à aula 16

frase = str(input('Digite uma frase: ')).strip().lower() # lower = bota tudo em minsuculo | strip = tira os espaços

frase_reversa = frase[::-1]

print('\nFrase Digitada: {}\nFrase Reversa: {}'.format(frase, frase_reversa))
if (frase == frase_reversa):
    print('\nA frase é um palíndromo')
else:
    print('\nIsso não é um palíndromo')
# fiz do meu jeito que é diferente do jeito do vídeo do Guanabara
# referente à aula 13

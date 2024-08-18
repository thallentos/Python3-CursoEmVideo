def escreva(text):
    text = f' {text} '
    tamanho = len(text)
    print('~'* tamanho)
    print(f'{text}')
    print('~' * tamanho)

texto = str(input('Digite algo: '))
escreva(texto)
# referente à aula 20
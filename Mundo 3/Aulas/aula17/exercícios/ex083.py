expressão = str(input('Digite sua expressão matemática: '))
pilha = []

for simbolo in expressão:
    if (simbolo == '('):
        pilha.append('(')
    elif (simbolo == ')'):
        if (len(pilha) > 0):
            pilha.pop()
            # exclui o último elemento
            # caso esteja com (
        else:
            pilha.append(')')

if (len(pilha) == 0):
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')
# referente à aula 17


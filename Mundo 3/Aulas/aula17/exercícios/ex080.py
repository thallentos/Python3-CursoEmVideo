lista = []

for t in range (1, 5+1):
    número_da_pergunta = int(input('Digite um valor: '))

    if (t == 1) or (número_da_pergunta > lista[-1]):
    # o 1º valor sempre vai p última posição e se o valor
    # colocado for menor que o último valor tmb vai ser adicionado
    # no final
        lista.append(número_da_pergunta)
        print('Adicionado ao final da lista')
    else:
        posição = 0 # onde colocaremos o número
        while (posição < len(lista)):
            # se o valor da posição for menor
            # que a quantidade de valores da
            # lista, então o loop vai continuar,
            # mas no final do loop a posição vai aumentando
            # de 1 em 1
            if (número_da_pergunta <= lista[posição]):
                lista.insert(posição, número_da_pergunta)
                print('Adicionado na posição {} da lista'.format(posição))
                break
            posição += 1

print('Os valores digitados em ordem foram: {}'.format(lista))
# referente à aula 17

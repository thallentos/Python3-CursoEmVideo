while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if (num < 0):
        break
    else:
        print('-'*34)
        for t in range(1, 10+1):
            print('{} x {} = {}'.format(num, t, num * t))
        print(('-'*34))
print('Perdão, só aceitamos tabuada de um número positivo. Programa finalizado')
# referente à aula 15

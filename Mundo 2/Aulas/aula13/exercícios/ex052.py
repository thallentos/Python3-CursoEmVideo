num = int(input('Digite um número: '))

cont = 0
for t in range(1, num+1):
    if (num % t == 0):
        print('\033[0:34m', end='') # se o num for divisivel por t, então vai aparecer que ele foi dividido
        cont += 1
    else:
        print('\033[0:31m', end='') # se o num for divisivel por t, então vai aparecer que ele NÃO foi dividido
    print('{} '.format(t),end='')
if (cont == 2):
    print('\n\033[mO número {} foi dividido {}x e, por isso, é um número primo'.format(num, cont))
else:
    print('\n\033[mO número {} foi dividido {}x e, por isso, não é um número primo'.format(num, cont))
# referente à aula 13

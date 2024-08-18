num = int(input('Digite um número: '))
cont = num
fatorial = 1

print('Calculando {}! = '.format(num), end='')
for t in range (cont, 0, -1):
    fatorial *= cont
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
'''
while cont > 0:
    fatorial *= cont # o fatorial é igual a 1 e o Cont vai diminuindo por 1 até valer 1.
    cont -= 1
'''
print('{}'.format(fatorial))
# referente à aula 14

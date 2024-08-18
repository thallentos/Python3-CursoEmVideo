soma = num = cont = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if (num == 999):
        break
    else:
        soma += num
        cont += 1

print('Números lidos: {}'.format(cont))
print('Soma dos números: {}'.format(soma))
# referente à aula 15

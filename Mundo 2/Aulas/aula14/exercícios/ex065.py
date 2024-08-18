soma = num = cont = maior = menor = 0
terminar = ''
while (terminar in 'Ss'):
    num = int(input('Digite um número: '))
    soma += num
    cont += 1

    if (cont == 1):
        menor = maior = num
    else:
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num

    terminar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

print('\nVocê digitou {} número(s)'.format(cont))
print('Média entre eles: {:.2f}'.format(soma/cont))
print('Maior número lido: {}'.format(maior))
print('Menor número lido: {}'.format(menor))
# referente à aula 14

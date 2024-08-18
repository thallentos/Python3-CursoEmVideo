print('--- Leitor de Números ----')
cont = 0
soma = 0
num = 0
while (num != 999):
    num = int(input('Digite um número: [999 para parar] '))
    if (num != 999):
        soma += num
        cont += 1
print('\nQuantidade de número(s) digitado(s): {}'.format(cont))
print('Soma do(s) número(s) digitado(s): {}'.format(soma))
# referente à aula 14

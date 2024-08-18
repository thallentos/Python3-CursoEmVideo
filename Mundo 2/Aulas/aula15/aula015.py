# aprendi a usar o break
num = soma = 0
while True:
    num = int(input('Digite um número: '))
    if (num == 999):
        break
    else:
        soma += num
print('Soma: {}'.format(soma))
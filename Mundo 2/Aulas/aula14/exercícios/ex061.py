# progressão aritmética
print('='*28)
print(' PA DOS 10 PRIMEIROS TERMOS ')
print('='*28)
primeiro = int(input('1º Termo: '))
razao = int(input('Razão: '))

'''
for c in range (primeiro, décimo + razao, razao):
    print(c, end=' -> ')
'''
cont = 1
termo = primeiro
while (cont <= 10):
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1

print('Fim :))')

# referente à aula 14

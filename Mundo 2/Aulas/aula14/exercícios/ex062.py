# progressão aritmética
print('='*28)
print(' PA DOS 10 PRIMEIROS TERMOS ')
print('='*28)
primeiro = int(input('1º Termo: '))
razao = int(input('Razão: '))

cont = 0
termo = primeiro
total = 0
while (cont < 10):
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
    total += 1
print('PAUSA')

termos_final = 1
while (termos_final != 0):
    termos_final = int(input('\nMais quantos termos você quer ver? '))
    cont = 0
    while (cont < termos_final):
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
        total += 1
    print('PAUSA')
print('Finalizando com {} termos'.format(total))
# referente à aula 14

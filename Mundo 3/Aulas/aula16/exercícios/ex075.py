núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais outro número: ')),
       int(input('Digite o último número: ')))

print('\nVocê digitou os valores {}'.format(núm))
print('\nQuantas vezes apareceu o número 9? {}x'.format(núm.count(9)))

if (3 in núm):
    print('Em que posição foi digitado o primeiro número 3? {}ª posição'.format(núm.index(3, 0)+1))
else:
    print('O valor 3 não foi digitado')

print('Valores pares digitados: ',end='')
for n in núm:
    if (n % 2 == 0):
        print(n,end=' ')
# referente à aula 16

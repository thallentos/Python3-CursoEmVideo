num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
'''
if (num1 > num2) and (num1 > num3):
    print('{} é o maior dentre os 3 números'.format(num1))
elif (num2 > num1) and (num2 > num3):
    print('{} é o maior dentre os 3 números'.format(num2))
elif (num3 > num1) and (num3 > num2):
    print('{} é o maior dentre os 3 números'.format(num3))

if (num1 < num2) and (num1 < num3):
    print('{} é o menor dentre os 3 números'.format(num1))
elif (num2 < num1) and (num2 < num3):
    print('{} é o menor dentre os 3 números'.format(num2))
elif (num3 < num1) and (num3 < num2):
    print('{} é o menor dentre os 3 números'.format(num3))
'''
menor = num1
if (num2 < num1) and (num2 < num3):
    menor = num2
if (num3 < num1) and (num3 < num2):
    menor = num3

maior = num1
if (num2 > num1) and (num2 > num3):
    maior = num2
if (num3 > num1) and (num3 > num2):
    maior = num3

print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
# referente à aula 10

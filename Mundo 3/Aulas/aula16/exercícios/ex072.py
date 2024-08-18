while True:
    numero_posição = int(input('Digite um número inteiro entre 0 e 20: '))
    if (numero_posição >= 0) and (numero_posição <= 20):
        break
    else:
        print('Tente novamente. ', end='')

numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

print('\n=== Números Por Extenso ===')
print('Você digitou o número {}'.format(numeros_extenso[numero_posição]))
'''
print('Você digitou o número ',end='')
if (numero_posição == 0):
    print(numeros_extenso[0])
elif (numero_posição == 1):
    print(numeros_extenso[1])
elif (numero_posição == 2):
    print(numeros_extenso[2])
elif (numero_posição == 3):
    print(numeros_extenso[3])
elif (numero_posição == 4):
    print(numeros_extenso[4])
elif (numero_posição == 5):
    print(numeros_extenso[5])
elif (numero_posição == 6):
    print(numeros_extenso[6])
elif (numero_posição == 7):
    print(numeros_extenso[7])
elif (numero_posição == 8):
    print(numeros_extenso[8])
elif (numero_posição == 9):
    print(numeros_extenso[9])
elif (numero_posição == 10):
    print(numeros_extenso[10])
elif (numero_posição == 11):
    print(numeros_extenso[11])
elif (numero_posição == 12):
    print(numeros_extenso[12])
elif (numero_posição == 13):
    print(numeros_extenso[13])
elif (numero_posição == 14):
    print(numeros_extenso[14])
elif (numero_posição == 15):
    print(numeros_extenso[15])
elif (numero_posição == 16):
    print(numeros_extenso[16])
elif (numero_posição == 17):
    print(numeros_extenso[17])
elif (numero_posição == 18):
    print(numeros_extenso[18])
elif (numero_posição == 19):
    print(numeros_extenso[19])
elif (numero_posição == 20):
    print(numeros_extenso[20])
'''
# referente à aula 16

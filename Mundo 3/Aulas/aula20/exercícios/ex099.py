from time import sleep
def maior(* números):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in números:
        print('{} '.format(valor), end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('\nForam informados {} valores ao todo'.format(cont))
    print('O maior valor informado foi {}'.format(maior))
    # outro jeito de se fazer abaixo:
    # print('O maior valor é {}'.format(max(números)))

maior(1, 2, 3, 4, 5, 6, 7, 8, 100, 90)
# referente à aula 20
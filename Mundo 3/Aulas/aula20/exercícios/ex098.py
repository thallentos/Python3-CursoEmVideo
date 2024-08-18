from time import sleep

def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    sleep(1.5)
    print('-='*20)
    print('Contagem de {} até {} de {} em {}'.format(início, fim, passo, passo))
    sleep(2.5)

    if início < fim:
        cont = início
        while cont <= fim:
            print('{} '.format(cont), end='', flush=True)
            sleep(0.5)
            cont += passo
        sleep(0.5)
        print('Fim!')
    else:
        cont = início
        while cont >= fim:
            print('{} '.format(cont), end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-='*20)
print('Agora é a sua vez!!!')
ini = int(input('Início: '))
fii = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fii, pas)
# referente à aula 20
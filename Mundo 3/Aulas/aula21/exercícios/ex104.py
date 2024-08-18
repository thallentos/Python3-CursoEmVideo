def leiaint(n):
    print('-' * 30)
    while True:
        número = str(input(n))
        if número.isnumeric():
            print(f'Você acabou de digitar o número {número}')
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
    return número


n = leiaint('Digite um número: ')
# referente à aula 21
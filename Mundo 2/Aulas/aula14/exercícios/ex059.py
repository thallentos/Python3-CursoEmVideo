menu = 0
while (menu != 5):
    num1 = int(input('\nDigite o 1º número: '))
    num2 = int(input('Digite o 2º número: '))
    menu = int(input("""O que você deseja fazer com esses números?
    [1] Somar 
    [2] Multiplicar 
    [3] Descobrir qual é maior
    [4] Escolher novos números
    [5] Sair do Programa
    >>>>> Sua escolha: """))
    if (menu == 1):
        print('\nA soma entre {} e {} é igual a {}'.format(num1, num2, num1 + num2))
    elif (menu == 2):
        print('\nA multiplicação entre {} e {} é igual a {}'.format(num1, num2, num1 * num2))
    elif (menu == 3):
        if (num1 > num2):
            print('\nO 1º número ({}) é o maior'.format(num1))
        elif (num2 > num1):
            print('\nO 2º número ({}) é o maior'.format(num2))
        else:
            print('\nOs dois números são iguais. Cê acha que eu sou besta é?')
    #elif (menu == 4):
    # não precisa de nada, porque vai voltar automaticamente
    elif (menu == 5):
       break

# referente à aula 14

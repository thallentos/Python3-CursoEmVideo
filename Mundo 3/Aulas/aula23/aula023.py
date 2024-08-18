while True:
    # >>> Loop while True:
    # Ajuda a repetir o processo
    try:
        # >>> Try:
        # Serve para colocar a operação (conta)
        a = int(input('\nNumerador: '))
        b = int(input('Denominador: '))
        r = a/b
    except Exception as erro:
        # Esse tipo de Except serve para ver
        # o tipo de erro encontrado
        print(f'O erro encontrado foi {erro.__class__}')
    except:
        # >>> Except:
        # Serve para colocar uma mensagem de que
        # algo deu erro (talvez o porquê também)
        print('Infelizmente tivemos um problema =(')
    else:
        # >>> Else:
        # Serve para colocar o resultado do Try
        # caso tenha dado certo
        print(f'O resultado é {r:.2f}')
        break
    finally:
        # >>> Finally:
        # Vai ocorrer independente se o resultado
        # for aceito ou não!
        print('Obrigado pelo tempo!')
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return print('Não vota')
    elif (16 <= idade < 18) or (idade > 65):
        return print('Voto opcional')
    elif (18 <= idade < 65):
        return print('Voto obrigatório')

print('-'*28)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
# referente à aula 21
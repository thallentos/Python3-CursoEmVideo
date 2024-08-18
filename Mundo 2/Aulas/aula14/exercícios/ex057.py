sexo = ''
while (sexo != 'Pp'):
    sexo = str(input('Digite seu sexo [M/F] ou [P] caso queira parar:  ')).upper().strip()[0]
    if (sexo in 'Mm'):
        print('Tu é macho, rapaz!')
    elif (sexo in 'Ff'):
        print('Você é uma princesa!')
    elif (sexo in 'Pp'):
        break
    else:
        print('Opção incorreta, digite novamente: ')

# referente à aula 14

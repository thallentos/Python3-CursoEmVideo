continuar = ''
cont_homens = 0
cont_mulheres = 0
cont_pessoas = 0
sexo = ''
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos

while True:
    print('='*25)
    print('   CADASTRE UMA PESSOA')
    print('='*25)
    idade = int(input('Idade: '))

    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if (sexo in 'MF'):
            break

    if (sexo == 'M'):
        cont_homens += 1
    elif (sexo == 'F') and (idade < 20):
        cont_mulheres += 1
    if (idade > 18):
        cont_pessoas += 1

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
        if (continuar in 'SN'):
            break
    if (continuar == 'N'):
         break

print('\nNúmero de pessoas que tem mais de 18 anos: {} pessoas'.format(cont_pessoas))
print('Número de homens cadastrados: {} homens'.format(cont_homens))
print('Números de mulheres que tem menos de 20 anos: {} mulheres'.format(cont_mulheres))

# referente à aula 15

soma_idades = 0
idade_velho = 0
nome_velho = ''
mulheres_abaixo_20 = 0
femeas = 0
num_pessoas = 0

for i in range(1, 2+1):
    print('----- {}ª Pessoa -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    soma_idades += idade
    num_pessoas += 1
    if ((i == 1) and (sexo in 'Mm')):
        idade_velho = idade
        nome_velho = nome
    if ((sexo in 'Mm') and (idade > idade_velho)):
        idade_velho = idade
        nome_velho = nome
    if (sexo in 'Ff'):
        femeas += 1
        if ((sexo in 'Ff') and (idade < 20)):
            mulheres_abaixo_20 += 1

media_idades = soma_idades/num_pessoas
print('A média de idade do grupo é {:.2f} anos'.format(media_idades))
print('O homem mais velho se chama {} e tem {} anos'.format(nome_velho, idade_velho))
print('O grupo tem {} mulher(es) e {} tem abaixo de 20 anos'.format(femeas, mulheres_abaixo_20))
# referente à aula 13

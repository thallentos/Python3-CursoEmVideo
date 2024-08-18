ficha = []

while True:
    nome = str(input('\nNome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    ficha.append([nome, [nota1, nota2], media]) # nome == 0, nota1 e nota2 == 1, media == 2 linha 18
    pergunta = str(input('Deseja continuar? [S/N] '))[0]
    if (pergunta in 'Nn'):
        break

print('\n', end='')
print('-'*26)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}') # a[0] é o nome, a[2] média
while True:
    print('-'*35)
    opção = int(input('Você deseja ver as notas de qual aluno? (999 interrompe): '))
    if (opção == 999):
        print('Programa finalizado com sucesso')
        break
    if (opção <= len(ficha) - 1):
        print('As notas de {} são {}'.format(ficha[opção][0], ficha[opção][1]))
        # ficha[opção][0] é o nome, ficha[opção][1] são as notas
# referente à aula 18

import random as rd
alun1 = str(input('Primeiro aluno: '))
alun2 = str(input('Segundo aluno: '))
alun3 = str(input('Terceiro aluno: '))
alun4 = str(input('Quarto aluno: '))

sorteio = [alun1, alun2, alun3, alun4]

rd.shuffle(sorteio)# embaralhei os nomes dos participantes

print('Essa é a ordem de apresentação dos trabalhos: \n{}'.format(sorteio))
# referente à aula 8

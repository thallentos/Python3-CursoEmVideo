import random as rd
alun1 = str(input('Primeiro aluno: '))
alun2 = str(input('Segundo aluno: '))
alun3 = str(input('Terceiro aluno: '))
alun4 = str(input('Quarto aluno: '))

sorteio = [alun1, alun2, alun3, alun4] # criei uma lista para agrupar os 4 alunos
apagar_quadro = rd.choice(sorteio)

print('O(a) aluno(a) sorteado(a) para apagar o quadro foi {}'.format(apagar_quadro))
# referente à aula 8

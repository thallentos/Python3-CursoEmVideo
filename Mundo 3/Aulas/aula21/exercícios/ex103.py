def ficha(n, g):
    if len(n) == 0:
        n = '<deconhecido>'
    if len(g) == 0 or not g.isnumeric():
        g = '0'
    print(f'O jogador {n} fez {g} gol(s) no campeonato')

print('-'*30)
nome = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
ficha(nome, gol)
# referente à aula 21
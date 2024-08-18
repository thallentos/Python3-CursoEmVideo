nome = input('Digite seu nome: ')
print('É um prazer te conhecer,', nome)
print(f'É um prazer te conhecer, {nome}') # só funciona se o print for formatado "f"
print('É um prazer te conhecer, ' + nome) # só funciona se for string para string
print('É um prazer te conhecer, {}'.format(nome))
# exercício referente à aula 6
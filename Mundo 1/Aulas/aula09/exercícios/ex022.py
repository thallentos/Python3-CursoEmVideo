nome = str(input('Digite seu nome: ')).strip() # retirou os espaços do início e do final

print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras (sem contar os espaços): {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(nome.find(' ')))
'''Quando o programa achar o espaço, significa que é o final do primeiro nome'''''
separa = nome.split()
# print('Quantidade de letras do seu primeiro nome: {}'.format(len(separa[0]))) outra forma de se fazer isso
# referente à aula 9

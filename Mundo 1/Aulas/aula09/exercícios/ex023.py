num = int(input('Digite um número (0 a 9999): '))

m = (num // 1000) % 10 # milhar
c = (num // 100) % 10 # centena
d = (num // 10) % 10 # dezena
u = (num // 1) % 10 # unidade
print('Analisando o número {}: \nUnidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(num, u, d, c, m))
# referente à aula 9

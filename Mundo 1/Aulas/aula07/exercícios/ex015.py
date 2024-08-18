kms = float(input('Digite a quantidade de Km rodados: '))
dias = int(input('Por quantos dias o carro foi alugado? '))

valor_final = (kms * 0.15) + (dias * 60)

print('O valor total a pagar por {:.2f}km rodados e {} dia(s) equivale a R${:.2f}'.format(kms, dias, valor_final))
# exercício referente à aula 7

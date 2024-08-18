valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos o comprador pagará pela casa? '))

prestacao_mensal = valor / (12 * anos)
minimo = 0.3 * salario

if (prestacao_mensal <= minimo):
    print('Parabéns, sua análise foi aprovada!')
else:
    print('Que pena... sua análise foi negada :(')

print('Para pagar uma casa de R${:.2f} em {} ano(s) a prestação mensal é de R${:.2f} !'.format(valor, anos, prestacao_mensal))
# referente à aula 12

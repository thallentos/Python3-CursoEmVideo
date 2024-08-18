salario = float(input('Digite seu salário: R$'))

aumento2 = salario * 1.10 #salário maior que R$1250
aumento1 = salario * 1.15 #salário menor ou igual que R$1250

if (salario <= 1250):
    print('Parabéns, após o aumento, seu salario de R${:.2f} agora é de R${:.2f}'.format(salario, aumento1))
else:
    print('Parabéns, após o aumento, seu salario de R${:.2f} agora é de R${:.2f}'.format(salario, aumento2))
# referente à aula 10

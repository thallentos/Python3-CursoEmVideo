print('='*25)
print('   Banco do Thallentos')
print('='*25)

dindin = int(input('Qual será o valor a ser sacado? R$'))
total = dindin
céd = 100
total_céd = 0
while True:
    if (total >= céd):
        total -= céd
        total_céd += 1
    else:
        if (total_céd > 0):
            print('Total de cédulas {} de R${:.2f}'.format(total_céd, céd))
        if (céd == 100):
            céd = 50
        elif (céd == 50):
            céd = 20
        elif (céd == 20):
            céd = 10
        elif (céd == 10):
            céd = 1
        total_céd = 0
        if (total == 0):
            break
# referente à aula 15

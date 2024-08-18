velocidade = float(input('Digite a velocidade do seu carro: '))

multa = (velocidade - 80) * 7 #só levará multa se a velocidade estiver acima de 80km

if (velocidade > 80):
    print('Vish, você foi multado e terá que pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tá de boa, você está na velocidade permitida')
print('Tenha um bom dia, dirija com segurança!')
# referente à aula 10

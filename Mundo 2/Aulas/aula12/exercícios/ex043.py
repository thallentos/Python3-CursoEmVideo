peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura: (m) '))

imc = peso / (altura**2)

print('O seu IMC é de {:.1f}'.format(imc))
if (imc < 18.5):
    print('Você está no osso')
elif((imc >= 18.5) and (imc < 25)):
    print('Parabéns, você está no ponto de corte')
elif((imc >= 25) and (imc < 30)):
    print('Você está um pouquinho cheio')
elif ((imc >= 30) and (imc < 40)):
    print('Você está gordo demais')
else:
    print('Parabéns! Você está apto(a) para entrar no Quilos Mortais')
# referente à aula 12

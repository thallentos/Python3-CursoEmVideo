distancia = float(input('Digite a distância da viagem percorrida: '))

valor = 0

if (distancia <= 200):
    valor = distancia * 0.50  # menor que 200km
else:
    valor = distancia * 0.45  # maior que 200km

# outra forma de fazer --> valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('Você pagará R${:.2f} nessa viagem'.format(valor))
# referente à aula 10

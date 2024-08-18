import math as mt
angulo = float(input('Digite o valor de um ângulo qualquer: '))

seno = mt.sin(mt.radians(angulo))
cosseno = mt.cos(mt.radians(angulo))
tangente = mt.tan(mt.radians(angulo))

# eu precisei botar "mt.randians()", porque a biblioteca do Python lê como radianos

print('O ângulo {}° têm...: \nSeno: {:.2f}°\nCosseno: {:.2f}°\nTangente: {:.2f}°'.format(angulo, seno, cosseno, tangente))
# referente à aula 8

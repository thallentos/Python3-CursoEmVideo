import random

numeros_aleatorios = [random.randint(0, 10) for t in range(0,5)]

menor = min(numeros_aleatorios)
maior = max(numeros_aleatorios)
print('Números gerados: {}'.format(sorted(numeros_aleatorios)))
print('Menor número gerado: {}'.format(menor))
print('Maior número gerado: {}'.format(maior))
# referente à aula 16

# Receber inúmeros valores numa função
'''
def contador (* núm):
    # esse * é um desempacotamento dos valores passados
    tamanho = len(núm)
    print(f'Recebi os valores {núm} e são no total {tamanho} números')

contador(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
'''

# Trabalhando com listas em funções
def dobra (lista):
    posição = 0
    while posição < len(lista):
        lista[posição] *= 2
        posição += 1

ímpares = [1, 3, 5, 7, 9]
print(ímpares)
dobra(ímpares)
print(ímpares)

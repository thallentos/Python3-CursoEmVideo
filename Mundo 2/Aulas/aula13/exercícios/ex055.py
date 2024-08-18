menor_peso = 0
maior_peso = 0

for p in range(1, 5+1):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if (menor_peso == 0): # o menor peso recebe até o momento, que é zero (linha 2)
        menor_peso = maior_peso
    if (peso > maior_peso):
        maior_peso = peso
    if (peso < menor_peso): # agora o bagulho dá certo
         menor_peso = peso

print('Menor peso lido: {:.1f}Kg'.format(menor_peso))
print('Maior peso lido: {:.1f}Kg'.format(maior_peso))
# referente à aula 13
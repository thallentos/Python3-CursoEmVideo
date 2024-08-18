# Tuplas
# - São imutáveis

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
print('Lanche: {}'.format(lanche[0]))
print('Lanche: {}'.format(lanche[0:2]))
print('Lanche: {}'.format(lanche[0:2+1]))
print('Lanche: {}'.format(lanche[1:]))
print('Lanche: {}'.format(lanche[-1]))
print('Lanche: {}'.format(lanche[-1::-2]))
print('Quantidade de lanche: {}\n'.format(len(lanche)))

for comida in lanche:
    print('Comida: {}'.format(comida))

for cont in range(0, len(lanche)):
    print('Eu vou comer {}'.format(lanche[cont]))

for cont, comida in enumerate(lanche):
    print('Comida {}: {}'.format(cont+1, comida))

a = (1, 2, 3, 4)
b = (4, 5, 6, 7)
c = a + b
print(sorted(c))

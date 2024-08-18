import math as mt
cat_op = int(input('Digite o valor do cateto oposto: '))
cat_adj = int(input('Digite o valor do cateto adjacente: '))

hip = mt.hypot(cat_op, cat_adj) # tira a raíz quadrada da soma dos catetos ao quadrado
'''hip = mt.sqrt(cat_op**2 + cat_adj**2)'''
'''hip = ((cat_op**2) + (cat_adj**2))** 0.5'''
# 3 formas diferentes de se fazer a mesma coisa

print('O valor da hipotenusa é igual a {:.2f}'.format(hip))
# referente à aula 8

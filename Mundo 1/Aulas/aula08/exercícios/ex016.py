import math as mt
num = float(input('Digite um número decimal: '))

pt_int = mt.floor(num) # arredonda o número para a parte inteira dele
'''pt_int = mt.trunc(num)'''
'''pt_int = int(num)'''
# 3 formas diferentes de se fazer a mesma coisa

print('A parte inteira de {} é igual a {}'.format(num, pt_int))
# referente à aula 8

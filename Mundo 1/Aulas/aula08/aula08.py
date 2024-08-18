import math as mt # importa todas as funções da biblioteca math e a chama de mt
# from math import sqrt --> só importa a função "sqrt"

num = int(input('Digite um número: '))
raiz = mt.sqrt(num)

print('A raíz quadrada de {} é {:.2f}'.format(num, raiz))

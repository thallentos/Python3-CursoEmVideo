from uteis import numeros
# importei a biblioteca (pacote) em que coloquei
# as funções

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}.')
print(f'O triplo de {num} é {numeros.triplo(num)}.')
# referente à aula 22

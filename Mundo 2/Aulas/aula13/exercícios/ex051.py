# progressão aritmética
print('='*28)
print(' PA DOS 10 PRIMEIROS TERMOS ')
print('='*28)
primeiro = int(input('1º Termo: '))
razao = int(input('Razão: '))
décimo = primeiro + ((10 - 1) * razao) # calculo do 10º termo

for c in range (primeiro, décimo + razao, razao):
    print(c, end=' -> ')
print('Fim :))')
# referente à aula 13

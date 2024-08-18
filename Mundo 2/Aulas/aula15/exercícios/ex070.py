total = cont_prod_maior_1000 = mais_barato = cont = 0
nome_mais_barato = ''

print('='*25)
print('   Loja do Thallentos')
print('='*25)
while True:
    nome_produto = str(input('Nome do produto: '))
    preço = float(input('Qual o preço desse produto: R$'))
    total += preço
    cont += 1
    if (preço > 1000):
        cont_prod_maior_1000 += 1
    if (cont == 1) or (preço < mais_barato):
        mais_barato = preço
        nome_mais_barato = nome_produto
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if  (continuar in 'SN'):
            break
    if (continuar in 'Nn'):
        break
print('\n')
print('='*4,end='')
print(' FIM DO PROGRAMA ', end='')
print('='*4)
print('Total da compra: R${:.2f}'.format(total))
print('Temos {} produtos que custam mais de R$1000.00'.format(cont_prod_maior_1000))
print('O produto mais barato foi "{}" e custa R${:.2f}'.format(nome_mais_barato,mais_barato))
# referente à aula 15

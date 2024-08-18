print(f'{" LOJAS THALLENTOS ":=^40}')
valor_produto = float(input('Qual o valor das compras? R$'))
forma_pagamento = int(input("""Digite como será a forma de pagamento:
[1] À vista no dinheiro ou cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão
Opção escolhida: """))

vista_dindin_check = valor_produto * 0.90 #10% de desconto
vista_cartão = valor_produto * 0.95 # 5% de desconto
cartão_2x = valor_produto/2 # especificar que a pessoa pagará 2 parcelas desse valor

total = 0
if (forma_pagamento == 1):
    total = vista_dindin_check
elif (forma_pagamento == 2):
    total = vista_cartão
elif (forma_pagamento == 3):
    total = valor_produto
    print('\nVocê pagará 2 parcelas de R${:.2f} sem juros nas suas compras'.format(cartão_2x))
elif (forma_pagamento == 4):
    parcelas = int(input('\nEm quantas vezes você quer parcelar (3x ou mais)? '))
    total = valor_produto * 1.20
    total_parcelas = total / parcelas
    print('\nSua compra será parcelada em {}x de R${:.2f} com juros'.format(parcelas, total_parcelas))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor_produto, total))

# referente à aula 12

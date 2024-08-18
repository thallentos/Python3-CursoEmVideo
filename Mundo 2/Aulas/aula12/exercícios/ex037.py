num = int(input('Digite um número: '))
pergunta = int(input("""Escolha em que você quer converter esse número: 
[1] Binário
[2] Octal
[3] Hexadecimal
A minha escolha é ... """))

binario = bin(num)
octal = oct(num)
hexa = hex(num)

if (pergunta == 1):
    print('O número {} convertido em Binário é igual a {}'.format(num, binario [2:]))
elif (pergunta == 2):
    print('O número {} convertido em Octal é igual a {}'.format(num, octal [2:]))
elif (pergunta == 3):
    print('O número {} convertido em Hexadecimal é igual a {}'.format(num, hexa [2:]))
else:
    print('Opção inválida. Tente novamente')
# referente à aula 12

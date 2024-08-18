reta1 = int(input('Digite o valor da 1ª reta: '))
reta2 = int(input('Digite o valor da 2ª reta: '))
reta3 = int(input('Digite o valor da 3ª reta: '))

if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2):
    print('Parabéns, essas 3 retas podem formar um triângulo')
else:
    print('Que pena...essas 3 retas não podem formar um triângulo')
# referente à aula 10

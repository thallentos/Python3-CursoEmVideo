reta1 = int(input('Digite a 1ª reta para a formação do triângulo: '))
reta2 = int(input('Digite a 2ª reta para a formação do triângulo: '))
reta3 = int(input('Digite a 3ª reta para a formação do triângulo: '))

if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta1 + reta3 > reta2):
    print('As retas podem formar um triângulo', end='')
    if(reta1 == reta2 == reta3):
        print('...equilátero')
    elif ((reta1 == reta2) and ((reta1 != reta3) and (reta2 != reta3))) or ((reta1 == reta3) and ((reta1 != reta2) and (reta3 != reta2))) or ((reta2 == reta3) and ((reta2 != reta1) and (reta3 != reta1))):
        print('...isósceles')
    else:
        print('...escaleno')
else:
    print('Infelizmente...não é possível formar um triângulo com esses valores')
# referente à aula 12

nome = str(input('Digite seu nome: '))

if (nome == 'Thalles'):
    print('Esse é o nome mais bonito que eu já vi')
elif (nome == 'Tales'):
    print('Eu acho mais bonito se tivesse 2 L e 1 H')
elif (nome in 'Pedro João Thiago Paulo Ana Maria Luisa'):
    print('Seu nome é bem popular no Brasil')
elif (nome == 'Mirella'):
    print('Nossa, que legal. Esse é o nome da minha futura namorada')
elif (nome == 'Enzo') or (nome == 'Valentina'):
    print('Namoral, nome de gente nutella')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia')

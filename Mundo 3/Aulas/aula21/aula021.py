# Ajuda interativa (help)
# help(variável que se deseja saber)


# Docstring
def contador(i, f, p):
    # o que está abaixo é a docstring
    # que pode ser vista chamando help(contador)
    # a partir de agora
    """
    -> Função para contar valores
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Thalles Coelho Marques
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')

help(contador)


# Parâmetros opcionais
def somar(a=0, b=0, c=0):
    # Parâmetros opcionais é quando se passa
    # valores padrão caso o usuário não informe
    # o valor desejado. No caso, foi utilizado
    # o valor de zero como padrão para os 3 valores
    """
    -> Função para somar 3 valores e mostrar o resultado na tela
    :param a: primeiro valor a ser somado
    :param b: segundo valor a ser somado
    :param c: terceiro valor a ser somado
    :return: sem retorno
    Feito por Thalles Coelho Marques
    """
    s = a + b + c
    print('A soma vale {}'.format(s))

somar(3, 2, 5)
somar(3, 2)
somar(3)
# somar((3 + (4) + 1), (4 + 5), (2 + 3))
# que top, tmb dá para fazer isso!


# Escopo de variáveis

# Variável de Escopo Global:
# significa que a variável pode ser usada
# em todas as linhas de código

# Variável de Escopo Local:
# significa que a variável só pode ser usada
# onde ela foi criada

# Como colocar uma variável global dentro
# de uma função sem que ela se torne local?
# Resposta: é só usar a palavra "global"
# antes da variável, como eu vou mostrar
# no exemplo abaixo, ou seja, a variável
# dentro da função vai ser alterada

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
# o valor de 'a' vai ser alterado na função
teste(a)
print(f'A fora vale {a}')


# Retorno de Valores
# Retonar valores possibilita que eu possa
# salvar cada soma numa variável, em vez de ter
# que printar todos os valores
def soma_retornando(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma_retornando(1)
r2 = soma_retornando(1 + 2)
r3 = soma_retornando(1 + 2 + 3)
print(f'As minhas somas deram {r1}, {r2}, {r3}')
from time import sleep

cores = ('\033[m',        # 0 - sem cores
         '\033[0;30;41m', # 1 - vermelho
         '\033[0;30;42m', # 2 - verde
         '\033[0;30;43m', # 3 - amarelo
         '\033[0;30;44m', # 4 - azul
         '\033[0;30;45m', # 5 - roxo
         '\033[7;30m'     # 6 - branco
         )

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[5], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('-'* tam)
    print(f'  {msg}')
    print('-'* tam)
    print(cores[0], end='')
    sleep(1)

# Programa principal
comando = ''
while True:
    título('Sistema de Ajuda Thallentos', 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() in 'FIM':
        break
    else:
        ajuda(comando)

título('Até logo :))', 1)
# referente à aula 21
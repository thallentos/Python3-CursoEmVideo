from datetime import date
atual = date.today().year
data_nascimento = int(input('Digite o ano que você nasceu: '))

idade_atual = atual - data_nascimento

if (idade_atual < 18):
    tempo_restante = 18 - idade_atual
    print('Você tem {} ano(s) e faltam {} anos para você se alistar'.format(idade_atual, tempo_restante))
    alistar_futuro = atual + tempo_restante
    print('Seu alistamento será em {}'.format(alistar_futuro))
elif(idade_atual == 18):
    print("""Hehe, você tem {} anos e está na hora de você se alistar, rapaz.
Não tem como fugir""".format(idade_atual))
else:
    tempo_atrasado = idade_atual - 18
    print("""Vish...já passou o prazo do alistamento.
Você tem {} anos e está {} ano(s) atrasado""".format(idade_atual, tempo_atrasado))
    alistar_passado = atual - tempo_atrasado
    print('Você deveria ter se alistado em {}'.format(alistar_passado))
# referente à aula 12

from datetime import date
atual = date.today().year
data_nascimento = int(input('Digite o ano em que você nasceu: '))

idade_atual = atual - data_nascimento

if (idade_atual < 9):
    print('De acordo com a sua idade, você é considerado um atleta Mirim')
elif (idade_atual < 14):
    print('De acordo com a sua idade, você é considerado um atleta Infantil')
elif (idade_atual < 19):
    print('De acordo com a sua idade, você é considerado um atleta Júnior')
elif (idade_atual < 25):
    print('De acordo com a sua idade, você é considerado um atleta Sênior')
else:
    print('De acordo com a sua idade, você é considerado um atleta Master')
# referente à aula 12

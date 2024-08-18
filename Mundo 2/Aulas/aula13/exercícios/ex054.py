from datetime import date

maioridade = 0
menoridade = 0
hoje = date.today().year # ano em si
for i in range(1, 7+1):
    nascimento = int(input('Em que ano a {} ª pessoa nasceu: '.format(i)))
    idade = hoje - nascimento
    if (idade >= 18):
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoa(s) atingiram a maioridade!'.format(maioridade))
print('{} pessoa(s) ainda não atingiram a maioridade!'.format(menoridade))
# referente à aula 13

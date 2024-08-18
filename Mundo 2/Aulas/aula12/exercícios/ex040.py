nota1 = float(input('Digite a sua 1ª nota: '))
nota2 = float(input('Digite a sua 2ª nota: '))

media = (nota1 + nota2)/ 2

print("""\nInformações:
Média menor que 5: Reprovado
Média entre 5 e 6.9: Recuperação
Média maior ou igual a 7: Aprovado""")

if (media < 5):
    print("""\nSituação: Reprovado
A sua média foi {:.2f}""".format(media))
elif (media > 5) and (media < 7):
    print("""\nSituação: Recuperação
A sua média foi {:.2f}""".format(media))
else:
    print("""\nSituação: Aprovado
A sua média foi {:.2f}""".format(media))

# referente à aula 12

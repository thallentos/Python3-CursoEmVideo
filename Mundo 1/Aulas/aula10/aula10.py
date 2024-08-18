n1 = int(input('Digite a sua nota 1ª: '))
n2 = int(input('Digite a sua nota 2ª: '))

media = (n1 + n2) / 2

print('A sua média é {:.1f}'.format(media))
if (media >= 6):
    print('Parabéns, você passou!')
else:
    print('Você ficou de recuperação. Poxa...')

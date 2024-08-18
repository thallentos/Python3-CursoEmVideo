larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = alt * larg
tinta = area / 2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e a área dela é {:.2f}m².'.format(larg, alt, area))
print('A quantidade de tinta necessária para pintá-la é {:.2f}l'.format(tinta))
# exercício referente à aula 7

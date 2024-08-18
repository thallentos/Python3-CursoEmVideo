def área (largura, comprimento):
    retangulo = largura * comprimento
    print('A área de um terreno {:.1f}x{:.1f} é {:.2f}m²'.format(largura, comprimento, retangulo))
    # return retangulo

print('-'*22)
print(' Controle de terrenos')
print('-'*22)
larg = float(input('Largura (m): '))
compr = float(input('Comprimento (m): '))
área(larg, compr)
# referente à aula 20
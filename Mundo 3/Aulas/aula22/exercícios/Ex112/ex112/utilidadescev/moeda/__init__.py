def aumentar(preço=0, taxa=0, formato=False):
    resultado = preço + (preço * (taxa/100))
    return resultado if formato is False else moeda(resultado)


def diminuir(preço=0, taxa=0, formato=False):
    resultado = preço - (preço * (taxa/100))
    return resultado if formato is False else moeda(resultado)


def dobro(preço=0, formato=False):
    resultado = preço * 2
    return resultado if not formato else moeda(resultado)


def metade(preço=0, formato=False):
    resultado = preço/2
    return resultado if not formato else moeda(resultado)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(preço=0, taxaA=10, taxaR=5):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(preço, taxaA, True)}')
    print(f'{taxaR}% de redução: \t{diminuir(preço, taxaR, True)}')
    print('-' * 30)
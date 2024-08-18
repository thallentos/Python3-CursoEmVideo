cidade = str(input('Digite o nome de uma cidade: ')).strip() # tirei os espaços indesejados
cidade_certa = (cidade[:5].upper() == 'SANTO')

print('A cidade começa com o nome SANTO? \n{}'.format(cidade_certa))
# referente à aula 9

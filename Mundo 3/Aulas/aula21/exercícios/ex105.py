'''
- quantidade de notas
- a maior nota
- a menor nota
- a média da turma
- a situação (opcional)
'''
def notas(*nota_individual, situação=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nota_individual: uma ou mais notas dos alunos (aceita várias)
    :param situação: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    nota_geral = \
        {
            'total': len(nota_individual),
            'maior': max(nota_individual),
            'menor': min(nota_individual),
            'média': sum(nota_individual)/len(nota_individual)
        }
    if situação:
        if (nota_geral['média'] >= 8.5):
            nota_geral['situação'] = 'Excelente'
        elif (nota_geral['média'] >= 7):
            nota_geral['situação'] = 'Boa'
        elif (nota_geral['média'] >= 5):
            nota_geral['situação'] = 'Razoável'
        elif (nota_geral['média'] >= 3):
            nota_geral['situação'] = 'Péssimo'
        else:
            nota_geral['situação'] = 'É melhor reprovar, por favor'
    return nota_geral


resp = notas(2, situação=True)
print(resp)
#help(notas)
# referente à aula 21
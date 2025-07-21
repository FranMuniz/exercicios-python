'''
Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes infos:
- Quantidade de notas
- A maior nota
- A menor nota
- A média das notas
- A situação (opcional)
Adicione também a docstring
'''

# Função
def notas(* nota, situacao=False):
    """
    -> Analisa notas e situação dos alunos.
    :param nota: uma ou mais notas dos alunos;
    :param situacao: valor opcional, indicando se de ou
        não adicionar a situação;
    :return: dicionário com informações sobre notas e
        situação.
    Função criada por Francieli Muniz
    """
    infos = {}
    infos['total'] = len(nota)
    infos['maior'] = max(nota)
    infos['menor'] = min(nota)
    infos['media'] = round(sum(nota)/len(nota), 2)

    if situacao:
        if infos['media'] >= 7:
            infos['situacao'] = 'BOA'
        elif infos['media'] >= 5:
            infos['situacao'] = 'RAZOÁVEL'
        else:
            infos['situacao'] = 'RUIM'
    return infos


# Programa Principal
valores = notas(5.6, 7.8, 9.8, situacao=True)
print(valores)
help(notas)
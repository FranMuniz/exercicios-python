'''
Faça um programa que tenha uma função chamada ficha(), que receba dois
parâmetros opcionais: O nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.
'''

# Função
def ficha(nome='<desconhecido>', gol=0):
    """
    -> Mostra ficha de jogador.
    :param nome: Nome do jogador (opcional), por default <desconhecido>;
    :param gol: Quantidade de gols (opcional), por default 0.
    Função criada por Francieli Muniz
    """
    print(f'Jogador(a) {nome} fez {gol} gol(s) no campeonato.')

# Programa Principal
nome_jogador = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome_jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome_jogador, gols)

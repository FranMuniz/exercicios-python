'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos gurante o 
campeonato.
'''

jogador = {}
partidas = []

jogador['nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, total):
    partidas.append(int(input(f'   Quantos gols na partida {i+1}: ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 20)
print(jogador)

print('-=' * 20)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')

print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''
Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema
de visualização de detalhes do aproveitamento de cada jogador.
'''

jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(0, total):
        partidas.append(int(input(f'   Quantos gols na partida {i+1}: ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('Erro! Por favor digite apenas S ou N.')
    if opcao == 'N':
        break
print('-=' * 20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-=' * 20)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No {i+1}º jogo fez {g} gols.')
    print('-=' * 20)
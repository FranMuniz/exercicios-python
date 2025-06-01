'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileira de Futebol (2025), na ordem de colocação. Depois mostre:
a) Os 5 primeiros;
b) Os últimos 4 colocados;
c) Times em ordem alfabética;
d) Em que posição está o time Palmeiras.
'''

times_brasileirao = (
    'Bragantino', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Bahia',
    'Fluminense', 'Mirassol', 'Ceará', 'Corinthians', 'Atlético-MG',
    'Botafogo', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco',
    'Fortaleza', 'Vitória', 'Santos', 'Juventude', 'Sport'
)

print(f'Lista de times do Brasileirão 2025: {times_brasileirao}')

print('-=-' * 30)
print(f'Os 5 primeiros colocados são: {times_brasileirao[0:5]}')

print('-=-' * 30)
print(f'Os 4 últimos colocados são: {times_brasileirao[-4:]}')

print('-=-' * 30)
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')

print('-=-' * 30)
print(f'O Palmeiras está na {times_brasileirao.index('Palmeiras')+1}ª posição.')
print('-=-' * 30)





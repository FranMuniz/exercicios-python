'''
Melhore o DESAFIO 61, perguntando para o usuário
se ele quer mostrar mais alguns termos. O protgrama
encerra quando ele disser que quer mostrar 0 termos.

DESAFIO 61: Refaça o DESAFIO 51, lendo o primeiro termo
e a razão de uma PA. Mostrando os 10 primeiros
termos da progressão, usando a estrutura WHILE.
'''

print('='*40)
print('TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('='*40)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' → ')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')




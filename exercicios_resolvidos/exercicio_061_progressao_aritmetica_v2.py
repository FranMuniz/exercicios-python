'''
Refaça o DESAFIO 51, lendo o primeiro termo
e a razão de uma PA. Mostrando os 10 primeiros
termos da progressão, usando a estrutura WHILE.

DESAFIO 51: Desenvolva um programa que leia o primeiro 
termo e a razão de uma PA. No final, mostre os 10 
primeiros termos dessa progressão.
'''

print('='*40)
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('='*40)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo}', end=' → ')
    termo = termo + razao
    cont += 1
print('Acabou!')

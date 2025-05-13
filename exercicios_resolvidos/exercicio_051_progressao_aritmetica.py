'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print('='*40)
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('='*40)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for i in range (termo, decimo + razao, razao):
    print(f'{i}', end=' → ')
print('Acabou')
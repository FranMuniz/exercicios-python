'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

num = int(input('Digite um número: '))
cont = 0
for i in range (1, num + 1):
    if num % i == 0:
        print('\033[33m', end=' ')
        cont = cont + 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {num} foi divisível {cont} vezes.')

if cont == 2:
    print(f'O número {num} é PRIMO.')
else:
    print(f'O número {num} NÃO É PRIMO.')

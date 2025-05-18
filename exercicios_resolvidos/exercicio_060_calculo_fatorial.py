'''
Faça um programa que leia um número inteiro
qualquer e mostre seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
'''
'''
Forma importando o módulo math
from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(num)
print(f'O fatorial de {num} é {fatorial}')
'''
from time import sleep

num = int(input('Digite um número para calcular seu Fatorial: '))
cont = num
fatorial = 1

print(f'Calculando {num}!')
sleep(2)
while cont > 0:
    print(f'{cont} ', end='')
    print('x ' if cont > 1 else '= ', end='')
    fatorial = fatorial * cont
    cont -= 1
print(f'{fatorial}', end='')
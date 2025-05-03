'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lado diferentes

Desafio 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''
print('-='*12)
print('Analisador de Triângulos')
print('-='*12)

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} PODEM formar um triângulo ', end='') 
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print(f'As retas {r1}, {r2} e {r3} NÃO PODEM formar um triângulo.')
print('-='*12)

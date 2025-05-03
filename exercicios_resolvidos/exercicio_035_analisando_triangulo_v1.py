'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''

print('-='*12)
print('Analisador de Triângulos')
print('-='*12)

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} PODEM formar um triângulo.') 
else:
    print(f'As retas {r1}, {r2} e {r3} NÃO PODEM formar um triângulo.')

print('-='*12)


















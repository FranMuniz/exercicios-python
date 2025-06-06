'''
Faça um programa que leia 5 valores numéricos e guarde-os
em um lista. No final, mostre qual foi o maior e o menor
valor digitado e suas respectivas posições.
'''

valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

print('-'*18)

print(f'Você digitou os valores: {valores}.')

print(f'O maior valor digitado foi: {max(valores)}, nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)}, nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{i}...', end='')
print()
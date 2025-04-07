# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

numero = int(input('Digite um número para ver sua tabuada: '))

print(f'\nTabuada do {numero}:\n')
print('-' * 15)
for i in range(1, 11):
    resultado = numero * i 
    print(f'{numero} * {i} = {resultado}')
print('-' * 15)
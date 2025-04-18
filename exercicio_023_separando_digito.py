'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: 
Digite um número: 1834
Unidade: 4, dezenas: 3, centena: 8, milhar: 1
'''

num = int(input('Informe um número: '))
u = num // 1 % 10 # Número dividido por 1, e pegano o resto da divisão
d = num // 10 % 10 # Número dividido por 1, e pegano o resto da divisão
c = num // 100 % 10 # Número dividido por 1, e pegano o resto da divisão
m = num // 1000 % 10 # Número dividido por 1, e pegano o resto da divisão

print(f'Analisando o número {num}.')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
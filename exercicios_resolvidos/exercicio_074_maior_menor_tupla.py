'''
Crie um programa que vai gerar cinco números aleatórios entre 1 e 100 e 
colocar em uma tupla. Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla.
'''

from random import sample

num_aleatorios = sample(range(1, 1000), 5)
tuple_num_aleatorios = tuple(num_aleatorios)

print(f'Os valores sorteados foram: {tuple_num_aleatorios}')
print(f'O maior valor sorteado foi: {max(tuple_num_aleatorios)}')
print(f'O menor valor sorteado foi: {min(tuple_num_aleatorios)}')
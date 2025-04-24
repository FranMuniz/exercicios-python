# Crie um algoritmo que leia um número inteiro e mostre o seu dobro, triplo e raiz quadrada.
import math

num = float(input('Digite um número: '))
dobro = num * 2
triplo = num * 3 
raiz = math.sqrt(num)

print(f'O dobro de {num} é {dobro}.')
print(f'O triplo de {num} é {triplo}.')
print(f'A raiz quadrada de {num} é {raiz:.2f}')
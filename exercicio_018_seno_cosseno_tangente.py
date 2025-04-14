'''Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo para descobrir seu seno, cosseno e tangente: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo informado foi: {angulo}°')
print(f'O Seno é: {seno:.2f}')
print(f'O Cosseno é: {cosseno:.2f}')
print(f'A Tangente é: {tangente:.2f}')
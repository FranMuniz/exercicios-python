'''Crie um algoritmo que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 4.345
O número 4.345 tem a parte inteira 4'''

from math import trunc # Importa somente uma função, que foi o necessário para o exercício
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua parte inteira é {trunc(num)}')


num2 = float(input('Digite outro valor (teste sem import math): '))
print(f'O valor digitado foi {num2} e a sua parte inteira é {int(num2)}')
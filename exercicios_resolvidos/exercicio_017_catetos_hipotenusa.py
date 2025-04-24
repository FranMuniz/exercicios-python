'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
Teorema de Pitágoras: A soma dos quadrados dos catetos é igual ao quadrado da hipotenusa.
'''
# Maneira matemática, sem import
ca = float(input('Informe o valor do Cateto Adjacente: '))
co = float(input('Informe o valor do Cateto Oposto: '))
hipotenusa = (co ** 2 + ca ** 2) ** (1/2)

print('Sem Import')
print(f'Os catetos são: {ca} e {co}')
print(f'O quadrado da hipotenusa é: {hipotenusa:.2f}')

# Maneira matemática, com import da função hypot da biblioteca math
from math import hypot
ca = float(input('Informe o valor do Cateto Adjacente: '))
co = float(input('Informe o valor do Cateto Oposto: '))
hipotenusa = hypot(co, ca)

print('Com Import (Hypot)')
print(f'Os catetos são: {ca} e {co}')
print(f'O quadrado da hipotenusa é: {hipotenusa:.2f}')

# Maneira matemática, com import da função sqrt da biblioteca math
from math import sqrt
ca = float(input('Informe o valor do Cateto Adjacente: '))
co = float(input('Informe o valor do Cateto Oposto: '))
hipotenusa = sqrt(ca*ca + co*co)

print('Com Import (sqrt)')
print(f'Os catetos são: {ca} e {co}')
print(f'O quadrado da hipotenusa é: {hipotenusa:.2f}')

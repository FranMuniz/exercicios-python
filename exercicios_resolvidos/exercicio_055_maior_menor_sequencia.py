'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre
qual foi o maior e o menor peso lidos.
'''
pesos = []
for i in range (1, 6):
    valor = float(input(f'Informe o {i}º peso: '))
    pesos.append(valor)

print(f'\nO maior peso lido foi: {max(pesos)}kg.')
print(f'O menor peso lido foi: {min(pesos)}kg.')

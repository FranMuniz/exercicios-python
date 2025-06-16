'''
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares 
e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

numeros = [[], []]

for i in range(1,8):
    num = int(input(f'Digite o {i}º número: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
    
print(f'O números pares digitados foram: {sorted(numeros[0])}')
print(f'O números ímpares digitados foram: {sorted(numeros[1])}')

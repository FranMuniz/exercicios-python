'''
Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9;
b) Em que posição foi digitado primeiro valor 3;
c) Quais foram os numeros pares.
'''
numeros = []
pares = 0

for i in range(1, 5):
    num = int(input(f'Informe o {i}º valor: '))
    numeros.append(num)

    if num % 2 == 0:
        pares += 1

numeros_tupla = tuple(numeros)

print(f'O número 9 apareceu {numeros_tupla.count(9)} vezes.')

if 3 in numeros_tupla:
    print(f'O número 3 foi digitado na posição {numeros_tupla.index(3)+1}')
else:
    print('O número 3 não foi digitado em nenhuma posição.')

print(f'Os números pares digitados foram ', end='')
for num in numeros_tupla:
    if num % 2 == 0:
        print(num, end=' ')



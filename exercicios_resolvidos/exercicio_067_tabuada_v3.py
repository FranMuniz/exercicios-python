'''
Faça um progama que mostre a tabuada de vários números inteiros, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o 
número solicitado for negativo.
'''

while True:
    num = int(input('Digite um número para descobrir sua tabuada: '))
    if num < 0:
        break
    for i in range(1, 11):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')
print(f'Programa encerrado!')
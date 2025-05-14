'''
Crie um programa que use um loop for para exibir todos os números primos de 1 até 100.
'''

print('Números primos de 1 a 100:\n')

for num in range(1, 101):
    cont = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        print(num, end=' ')


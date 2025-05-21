'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi a soma entre eles (desconsiderando a flag).
'''

num = int(input('Digite um número [999 para parar!]: '))
parada = 999
cont = 0
soma = 0

while num != parada:
    soma = soma + num
    num = int(input('Digite um número [999 para parar!]: '))
    cont = cont + 1

print(f'Você digitou {cont} números e a soma deles é {soma}.')
print('Acabou')
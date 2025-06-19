'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.
'''

from random import randint
from time import sleep

print('-' * 30)
print('     PALPITES MEGA SENA'     )
print('-' * 30)

quantidade = int(input('Quantos jogos você deseja fazer?: '))
lista = []
jogos = []
total = 1
while total <= quantidade:
    cont = 0

    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-=' * 3)
for i, lista in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {lista}')
print('-=' * 5, f' BOA SORTE! ', '-=' * 5)
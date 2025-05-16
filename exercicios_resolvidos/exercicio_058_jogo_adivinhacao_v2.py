'''
Melhore o jogo do DESAFIO 28 onde o computador vai 'pensar' em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos papalpites foram necessários para vencer.

Desafio 28: Escreva um programa que faça o computador 'pensar' em um número inteiro 
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo 
computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep

computador = randint(0, 10)

print('*-' * 28)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar 🤔')
print('*-' * 28)

jogador = int(input('Em que número eu pensei?: '))
cont = 1

while jogador != computador:
    if jogador < computador:
        print('Quase... tente um número maior ⬆️')
    elif jogador > computador:
        print('Talvez seja melhor tentar um número menor ⬇️')
    jogador = int(input('Tente mais uma vez: '))
    cont += 1
sleep(2)        
print(f'\nVocê acertou após {cont} tentativas. Parabéns 🎉👏🎯')
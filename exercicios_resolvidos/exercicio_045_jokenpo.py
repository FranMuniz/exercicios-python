# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
from colorama import init, Fore
import sys

init(autoreset=True)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA ✊
[1] PAPEL ✋
[2] TESOURA ✌️''')

jogador = int(input('Qual a sua jogada? ')) 
if jogador not in [0, 1, 2]:
    print(Fore.RED + 'Jogada inválida!')
    sys.exit()  # Encerra o programa imediatamente

print(Fore.BLUE + '-=' * 13)
print('JO..')
sleep(1)
print('KEN..')
sleep(1)
print('PÔ!')
sleep(1)
print('🤜    🤛')
print(Fore.BLUE + '-=' * 13)

print(f'Computador escolheu: {itens[computador]}')
print(f'Jogador escolheu: {itens[jogador]}')
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print(Fore.YELLOW + 'Empate!')
    elif jogador == 1:
        print(Fore.GREEN + 'Jogador venceu!')
    elif jogador == 2:
        print(Fore.GREEN + 'Computador venceu!')
    else:
        print(Fore.RED + 'Jogada inválida!')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print(Fore.GREEN + 'Computador venceu!')
    elif jogador == 1:
        print(Fore.YELLOW + 'Empate')
    elif jogador == 2:
        print(Fore.GREEN + 'Jogador venceu!')
    else:
        print(Fore.RED + 'Jogada inválida!')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print(Fore.GREEN + 'Jogador venceu!')
    elif jogador == 1:
        print(Fore.GREEN + 'Computador venceu!')
    elif jogador == 2:
        print(Fore.YELLOW + 'Empate!')
    else:
        print(Fore.RED + 'Jogada inválida!')
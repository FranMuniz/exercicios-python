'''
Sortear entre os jogos de terror para jogar com minha irmã em live
hoje dia 16/05/2025.
'''
import random
from time import sleep

jogos = [    
    "Chased by Darkness",
    "Cry of Fear",
    "Devour",
    "Holy Purge",
    "Pacify",
    "Sign of Silence",
    "Somewhere in the Shadow",
    "Stay Close",
    "Resident Evil 5"
]
jogo_escolhido = random.choice(jogos)
print('\n🎲 Sorteando o melhor jogo ...')
sleep(3)
print('\n🧠 Calma, to pensando bem ...')
sleep(2)
print('\n💡 Já sei!!!!')
sleep(2)
print('\n🎮 O melhor jogo para jogarmos é: ')
sleep(3)
print('\n🥁 TCHRAMMM 🥁')
print(f'\n👉 {jogo_escolhido}')




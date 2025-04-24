'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o
preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
para viagens mais longas.
'''

from time import sleep
from colorama import init, Fore

init(autoreset=True)

distancia = float(input('Informe a distância a ser percorrida (em km): '))

print(Fore.BLUE + f'Você está prestes a começar uma viagem de {distancia} km')
print(Fore.BLUE + f'Calculando o preço da sua passagem, aguarde ...')
sleep(3)

if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50

print(Fore.GREEN + f'O preço da sua passagem será de R${preco:.2f}')



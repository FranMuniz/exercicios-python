'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
from time import sleep
from colorama import init, Fore

init(autoreset=True)

velocidade = float(input('Informe a velocidade do veículo: '))
limite = 80

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7
    print(Fore.RED + f'Você ultrapassou o limite em {excesso:.2f} km/h.')
    print(Fore.BLUE +'Calculando valor da multa, aguarde...')
    sleep(3)
    print(Fore.RED + f'A multa é de R${multa:.2f}')
else:
    print(Fore.GREEN + f'Velocidade de {velocidade} km/h está dentro do limite permitido.')
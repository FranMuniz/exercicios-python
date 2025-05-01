'''
Criar um programa que calcule o valor da passagem com base na idade da pessoa e na distância da viagem. As regras são:
- Se a pessoa tiver menos de 6 anos, a passagem é gratuita.
- Se a pessoa tiver 6 a 17 anos, ou mais de 65 anos, paga meia tarifa.
- Todos os demais pagam tarifa cheia.
A tarifa cheia é de R$0,50 por km.
Seu programa deve pedir:
- A idade da pessoa
- A distância da viagem (em km)
E ao final, deve imprimir o valor da passagem, formatado com duas casas decimais.
'''
from time import sleep
from colorama import init, Fore

init(autoreset=True)

idade = int(input('Informe sua idade: '))
distancia = float(input('Informe a distância a ser percorrida em km: '))
tarifa_inteira = 0.50
tarifa_meia = 0.25

print(Fore.BLUE + 'Calculando valor da passagem...')
sleep(3)

if (idade >= 6 and idade <= 17) or idade > 65:
    valor = distancia * tarifa_meia
    print(Fore.GREEN + 'Elegível a meia tarifa.')
    print(Fore.BLUE + f'Sua passagem custa R${valor:.2f}.')
elif idade < 6:
    print(Fore.GREEN + 'Crianças menores de 6 anos não pagam passagem.')
else:
    valor = distancia * tarifa_inteira
    print(Fore.RED + 'Não elegível a meia tarifa')
    print(Fore.BLUE + f'Sua passagem custa R${valor:.2f}.')





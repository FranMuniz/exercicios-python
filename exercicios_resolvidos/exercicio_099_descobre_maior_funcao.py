'''
Faça um programa que tenha uma função chamada maior(), que
receba vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é maior.
'''
from time import sleep

# Função
def maior(* num):
    cont = maior = 0
    print('-*' * 15)
    print('Analisando os valores informados ...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')



# Main
maior(4, 6, 5, 8, 14, 12)
maior(4, 7, 9)
maior(3, 6)
maior(9)
maior()
'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date 

ano_atual = date.today().year 
cont_menor = 0
cont_maior = 0

for i in range (1, 8):
    ano_nascimento = int(input(f'Informe o ano de nascimento da {i}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print(f'Ao todo tivemos {cont_maior} pessoas maiores de idade, ', end='')
print(f'e {cont_menor} pessoas menores de idade.')





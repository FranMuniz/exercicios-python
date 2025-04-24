'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto, e se o valor 0 for informado,
mostre se o ano atual é bissexto.
'''
from datetime import date

ano = int(input('Qual ano gostaria de analisar? Ou coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')





















    
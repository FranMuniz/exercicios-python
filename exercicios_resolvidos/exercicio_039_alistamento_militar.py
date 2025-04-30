'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do
tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

ano_atual = date.today().year
nascimento = int(input('Informe seu ano de nascimento: '))
idade = ano_atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Faltam {saldo} anos para a obrigatoriedade do alistamento.')
    ano_alistamento = ano_atual + saldo
    print(f'Seu alistamento será em {ano_alistamento}.')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano_alistamento = ano_atual - saldo
    print(f'Seu alistamento foi em {ano_alistamento}.')
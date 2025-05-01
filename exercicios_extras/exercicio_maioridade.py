'''Peça o ano de nascimento do usuário e informe se ele:
- Ainda não atingiu a maioridade (menor de 18 anos),
- Acabou de atingir a maioridade (tem exatamente 18),
- Ou já é maior de idade (mais de 18 anos).
'''

from datetime import date 

ano_atual = date.today().year
ano_nascimento = int(input('Informe seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade > 18:
    print(f'Você já é maior de idade, pois tem {idade} anos.')
elif idade == 18:
    print(f'Você acabou de atingir a maioridade, pois tem {idade} anos.')
else:
    print(f'Você ainda é menor de idade, pois tem {idade} anos.')

'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas notas de cada valor serão fornecidas.
Obs: Considere que o caixa possui notas de R$50, R$20, R$10 e R$1.
'''

print('=' * 16)
print('Caixa Eletrônico')
print('=' * 16)
valor = int(input('Qual valor você deseja sacar? R$ '))
ced = 50
total_ced = 0
total = valor

while True:
    if valor >= ced:
        valor -= ced
        total_ced += 1
    else:
        print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if valor == 0:
            break
print('=' * 35)
print('Volte sempre ao caixa eletrônico!')
print('=' * 35)

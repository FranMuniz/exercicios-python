'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou igual, o aumento é de 15%.
'''

salario = float(input('Informe seu salário: '))

if salario <= 1250:
    salario = salario + (salario * 15 / 100)
    print(f'Você receberá um aumento de 15%, seu novo salário será R${salario:.2f}.')
else:
    salario = salario + (salario * 10 / 100)
    print(f'Você receberá um aumento de 10%, seu novo salário será R${salario:.2f}.')
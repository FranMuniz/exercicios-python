'''Faça um algoritmo que leia os salários de um funcionário e mostre seu novo salário, com 30% de aumento.'''

salario = float(input('Informe seu salário bruto: '))
novo_salario = salario + (salario * 30 / 100)

print(f'Com o aumento de 15% seu novo salário passará a ser R${novo_salario:.2f}, o valor será pago a partir do mês de maio/2025.')
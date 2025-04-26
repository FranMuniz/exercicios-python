'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe o valor do seu salário: R$'))
anos = int(input('Em quantos anos pretende pagar o financiamento?: '))
prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de {valor_casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo CONCEDIDO! :)')
else:
    print('Empréstimo NEGADO! :(')
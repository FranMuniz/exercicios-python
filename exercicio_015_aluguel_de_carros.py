'''Escreva um programa que pergunte a quantidade de KMs percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado'''

qtd_dias = int(input('Informe a quantidade de dias de aluguel: '))
qtd_km = float(input('Informe a quantidade de KMs rodados: '))
valor_total_aluguel = (qtd_dias * 60) + (qtd_km * 0.15)

print(f'O valor total a ser pago pelo aluguel é: R${valor_total_aluguel:.2f}')

# Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares e euros ela pode comprar.
# Considere U$1 = R$5,90

real = float(input('Informe quantos R$ (reais) você tem na carteira?: '))
dolar = float(5.90)
euro = float(6.39)
real_to_dolar = real / dolar
real_to_euro = real / euro

print(f'Você possui R$ {real}, a cotação atual do dólar é U$1 = {dolar}, você pode comprar U$ {real_to_dolar:.2f} ')
print(f'Você possui R$ {real}, a cotação atual do euro é €1 = {euro}, você pode comprar € {real_to_euro:.2f} ')
'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 10% de desconto'''

preco_produto = float(input('Insira o preço do produto: '))
novo_preco_produto = preco_produto - (preco_produto * 10 / 100)

print(f'O preço original do produto é R${preco_produto}, com o desconto de 5%, você pagará apenas R${novo_preco_produto}')
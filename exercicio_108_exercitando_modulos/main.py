'''
Adapte um código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.
'''
from utils import moedas

preco = float(input('Digite o preço: R$'))
metade = moedas.metade(preco)
dobro = moedas.dobro(preco)
aumento = moedas.aumentar(preco)
desconto = moedas.diminuir(preco)

print(f'A metade de {moedas.moeda(preco)} é {moedas.moeda(metade)}')
print(f'O dobro de {moedas.moeda(preco)} é {moedas.moeda(dobro)}')
print(f'Aumentando 10%, temos {moedas.moeda(aumento)}')
print(f'Diminuindo 10%, temos {moedas.moeda(desconto)}')

help(moedas.moeda)
'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.
'''
from utils import moedas

preco = float(input('Digite o preço: R$'))
metade = moedas.metade(preco)
dobro = moedas.dobro(preco)
aumento = moedas.aumentar(preco)
desconto = moedas.diminuir(preco)

print(f'A metade de R${preco} é R${metade}')
print(f'O dobro de R${preco} é R${dobro}')
print(f'Aumentando 10%, temos R${aumento}')
print(f'Diminuindo 10%, temos R${desconto}')

# help(moedas.metade)
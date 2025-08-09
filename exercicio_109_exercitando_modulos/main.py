'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por eles vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
'''
from utils import moedas

preco = float(input('Digite o preço: R$'))
metade = moedas.metade(preco, True)
dobro = moedas.dobro(preco, True)
aumento = moedas.aumentar(preco, True)
desconto = moedas.diminuir(preco, True)

print(f'A metade de {moedas.moeda(preco)} é {metade}')
print(f'O dobro de {moedas.moeda(preco)} é {dobro}')
print(f'Aumentando 10%, temos {aumento}')
print(f'Diminuindo 10%, temos {desconto}')

# help(moedas.moeda)
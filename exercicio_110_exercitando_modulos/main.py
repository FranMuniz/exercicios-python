'''
Adicione ao módulo moeda.py criado nos desagios anteriores, uma função
chamada resumo(), que mostre na tela algumas informações geradas pelas
funções que já temos no módulo criado até aqui.
'''
from utils import moedas

preco = float(input('Digite o preço: R$'))
moedas.resumo(preco, 50, 35)

# help(moedas.moeda)
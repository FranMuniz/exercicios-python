'''
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e
idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas
cadastradas.
'''
from time import sleep
from lib.interface import *
from lib.arquivo import *

arquivo = 'curso.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        sleep(0.5)
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
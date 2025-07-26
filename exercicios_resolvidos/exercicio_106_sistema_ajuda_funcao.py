'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário
vai digitar o comando e o manual aparecer. Quando o usuário digitar a 
palavra 'FIM', o programa se encerrará.
Obs: Use cores.
'''

from time import sleep

c = ('\033[n',          # 0 - Sem cores
     '\033[0;30;41m',   # 1 - Vermelho
     '\033[0;30;42m',   # 2 - Verde
     '\033[0;30;43m',   # 3 - Amarelo
     '\033[0;30;44m',   # 4 - Azul
     '\033[0;30;45m',   # 5 - Roxo
     '\033[7;30m',      # 6 - Branco
    )   

# Função
def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)

# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
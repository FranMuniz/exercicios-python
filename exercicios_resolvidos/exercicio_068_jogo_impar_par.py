'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só
será interrompido quando o jogador PERDER, mostrando o total de 
vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
vitoria = 0

while True:
    jogador = int(input('Informe um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: [P / I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu Par!' if total % 2 == 0 else 'Deu Ímpar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!!')
            vitoria += 1
        else:
            #print('Você perdeu!')
            print(f'Game Over! Você venceu {vitoria} vezes.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
            vitoria += 1
        else:
            #print('Você perdeu!')
            print(f'Game Over! Você venceu {vitoria} vezes.')
            break
    print('Vamos jogar novamente ...')
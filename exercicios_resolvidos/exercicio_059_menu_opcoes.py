'''
Crie um programa que leia dois valores e mostre um menu conforme exemplo abaixo.
O programa deverá realizar a operação solicitada em cada caso.
Ex: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''
from time import sleep

v1 = float(input('Digite o primeiro número: '))
v2 = float(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')

    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = v1 + v2
        print(f'{v1} + {v2} é {soma}')
    elif opcao == 2:
        mult = v1 * v2
        print(f'{v1} x {v2} é {mult:.2f}')
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'Entre {v1} e {v2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente')
        v1 = float(input('Digite o primeiro número: '))
        v2 = float(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando ...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente!')
print('Fim do programa :)')






'''
Crie um programa que leia vários números e os coloque em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores, ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))

    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if opcao in 'SN':
            break  
        else:
            print('Opção inválida! Por favor, digite S para sim ou N para não.')

    if opcao == 'N':
        break

print(f'Você digitou {len(numeros)} números.')

numeros.sort(reverse=True)
print(f'Os números em ordem decrescente são {numeros}')

if 5 in numeros:
    print(f'O valor 5 faz parte da lista.')    
else:
    print('O valor 5 não faz parte da lista.')
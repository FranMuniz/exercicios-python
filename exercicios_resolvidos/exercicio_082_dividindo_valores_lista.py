'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois dissom crie duas listas extras que vão conter openas os 
valores pares e os valores ímpares digitados, respectivamente. Ao
final, mostre o conteúdo das três listas geradas.
'''

lista_completa = []
lista_pares = []
lista_impares = []

while True:
    num = int(input('Digite um número: '))
    lista_completa.append(num)

    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if opcao in 'SN':
            break
        else:
            print('Opção inválida! Por favor, digite S para sim ou N para não.')

    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)


    if opcao == 'N':
        break

print(f'A lista completa é: {lista_completa}')
print(f'A lista de números pares é: {lista_pares}')
print(f'A lista de números ímpares é: {lista_impares}')
'''
Faça um programa que leia nome e peso de várias pessoas, guardando 
tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves.
'''

temp = []
main = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))

    if len(main) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    main.append(temp[:])
    temp.clear()

    while True:
        opcao = str(input('Deseja continuar [S/N]?: ')).strip().upper()
        if opcao in 'SN':
            break
        else:
            print('Opção inválida. Digite S para sim ou N para não')
    if opcao == 'N':
        break

print(f'Ao todo você cadastrou {len(main)} pessoas.')

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in main:
    if i[1] == maior:
        print(f'[{i[0]}] ')

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for i in main:
    if i[1] == menor:
        print(f'[{i[0]}] ')

        

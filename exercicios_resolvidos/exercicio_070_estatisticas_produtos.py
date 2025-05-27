'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se 
o usuário vai continuar ou não. No final, mostre:
- Qual é o total gasto na compra;
- Quantos produtos custam mais de R$ 1000;
- Qual é o nome do produto mais barato.
'''
soma = mais_de_mil = 0
itens = []
while True:
    print('---' * 5)
    print('LOJÃO DO SEU ZÉ')
    print('---' * 5)

    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: '))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if opcao not in 'SN':
        print('Opção inválida! Digite S ou N.')
        continue

    soma += preco 
    itens.append(preco)

    if preco > 1000:
        mais_de_mil += 1

    if opcao == 'N':
        break

print(f'O total gasto na compra foi de R$ {soma:.2f}.')
print(f'Foram {mais_de_mil} produtos que custam mais de R$ 1.000,00')
print(f'O produto mais barato custou {min(itens):.2f}.')



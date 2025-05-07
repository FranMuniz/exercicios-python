'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista em dinheiro ou cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' LOJAS FRAN '))
preco = float(input('Preço das compras: R$'))

print('''FORMA DE PAGAMENTO
[1] À vista em dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')

opcao = int(input('Selecione a opção desejada: '))
parcelas = int(input('Informe o número de parcelas: ')) if opcao == 4 else None

if opcao == 1:
    preco = preco - (preco * 10 / 100)
    print('Você teve um desconto de 10%,', end='')
    print(f' sua compra ficou no valor de R${preco:.2f}')
elif opcao == 2:
    preco = preco - (preco * 5 / 100)
    print('Você teve um desconto de 5%,', end='')
    print(f' sua compra ficou no valor de R${preco:.2f}')
elif opcao == 3:
    parcelas = preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas:.2f} SEM JUROS.')
    print(f'Valor total: R${preco:.2f}')
elif opcao == 4:
    if parcelas < 3:
        print('Número de parcelas inválido para a opção desejada.')
    else:
        preco_final = preco + (preco * 20 / 100)
        parcela_juros = preco_final / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${parcela_juros:.2f} COM JUROS.')
        print(f'Sua compra de R${preco:.2f} custará R${preco_final:.2f}.')
else:
    print('Opção inválida de pagamento.')



    
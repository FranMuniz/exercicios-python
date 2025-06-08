'''
Crie um programa onde o usuário possa digitar vários valores
numéricos inteiros e cadastre-os em uma lista. Caso o número já
exista na lista, ele não será adicionado novamente. No final,
serão exibidos todos os valores únicos digitados, em ordem
crescente.
'''
from colorama import init, Fore
init(autoreset=True)

numeros = []

while True:
    valor = int(input('Digite um número: '))

    if valor not in numeros:
        numeros.append(valor)
        print(Fore.GREEN + 'Valor adicionado com sucesso!')
    else:
        print(Fore.RED + 'Valor duplicado. Não adicionado!')

    opcao = str(input('Deseja continuar [S/N]?: ')).upper().strip()

    if type(opcao) is not str or opcao not in 'SsNn':
        print(Fore.RED + 'Opção inválida. Digite novamente...')  
        opcao = str(input('Deseja continuar [S/N]?: ')).upper().strip()

    if opcao == 'N':
        break

print(Fore.BLUE + f'Você digitou os valores {sorted(numeros)}')





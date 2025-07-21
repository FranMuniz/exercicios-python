'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Pyhton, só que fazendo a validação para 
aceitar apenas um valor numérico.
Ex:
    n = leiaInt('Digite um número: ')
'''

# Função
def leiaInt(msg):
    """
    -> Lê apenas números.
    :param num: Número a ser lido
    Função criada por Francieli Muniz
    """
    from colorama import init, Fore
    init(autoreset=True)

    ok = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(Fore.RED + 'ERRO! Digite um número inteiro válido!')
        if ok:
            break
    return valor


# Programa Principal
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
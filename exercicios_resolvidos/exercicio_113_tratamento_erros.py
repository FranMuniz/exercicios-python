'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade 
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.
'''

# Função
def leiaInt(num):
    """
    -> Lê um número inteiro e aplica tratamento de erros.
    :param num: Número a ser lido
    Função criada por Francieli Muniz
    """
    from colorama import init, Fore
    init(autoreset=True)

    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO! Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print(Fore.RED + 'Usuário preferiu não digitar o número!')
            return 0
        else:
            return n
        

def leiaFloat(num):
    """
    -> Lê um número real e aplica tratamento de erros.
    :param num: Número a ser lido
    Função criada por Francieli Muniz
    """
    from colorama import init, Fore
    init(autoreset=True)

    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print(Fore.RED + 'ERRO! Digite um número real válido!')
            continue
        except KeyboardInterrupt:
            print(Fore.RED + 'Usuário preferiu não digitar o número!')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O número Inteiro digitado foi: {n1}')
print(f'O número Real digitado foi: {n2}')
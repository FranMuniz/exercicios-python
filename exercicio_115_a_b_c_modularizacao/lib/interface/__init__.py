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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será
um valor lógico (opcional) indicando se será mostrado ou não na tela o 
processo de cálculo do fatorial.
'''

# Função
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado;
    :param show: Mostrar ou não a conta (opcional), por default (False) 
    :return: O valor do Fatorial de um número num
    Função criada por Francieli Muniz
    """
    f = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont 
    return f

# Programa Principal
n = int(input('Informe um número: '))
print(fatorial(n, show=True))
print(fatorial(n))
help(fatorial)

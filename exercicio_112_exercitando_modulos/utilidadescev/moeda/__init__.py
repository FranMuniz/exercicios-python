def aumentar(num=0, taxa=0, formato=False):
    """
    -> Calcula aumento de 10%.
    :param num: número a ser calculado;
    :return: número + 10% 
    Função criada por Francieli Muniz
    """
    res = num + (num * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    """
    -> Calcula diminuição de 10%.
    :param num: número a ser calculado;
    :return: número - 10% 
    Função criada por Francieli Muniz
    """
    res = num - (num * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    """
    -> Calcula dobro de um número.
    :param num: número a ser calculado;
    :return: o dobro do número 
    Função criada por Francieli Muniz
    """
    res = num * 2
    return res if formato is False else moeda(res)


def metade(num=0, formato=False):
    """
    -> Calcula metade de um número.
    :param num: número a ser calculado;
    :return: a metade do número 
    Função criada por Francieli Muniz
    """
    res = num / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Formata moeda.
    :param preco: número a ser formatado;
    :param moeda: moeda a ser apresentada;
    :return: string formatada
    Função criada por Francieli Muniz
    """
    return f'{moeda}{preco:>4.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 35)
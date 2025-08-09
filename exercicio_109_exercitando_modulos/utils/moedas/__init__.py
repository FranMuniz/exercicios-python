def aumentar(num=0, formato=False):
    """
    -> Calcula aumento de 10%.
    :param num: número a ser calculado;
    :return: número + 10% 
    Função criada por Francieli Muniz
    """
    res = num + (num * 0.10)
    return res if formato is False else moeda(res)


def diminuir(num=0, formato=False):
    """
    -> Calcula diminuição de 10%.
    :param num: número a ser calculado;
    :return: número - 10% 
    Função criada por Francieli Muniz
    """
    res = num - (num * 0.10)
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
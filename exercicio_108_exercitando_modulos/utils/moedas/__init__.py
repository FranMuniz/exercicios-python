def aumentar(num=0):
    """
    -> Calcula aumento de 10%.
    :param num: número a ser calculado;
    :return: número + 10% 
    Função criada por Francieli Muniz
    """
    return num + (num * 0.10)


def diminuir(num=0):
    """
    -> Calcula diminuição de 10%.
    :param num: número a ser calculado;
    :return: número - 10% 
    Função criada por Francieli Muniz
    """
    return num - (num * 0.10)


def dobro(num=0):
    """
    -> Calcula dobro de um número.
    :param num: número a ser calculado;
    :return: o dobro do número 
    Função criada por Francieli Muniz
    """
    return num * 2


def metade(num=0):
    """
    -> Calcula metade de um número.
    :param num: número a ser calculado;
    :return: a metade do número 
    Função criada por Francieli Muniz
    """
    return num / 2


def moeda(preco=0, moeda='R$'):
    """
    -> Formata moeda.
    :param preco: número a ser formatado;
    :param moeda: moeda a ser apresentada;
    :return: string formatada
    Função criada por Francieli Muniz
    """
    return f'{moeda}{preco:>4.2f}'.replace('.', ',')
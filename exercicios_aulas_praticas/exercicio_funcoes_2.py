# Interactive help
# help(print)

##################################################

# Docstrings -> String de documentação
def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p 
    print('FIM!')

help(contador)

##################################################

# Parâmetros opcionais
def somar(a=0, b=0, c=0): # Se c não for informado, terá valor zero
    """
        -> Faz a soma dos valores e mostra na tela.
        :param a: primeiro valor
        :param b: segundo valor
        :param c: terceiro valor
        Função criada por Francieli Muniz
    """
    s = a + b + c 
    print(f'A soma vale {s}')

help(somar)
somar(2, 3, 6)
somar(5, 9)
somar()

##################################################

# Retorno de valores

def somar(a=0, b=0, c=0): # Se c não for informado, terá valor zero
    """
        -> Faz a soma dos valores e mostra na tela.
        :param a: primeiro valor
        :param b: segundo valor
        :param c: terceiro valor
        Função criada por Francieli Muniz
    """
    s = a + b + c 
    return s

r1 = somar(5, 5)
r2 = somar(2, 1, 3)
print(f'Meus cálculos deram {r1} e {r2}')

##################################################

# Exercício Aula prática

def fatorial(num=1):
    f = 1
    for cont in range(num, 0, -1):
        f *= cont 
    return f

# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(6)
f2 = fatorial(5)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
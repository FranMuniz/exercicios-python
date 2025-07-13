'''
Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''

# Função 
def voto(ano_nasc):
    """
        -> Analisa idade e mostra na tela o resultado.
        :param ano_nasc: ano de nascimento a ser analisado
        Função criada por Francieli Muniz
    """
    from datetime import date
    print('=' * 30)

    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: VOTO OPCIONAL!')
    else:
        print(f'Com {idade} anos: VOTO NEGADO!')
    
    print('=' * 30)

# Programa principal
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)

help(voto)



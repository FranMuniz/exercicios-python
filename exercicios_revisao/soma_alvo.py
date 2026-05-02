'''
Dada uma lista:
    [2, 7, 11, 15]
E um alvo:
    9
Retorne dois números que somam o alvo.
'''

def soma(nums, alvo):
    # Dicionário para armazenar: {número: índice}
    mapa = {}

    for i, num in enumerate(nums):
        complemento = alvo - num

        # Se o complemento já existe no mapa, encontro a solução
        if complemento in mapa:
            return [mapa[complemento], i]

        # Caso contrário, adiciona o número atual
        mapa[num] = i 

# Entrada
lista = [2, 7, 11, 15]
alvo = 9

# Resultado 
print(f'Índices: {soma(lista, alvo)}')

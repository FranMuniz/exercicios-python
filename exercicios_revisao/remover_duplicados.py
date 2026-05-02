'''
Dada uma lista:
    [1, 2, 3, 2, 1, 4, 5, 1]
Retorne uma nova lista sem duplicados, mas mantendo a ordem original.
'''

lista = [1, 2, 3, 2, 1, 4, 5, 1]
nova_lista = list(dict.fromkeys(lista)) # -> Esse método cria um dicionário usando os elementos como chaves (removendo duplicatas automaticamente, 
                                        # pois chaves são únicas) e converte de volta para uma lista, preservando a ordem de inserção

print(nova_lista)


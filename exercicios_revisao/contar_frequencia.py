'''
Dada uma lista:
    ["a", "b", "a", "c", "b", "a"]
Retorne um dicionário com a contagem de cada elemento.

Ex esperado: {"a": 3, "b": 2, "c": 1}
'''

lista = ['a', 'b', 'a', 'c', 'b', 'a']
contagem = {}

for item in lista:
    contagem[item] = contagem.get(item, 0) + 1

print(contagem)


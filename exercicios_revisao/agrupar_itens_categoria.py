'''
Dada uma lista de dicionários:
    [
    {"produto": "camisa", "categoria": "roupa"},
    {"produto": "calça", "categoria": "roupa"},
    {"produto": "celular", "categoria": "eletronico"}
    ]
Transforme em:
    {
    "roupa": ["camisa", "calça"],
    "eletronico": ["celular"]
    }
'''

dados = [
    {'produto': 'camisa', 'categoria': 'roupa'},
    {'produto': 'calça', 'categoria': 'roupa'},
    {'produto': 'calular', 'categoria': 'eletronico'},
]

resultado = {}

for item in dados:
    categoria = item['categoria']
    produto = item['produto']

    if categoria not in resultado:
        resultado[categoria] = []

    resultado[categoria].append(produto)

print(resultado)


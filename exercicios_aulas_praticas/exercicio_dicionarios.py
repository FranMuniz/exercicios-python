pessoas = {'nome': 'Francieli', 'sexo': 'F', 'idade': 28}

for key in pessoas.keys():
    print(key)

for value in pessoas.values():
    print(value)

for key, value in pessoas.items():
    print(f'{key} = {value}')

pessoas['nome'] = 'Amanda' # Modificar
pessoas['peso'] = 54.6

print(pessoas)
print(pessoas['nome'])
print(f'A {pessoas['nome']} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['nome'] = 'André'
# del pessoas['sexo'] # Apagar em dicionários

####################

# Dicinários dentro de listas
brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Minas Gerias', 'sigla': 'MG'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(estado1)
print(brasil[1])
print(brasil[0]['uf'])

####################

# Cópia de dicinários 

estado = {}
brasil = []

for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for estado in brasil:
    for valor in estado.values():
        print(valor, end=' ')
        print()
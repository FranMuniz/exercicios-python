

num = [1, 2, 3, 4] # Declaração da lista
num[2] = 15 # Alterar o valor
num.append(7) # Adicionar um valor
num.sort() # Ordenar em ordem crescente
num.sort(reverse=True) # Ordenar em ordem decrescente
num.insert(2, 67) # Inserir na lista (índice, valor)
num.pop() # Sem parâmetro, elimina o último elemento.
num.pop(1)

num.insert(2,2)
num.remove(2) # Procura a primeira ocorrência e elimina
# num.remove(3) # Da erro pois o 3 não existe na lista
if 3 in num:
    num.remove(3)
else:
    print('Não achei o número 3.')

print(num)
print(f'Essa lista tem {len(num)} elementos.')

#######################################

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores: # Mostrar os valores
    print(f'{valor}...')

for indice, valor in enumerate(valores): # Mostrar os índices e valores
    print(f'Na posição {indice}, encontrei o valor {valor}.')

#######################################

listinha = []

for cont in range(0, 5):
    listinha.append(int(input('Digite um valor: ')))

for ind, val in enumerate(listinha):
    print(f'No índice {ind} encontrei o valor {val}.')
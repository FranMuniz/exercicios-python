# Tuplas são entre (parênteses) 
# Tuplas são IMUTÁVEIS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[-2])
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

# lanche[1] = 'Refrigerante' # Tuplas são IMUTÁVEIS

# Primeira opção
for comida in lanche:
    print(f'Eu vou comer {comida}') # --> Se não precisar mostrar a posição, usar dessa forma
print('Comi pra caramba!')

# Segunda opção
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') # --> Sempre que precisar mostrar a posição, usar dessa forma
print('Comi pra caramba!')

# Terceira opção
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') # --> Sempre que precisar mostrar a posição, usar dessa forma
print('Comi pra caramba!')

# Organizar a tupla (ordem alfabética)
print(sorted(lanche))

# Concatenar tuplas
a = (10, 9, 8, 7)
b = (1, 2, 3, 4, 1)
c = a + b
print(c)
print(len(c))
print(c.count(1))
print(c.index(7))


pessoa = ('Fran', 28, 'F', 80) # Pode ter tipo diferentes em uma mesma tupla
print(pessoa)
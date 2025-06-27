# Função
def soma (a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(a=4, b=5)

##############

# Função
def soma(*valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'Somando os valores {valores} temos {soma} :)')

# Programa principal
soma(4, 5, 3)
soma(3, 4)

##############

# Função
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

# Programa principal
valores = [5, 18, 3, 8]
dobra(valores)
print(valores)
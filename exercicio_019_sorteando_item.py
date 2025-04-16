'''Um professor quer sortear um dos seus quatro alunos apara apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e apresentando o nome do escolhido.'''

# Básico

from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print(f'O aluno escolhido foi: {escolhido}')

##################

# Com loop

from random import choice

quantidade = int(input('Quantos alunos você quer inserir? '))
alunos = []

for i in range(1, quantidade + 1):
    nome = input(f'Aluno {i}: ')
    alunos.append(nome)

escolhido = choice(alunos)

print(f'O aluno escolhido foi: {escolhido}')

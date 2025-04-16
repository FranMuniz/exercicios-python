'''O mesmo professor do desafio anterior (019) quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

# Básico
from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]

shuffle(lista)
print(f'A ordem de apresentação será: {lista}')

##################################################################

# Com loop

from random import shuffle

quantidade = int(input('Quantos alunos você deseja inserir? ')) 
alunos = []

for i in range(1, quantidade + 1):
    nome = input(f'Aluno {i}: ')
    alunos.append(nome)

shuffle(alunos)
print(f'A ordem de apresentação escolhida é: {alunos}')

'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
o último nome separadamente.
Ex: Francieli dos Santos Muniz
primeiro: Francieli
último: Muniz
'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print(f'Muito prazer em te conhecer {n}')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu útimo nome é {nome[len(nome)-1]}')
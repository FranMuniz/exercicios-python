'''
Crie um programa que leia o nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    while True:
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()
        if opcao in 'SN':
            break
        else:
            print('Opção inválida. Digite S para Sim ou N para Não.')
    if opcao == 'N':
        break
print('-' * 26) 
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 26)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 26)
    opcao = int(input('Mostrar notas de qual aluno? [000 interrompe]: '))
    if opcao == 000:
        print('Finalizando ...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')
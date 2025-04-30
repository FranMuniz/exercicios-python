'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5: Reprovado
- Média entre 5 e 6,9: Recuperação
- Média 7 ou superior: Aprovado
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print(f'A média das notas {n1} e {n2} é {media:.2f}')
if media < 5:
    print(f'O aluno está REPROVADO!')
elif media <= 6.9:
    print(f'O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')

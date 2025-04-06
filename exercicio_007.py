# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre suas médias e diga se ele foi aprovado ou não.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média das notas {nota1} e {nota2} é: {media}')

if media >= 7:
    print('Aluno aprovado! :)')
else:
    print('Aluno reprovado :(')
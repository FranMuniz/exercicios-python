'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas são maiores de idade;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos.
'''
maiores_idade = mulheres_menores = homens_cadastrados = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if idade >= 18:
        maiores_idade += 1
    if idade < 20 and sexo == 'F':
        mulheres_menores += 1
    if sexo == 'M':
        homens_cadastrados += 1

    if opcao == 'N':
        break

print(f'''
    Total de pessoas maiores de idade: {maiores_idade}.
    Ao todo temos {homens_cadastrados} homens cadastrados.
    Temos {mulheres_menores} mulheres com menos de 20 anos.
    ''')
'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionario e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas;
B) A média de idade;
C) Uma lista com as mulheres;
D) Uma lista com idade acima da média.
'''

pessoa = {}
galera = []
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('Erro! Por favor digite apenas F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('Erro! Por favor digite apenas S ou N.')
    if opcao == 'N':
        break

print('-=' * 20)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p['nome']} ')
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for key, value in p.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<< ENCERRADO >>')
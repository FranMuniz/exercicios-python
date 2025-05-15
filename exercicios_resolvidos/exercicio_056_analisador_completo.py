'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo;
- Qual o nome do homem mais velho;
- Quantas mulheres têm menos de 20 anos.
'''

nomes = []
idades = []
generos = []
mulheres_menores_vinte_anos = 0
idade_mais_velho = 0
nome_velho = ''

for i in range (1, 5):
    print(f'---- {i}ª PESSOA ----')
    nome = str(input(f'Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    genero = str(input('Sexo [F/M]: ')).upper().strip()

    while genero not in ['F', 'M']:
        print('Gênero inválido. Digite novamente.')
        genero = input('Sexo [F/M]: ').strip().upper()

    nomes.append(nome)
    idades.append(idade)
    generos.append(genero)

    if genero == 'F' and idade < 20:
        mulheres_menores_vinte_anos += 1 

    if genero == 'M' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_velho = nome
    
media_idades = sum(idades) / len(idades)

print(f'\nA média de idade do grupo é de {media_idades} anos.')
print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_velho}.')
print(f'Ao todo são {mulheres_menores_vinte_anos} mulheres com menos de 20 anos.')

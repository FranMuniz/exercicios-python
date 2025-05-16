'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter o valor correto.
'''

genero = str(input('Gênero [F/M]: ')).upper().strip()[0]

while genero not in 'MmFf':
    genero = str(input('Gênero inválido. Por favor, informe seu gênero: ')).upper().strip()[0]
print(f'Gênero {genero} registrado com sucesso.')
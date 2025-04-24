'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas;
- Quantas letras ao todo (sem considerar os espaços);
- Quantas letras tem o primeiro nome.
'''

nome_completo = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome ...')
print(f'Seu nome em maiúsculo é: {nome_completo.upper()}')
print(f'Seu nome em minúsculo é: {nome_completo.lower()}')
print(f'Seu nome possui {len(nome_completo.replace(' ', ''))} caracteres.')

separa = nome_completo.split()
print(f'Seu primeiro nome é {separa[0]} e ele possui {len(separa[0])} letras.')
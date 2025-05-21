'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
'''
soma = cont = 0
num = int(input('Digite um número: '))
soma += num
cont += 1
resposta = str(input('Quer continuar? [S/N] ')).upper()
maior = menor = num

while resposta == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper()

media = soma / cont
print(f'Você digitou {cont} números e a média deles é {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
'''
Faça um programa que leia três números inteiros e mostre qual é o menor e qual é o maior. 
'''
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

# Verifica o menor
menor = primeiro 
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

# Verifica o maior
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

print(f'O menor número digitado foi {menor}.')
print(f'O maior número digitado foi {maior}.')
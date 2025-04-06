# Fazer um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input('Digite alguma coisa: ')

print('O tipo primitivo é: ', type(palavra))
print('Só tem espaços? ', palavra.isspace())
print('É um número? ', palavra.isnumeric())
print('É alfabético? ', palavra.isalpha())
print('É alphanumérico? ', palavra.isalnum())
print('Está em maiúsculas?' , palavra.isupper())
print('Está em minúsculas?' , palavra.islower())
print('Está capitalizada? ', palavra.istitle())
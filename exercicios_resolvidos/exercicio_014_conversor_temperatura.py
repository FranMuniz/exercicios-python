# Escreva um programa que converta uma temperatura digitada em ºC para ºF

c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32 # --> Não precisa de parenteses pq a ordem de precedência já é * ou / (o que aparecer primeiro) e depois o + ou -

print(f'A temperatura de {c}ºC corresponde a {f}ºF')
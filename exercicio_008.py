# Escreva um programa que leia um valor em km, e o exiba convertido em metros, centímetros e milímetros.

km = float(input('Digite uma distância em km: '))
m = km * 1000
cm = km * 100000
mm = km * 1000000

print(f'A medida de {km}km corresponde a {m}m, {cm:.0f}cm e {mm:.0f}mm')
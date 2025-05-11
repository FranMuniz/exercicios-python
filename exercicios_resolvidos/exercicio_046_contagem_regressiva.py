'''
Faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifício de ano novo, indo de 10 até 0, com uma
pausa de um segundo entre eles.
'''

from time import sleep
for i in range (10, 0, -1):
    print(i)
    sleep(1)
print('Happy New Year!!!!!')
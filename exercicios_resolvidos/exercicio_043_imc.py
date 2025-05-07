'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com as informações abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)

print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do seu peso ideal.') 
elif 18.5 <= imc < 25:
    print('Parabéns, você está no seu peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Atenção, você está obeso!')
else:
    print('ATENÇÃO, você está com obesidade mórbida!!!')




    
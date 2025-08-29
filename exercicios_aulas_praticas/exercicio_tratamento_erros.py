try:
    a = int(input('Numerador: '))
    b = int(input('Denomidaor: '))
    r = a / b 
#except Exception as e:
    #print(f'Infelizmente tivemos um problema: {e}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
else:
    print(f'O resultado é {r:.1f}')
finally: # Sempre acontece, se der erro ou não
    print('Volte sempre! Muito obrigada :)')

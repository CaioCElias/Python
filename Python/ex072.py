"""
EXERCÍCIO 072: Número por Extenso
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',\
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    escolha = int(input('Escolha um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente. ', end='')

extenso = numeros[escolha]
print(f'Você escolheu o número: {extenso}')

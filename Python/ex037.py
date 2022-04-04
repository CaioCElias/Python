# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão:
# - 1 para Binário
# - 2 para Octal
# - 3 para Hexadecimal
numero = int(input('Escreva um número inteiro: '))
base = int(input('''Qual será a base de conversão?
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal
'''))
if base == 1:
    print(f'O número {numero} em Binário é {bin(numero)[2:]}')
elif base == 2:
    print(f'O número {numero} em Octal é {oct(numero)[2:]}')
elif base == 3:
    print(f'O número {numero} em Hexadecimal é {hex(numero)[2:]}')
else:
    print('Escolha uma opção válida')

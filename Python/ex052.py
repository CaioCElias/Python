# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
final = num + 1
cont = 0

for c in range(1, final):
    if num % c == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')

print(f'\n\033[mO número {num} foi dividido {cont} vezes')
if cont == 2:
    print(f'Portanto o número {num} É PRIMO!')
elif cont > 2:
    print(f'Portanto, o número {num} NÃO É PRIMO!')

"""
DESAFIO 074: Maior e Menor Valores em Tupla
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""

from random import randint

# Gerando números aleatórios
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

# Organizando em uma tupla
print('Os valores sorteados foram: ', end='')
for tupla in numeros:
    print(f'{tupla} ', end='')

# Organizando a tupla do menor pro maior, para sempre o 1º número ser o menor e o 5º o maior
organizar = sorted(numeros)
print(f'\nO menor valor é: {organizar[0]}')
print(f'O maior valor é: {organizar[-1]}')

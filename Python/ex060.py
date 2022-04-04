# Faça um programa que leia um número qualquer e mostre seu fatorial.
from math import factorial
fatorial = int(input('Digite um número para calcular o fatorial: '))
print(f'\033[1;31mCalculando {fatorial}!\033[m', end=' → ')
count = fatorial
while count > 0:
    print(count, end='')
    print(' x ' if count > 1 else ' = ', end='')
    count -= 1
print(factorial(fatorial))

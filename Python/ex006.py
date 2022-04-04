# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
a = int(input('Digite um número: '))
print(f'O dobro de {a} vale {a*2}')
print(f'O triplo de {a} vale {a*3}')
print(f'A raiz quadrada de {a} vale {sqrt(a):.2f}')

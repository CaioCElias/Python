# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
a = (co ** 2) + (ca ** 2)
b = sqrt(a)
print(f'A hipotenusa é {b:.2f}')

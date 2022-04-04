# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

# Calcular o menor valor
menor = a # Eliminar a necessidade de 1 if
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor é: {menor}')

# Calcular o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior é {maior}')
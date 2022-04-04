# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
nome = input('Digite seu nome completo: ').strip().capitalize()
import time
time.sleep(2)
print('Muito prazer em te conhecer!')

# Separar nomes
a = nome.split()
print(f'Seu primeiro nome é {a[0]}')
print(f'Seu último nome é {a[-1].capitalize()}')
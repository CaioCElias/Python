# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas e minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome...')
import time
time.sleep(3)

# Diz o nome em MAÍUSCULAS
print(f'Seu nome em MAÍUSCULAS é {nome.upper()}')
time.sleep(1)

# Diz o nome em minúsculas
print(f'Seu nome em minúsculas é {nome.lower()}')
time.sleep(1)

# Conta as letras
nome2 = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {nome2} letras')

# Descobre o primeiro nome e diz quantas letras ele tem
time.sleep(1)
nome3 = nome.split()
print(f'Seu primeiro nome é {nome3[0]} e ele tem {len(nome3[0])} letras')

# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
jovem = 0
adulto = 0

for c in range(1, 8):
    ano = int(input(f'Digite em que ano a {c}ª pessoa nasceu: '))
    if atual - ano < 18:
        jovem += 1
    elif atual - ano >= 18:
        adulto += 1

print(f'\nAo todo tem {adulto} pessoas maiores de idade')
print(f'E {jovem} pessoas menores de idade')

# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Digite o ano que você deseja analisar: '))

from datetime import date

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto')

else:
    print(f'O ano {ano} NÃO é bissexto')

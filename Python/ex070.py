'''
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
'''

print('-'*30)
print('LOJA SUPER BARATÃO')

total = 0
acimadeMil = 0
maisBarato = ''
menorPreco = 0
cont = 0

while True:
    print('-' * 30)
    nome = str(input('Nome do produto: ')).capitalize().strip()
    preco = float(input('Preço: R$'))

    cont += 1
    total += preco
    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        maisBarato = nome
    if preco > 1000:
        acimadeMil += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('=-'*15)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {acimadeMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi "{maisBarato}" que custa R${menorPreco:.2f}')

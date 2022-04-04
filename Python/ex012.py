# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual é o preço do produto? R$ '))
desconto = (preco / 100) * 5
final = preco - desconto
print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${final:.2f}')

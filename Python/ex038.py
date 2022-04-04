# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior.
# - O segundo valor é maior.
# - Não existe valor maior, os dois são iguais.
a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
if a > b:
    print('O PRIMEIRO valor é MAIOR')
elif a < b:
    print('O SEGUNDO valor é MAIOR')
elif a == b:
    print('Os dois valores são iguais')

# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.
resposta = 'S'
soma = count = maior = menor = 0
while 'S' in resposta:
    count += 1
    num = float(input('Digite um número: '))
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += num
print(f'Você digitou {count} números e a média deles foi de {soma/count}')
print(f'O maior número é {maior} e o menor é {menor}')

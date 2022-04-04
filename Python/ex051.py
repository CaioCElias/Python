# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
geral = primeiro + (10 - 1) * razao
maximo = geral + razao
for c in range(primeiro, maximo, razao):
    print(c, end='-')
print('FIM')

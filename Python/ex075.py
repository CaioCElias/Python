"""
DESAFIO 075: Análise de Dados em uma Tupla
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

numeros = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')),
           int(input('Digite o 4º valor: ')))

print('-'*30)
print(f'Você digitou os valores: ', end='')
for tupla in numeros:
    print(tupla, end=' ')

# A) Quantas vezes apareceu o valor 9.
valorNove = numeros.count(9)
if valorNove == 1:
    vez = 'vezes'
else:
    vez = 'vezes'
print(f'\nO valor 9 apareceu {valorNove} {vez}')

# B) Em que posição foi digitado o primeiro valor 3.
contarTres = numeros.count(3)
if contarTres != 0:
    posTres = numeros.index(3) + 1
    print(f'O primeiro valor 3 foi na {posTres}ª posição')
else:
    print('O número 3 NÃO foi digitado nenhuma vez')

# C) Quais foram os números pares.
pares = 0
valoresPares = ''
for n in numeros:
    if n % 2 == 0:
        pares += 1
        valoresPares += ' ' + str(n)

if pares > 0:
    print(f'Os números pares foram:{valoresPares}')
else:
    print('Não há números pares')

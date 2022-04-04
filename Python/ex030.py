# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Me diz um número: '))

# Mostrar de é Impar ou par
conta = num % 2
if conta == 0:
    print(f'O número {num} é um número par')
else:
    print(f'O número {num} é um número impar')

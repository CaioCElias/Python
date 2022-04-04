# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').strip().upper()

# Contar palavra na frase
a = frase.count('A')
print(f'A letra A aparece {a} vezes na frase')

# Achar a letra A
b = frase.find('A') + 1
print(f'A primeira letra A apareceu na posição {b}')

# Achar a letra A²
c = frase.rfind('A') + 1
print(f'A última letra A apareceu na posição {c}')

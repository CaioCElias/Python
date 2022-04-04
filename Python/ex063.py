# Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
t1 = 0 # Primeiro termo
t2 = 1 # Segundo termo

quantos = int(input('Quantos termos você quer mostrar? ')) # Quantos termos vai mostrar?
cont = 2 # Por ter 2 termos ja, o contador começa no 2

print(f'{t1} → {t2}', end='')
while cont < quantos:
    t3 = t1 + t2 # Sequencia de Fibonacci
    print(t3, end=' → ') # Mostrar todos os termos
    cont += 1 # Contar quantas vezes passou
    t1 = t2 # T1 vira o T2
    t2 = t3 # T2 vira o T3
print('Fim')

# Faça um programa que calcule a soma entre todos os números ímpares que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for valores in range(1, 501, 2):
    if valores % 3 == 0:
        contador = contador + 1
        soma = soma + valores
print(f'A soma {contador} valores é igual a {soma}')

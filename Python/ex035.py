# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print(f'Com os valores {a, b, c} é POSSÍVEL formar um triângulo')
else:
    print(f'Com os valores {a, b, c} é IMPOSSÍVEL formar um triângulo')

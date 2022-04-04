# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(angulo)
print(f'O ângulo de {angulo} tem o SENO de {math.sin(rad):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {math.cos(rad):.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {math.tan(rad):.2f}')

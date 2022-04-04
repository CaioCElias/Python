# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
km = float(input('Quantos quilometros foram percorridos? '))
dias = float(input('Por quantos dias o carro foi alugado? '))
x = dias * 60
y = 0.15 * km
z = x + y
print(f'O preço final é de R${z:.2f}')

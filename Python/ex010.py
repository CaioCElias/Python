# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar.
qntd = float(input('Quanto dinheiro você tem na sua carteira? R$ '))
conv = qntd / 3.27
print(f'Com R${qntd} vc pode comprar US${conv:.2f}')

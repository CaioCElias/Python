# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade < 80:
    print('Muito Bem! Pode Continuar!')
else:
    multa = (velocidade - 80) * 7
    print('Multado!')
    print(f'Você pagará uma multa de R${multa:.2f}')

# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
distancia = float(input('Distância em KM da sua viagem: '))
if distancia <= 200:
    conta = distancia * 0.50
else:
    conta = distancia * 0.45
print(f'A sua viagem custará de R${conta}')

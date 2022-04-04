# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
altura = float(input('Digite a altura (Metros): '))
peso = float(input('Digite o peso em (KG): '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Você está ABAIXO DO PESO')
elif imc <= 25:
    print(f'Seu IMC é {imc:.2f}. Você está com o PESO IDEAL')
elif imc <= 30:
    print(f'Seu IMC é {imc:.2f}. Você está com SOBREPESO')
elif imc <= 40:
    print(f'Seu IMC é {imc:.2f}. Você está com OBESIDADE')
else:
    print(f'Seu imc é {imc:.2f}. Você está com OBESIDADE MORBIDA')

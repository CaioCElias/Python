# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o salário do funcionário? R$ '))
aumento = (salario / 100) * 15
final = salario + aumento
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${final:.2f}')
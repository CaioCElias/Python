# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.
salario = int(input('Qual é o seu salário? R$'))

if salario <= 1250:
    aumento = salario + (salario / 100 * 15)
    print(f'Seu novo salário é R${aumento:.2f}')

else:
    aumento = salario + (salario / 100 * 10)
    print(f'Seu novo salário é R${aumento:.2f}')

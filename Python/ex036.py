# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.

valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? ')) * 12

prestacao = (valor / tempo)
porcentagem = (salario / 100 * 30)

print(f'Para pagar uma casa de R${valor} em {tempo/12} ano(s), a prestação será de R${prestacao:.2f}')
if prestacao <= porcentagem:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')

# Elabore um programa que calcule o valor a ser pago de um produto,
# considerando o seu preço normal, e condição de pagamento:
# - À vista no dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] parcelado no cartão''')

escolha = int(input('Escolha sua opção: '))
if escolha == 1:
    valor = preco - (preco / 100 * 10)
    print(f'Você ganhou 10% de desconto e o valor ficou de R${valor:.2f}')
elif escolha == 2:
    valor = preco - (preco / 100 * 5)
    print(f'Você ganhou 5% de desconto de o valor ficou de R${valor:.2f}')
elif escolha == 3:
    meses = int(input('Em quantos meses? '))
    if meses == 2:
        parcelas = preco / meses
        print(f'O preço se manteve. Pague R${preco:.2f} em 2 parcelas de R${parcelas:.2f} ')
    elif meses >= 3:
        valor = preco + (preco / 100 * 20)
        parcelas = valor / meses
        print(f'O preço subiu 20%, ficando no valor de R${valor:.2f} e {meses} parcelas de R${parcelas:.2f}')
else:
    print(f'Escolha um número válido')
